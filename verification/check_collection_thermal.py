#!/usr/bin/env python3
"""Verify the Gaussian collection boundary with complex thermal auxiliaries.

Usage:
    python verification/check_collection_thermal.py
    python verification/check_collection_thermal.py --seed 9242026 --samples-per-q 70

The calculation reconstructs full real quadrature scattering from U(2,q),
uses correlated gauge-invariant Gaussian idler occupations, and compares the
full partial-transpose CP spectrum with the two-block theorem. It also checks
the optimal heterodyne-feedback Schur complement and finite-energy NPT test.

Results are JSON on stdout. Exit status is zero on success and one on a
numerical verification failure. NumPy and SciPy are the only dependencies.
Singular corners are treated analytically in science/collection_boundary.md;
the random checks deliberately use well-defined finite feedback optimizers.
"""

import argparse
import json

import numpy as np
from scipy.linalg import expm


NEGATIVE_MODES = (1, 2, 4)
EFFICIENCIES = (0.0, 0.03, 0.37, 0.9, 1.0)
SIGNAL_OCCUPATIONS = (0.01, 0.4, 2.0)
CORNER_TOLERANCE = 1e-11


def realify(matrix):
    """Annihilation-coordinate complex map in all-q, then all-p order."""
    return np.block([[matrix.real, -matrix.imag],
                     [matrix.imag, matrix.real]])


def omega(modes):
    ident = np.eye(modes)
    zero = np.zeros_like(ident)
    return np.block([[zero, ident], [-ident, zero]])


def random_canonical(rng, negative_modes):
    modes = 2 + negative_modes
    signature = np.diag([1, 1] + [-1] * negative_modes)
    raw = rng.normal(size=(modes, modes)) + 1j * rng.normal(size=(modes, modes))
    hermitian = (raw + raw.conj().T) / 2
    return expm(0.35j * signature @ hermitian)


def quadrature_scatter(scattering):
    """Convert the complete Nambu map, not only its positive-output block."""
    modes = scattering.shape[0]
    annihilation = np.zeros((modes, modes), complex)
    creation = np.zeros_like(annihilation)
    annihilation[:2, :2] = scattering[:2, :2]
    annihilation[2:, 2:] = scattering[2:, 2:].conj()
    creation[:2, 2:] = scattering[:2, 2:]
    creation[2:, :2] = scattering[2:, :2].conj()
    return np.block([[(annihilation + creation).real,
                      -(annihilation - creation).imag],
                     [(annihilation + creation).imag,
                      (annihilation - creation).real]])


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def run_checks(seed, samples_per_q, atol, decision_tol):
    rng = np.random.default_rng(seed)
    spectral_error = 0.0
    noise_error = 0.0
    witness_error = 0.0
    physical_residual = 0.0
    checked = 0
    positive_cases = 0
    for q in NEGATIVE_MODES:
        modes = 2 + q
        for sample in range(samples_per_q):
            scattering = random_canonical(rng, q)
            trans = quadrature_scatter(scattering)
            physical_residual = max(
                physical_residual,
                float(np.max(np.abs(trans @ omega(modes) @ trans.T - omega(modes)))))
            a = scattering[:2, :2]
            b = scattering[:2, 2:]
            raw = rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))
            idler_occupation = raw @ raw.conj().T / (4 * q)
            other_occupation = float(rng.uniform(0, 0.8))
            if sample % 7 == 0:
                idler_occupation *= 0.0
                other_occupation = 0.0

            # This covariance is constructed before scattering. In particular,
            # the transpose on the idler occupation below is checked against
            # a separately transformed physical input covariance.
            full_occupation = np.zeros((modes, modes), complex)
            full_occupation[1, 1] = other_occupation
            full_occupation[2:, 2:] = idler_occupation
            input_covariance = realify(full_occupation + 0.5 * np.eye(modes))
            rows = [0, 1, modes, modes + 1]
            signal_cols = [0, modes]
            selected_trans = trans[rows, :]
            x = selected_trans[:, signal_cols]
            output_covariance = selected_trans @ input_covariance @ selected_trans.T
            y = output_covariance - 0.5 * x @ x.T
            occupation = (b @ (np.eye(q) + idler_occupation.T) @ b.conj().T
                          + other_occupation * np.outer(a[:, 1], a[:, 1].conj()))

            for efficiency in EFFICIENCIES:
                case = f"q={q}, sample={sample}, efficiency={efficiency}"
                l = np.diag([np.sqrt(efficiency), 1.0])
                l_real = realify(l)
                x_eff = l_real @ x
                y_eff = (l_real @ y @ l_real.T
                         + np.diag([(1-efficiency)/2, 0,
                                    (1-efficiency)/2, 0]))
                pt = np.diag([1, 1, 1, -1])
                x_pt = pt @ x_eff
                cp = (pt @ y_eff @ pt
                      + 0.5j * (omega(2) - x_pt @ omega(1) @ x_pt.T))
                t = l @ a[:, 0]
                cmat = l @ occupation @ l
                minus = np.diag([1.0, 0.0]) - np.outer(t, t.conj()) + cmat
                plus = np.diag([0.0, 1.0]) + cmat
                full_eigenvalues = np.linalg.eigvalsh(cp)
                predicted = np.sort(np.r_[np.linalg.eigvalsh(minus),
                                          np.linalg.eigvalsh(plus)])
                require(np.isfinite(full_eigenvalues).all(), f"Nonfinite CP spectrum: {case}")
                spectral_error = max(
                    spectral_error, float(np.max(np.abs(full_eigenvalues-predicted))))

                a11 = float(minus[0, 0].real)
                require(a11 > CORNER_TOLERANCE,
                        f"Near-singular optimizer; use the analytical corner proof: {case}")
                # This gain multiplies the collected output, without rescaling
                # the measurement back to the pre-loss reflected amplitude.
                feedback = -minus[0, 1].conj() / a11
                gain = float(abs(t[1] + feedback * t[0])**2)
                noise = float((cmat[1, 1]
                               + abs(feedback)**2 * (cmat[0, 0] + 1)
                               + 2 * np.real(feedback * cmat[0, 1])).real)
                schur = -float(np.linalg.det(minus).real) / a11
                noise_error = max(noise_error, abs((gain-noise)-schur))
                require(noise >= max(0.0, gain-1)-atol,
                        f"Corrected channel violates the physical noise floor: {case}")

                for injected in SIGNAL_OCCUPATIONS:
                    occ_a = injected
                    occ_b = gain * injected + noise
                    pair_sq = gain * injected * (injected+1)
                    gap = pair_sq-occ_a*occ_b
                    witness_error = max(witness_error, abs(gap-injected*schur))
                    ppt_cov = np.array([[occ_a+0.5, np.sqrt(pair_sq)],
                                        [np.sqrt(pair_sq), occ_b+0.5]])
                    smallest_ppt = np.linalg.eigvalsh(ppt_cov)[0]
                    if abs(schur) > decision_tol:
                        require((smallest_ppt < 0.5) == (schur > 0),
                                f"Finite-energy PPT sign disagrees: {case}, input={injected}")
                require((full_eigenvalues[0] >= -atol) == (schur <= atol),
                        f"Full CP test disagrees with feedback boundary: {case}")
                positive_cases += int(schur > atol)
                checked += 1

    errors = dict(
        canonical_quadrature=physical_residual,
        full_cp_spectrum=spectral_error,
        feedback_schur=noise_error,
        finite_energy_npt_gap=witness_error,
    )
    require(max(errors.values()) < atol,
            f"Maximum residual exceeds absolute tolerance {atol}: {errors}")
    return dict(
        passed=True,
        check="collection_thermal",
        seed=seed,
        samples_per_negative_mode_count=samples_per_q,
        negative_mode_counts=list(NEGATIVE_MODES),
        efficiencies=list(EFFICIENCIES),
        signal_occupations=list(SIGNAL_OCCUPATIONS),
        channel_cases=checked,
        finite_energy_cases=checked*len(SIGNAL_OCCUPATIONS),
        positive_capacity_cases=positive_cases,
        tolerances=dict(absolute=atol, sign_decision=decision_tol,
                        singular_optimizer=CORNER_TOLERANCE),
        max_absolute_errors=errors,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=9242026)
    parser.add_argument("--samples-per-q", type=int, default=70)
    parser.add_argument("--atol", type=float, default=1e-10,
                        help="Absolute residual tolerance (default: 1e-10).")
    parser.add_argument("--decision-tol", type=float, default=1e-8,
                        help="Minimum Schur margin for finite-energy sign checks.")
    args = parser.parse_args(argv)
    if args.seed < 0 or args.samples_per_q < 1:
        parser.error("seed must be nonnegative and samples-per-q must be positive")
    if not np.isfinite(args.atol) or args.atol <= 0:
        parser.error("atol must be finite and positive")
    if not np.isfinite(args.decision_tol) or args.decision_tol < args.atol:
        parser.error("decision-tol must be finite and at least atol")
    try:
        result = run_checks(args.seed, args.samples_per_q, args.atol, args.decision_tol)
    except (ArithmeticError, np.linalg.LinAlgError) as exc:
        print(json.dumps(dict(passed=False, check="collection_thermal",
                              seed=args.seed, error=str(exc)), indent=2))
        return 1
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

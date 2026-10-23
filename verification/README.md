# Reproducing the scientific checks

The analytical arguments live in the [science account](../science/model.md).
This directory supplies finite, deterministic checks of their algebra,
covariance calculations and explicit physical construction. These programs
do not replace the infinite-dimensional local-instrument proof, the coding
theorems, the continuum argument or a comparison with prior literature.

## Run the suite

The recorded environment is Python **3.12.14**, NumPy **2.3.5**, SciPy
**1.17.0** and Matplotlib **3.10.8**. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py --output verification/results.json
```

The runner launches each `check_*.py` in a fresh process, fails on any
nonzero exit, and combines its JSON results. The final output is:

```text
PASS check_atomic_model.py
PASS check_collection_thermal.py
PASS check_collection_vacuum.py
PASS check_rates.py
PASS check_scattering.py
Saved verification/results.json
PASS: 5 scientific check programs
```

The checked-in [results.json](results.json) contains the full numerical
output. A fresh run overwrites it only when `--output` is supplied. Last
floating-point digits can vary with the numerical libraries and platform;
the assertions use explicit tolerances. None of the checks needs network
access, credentials, external data, or a testing framework. Numerical checks
must be run without Python's `-O` flag, which disables assertions.

## Claim-to-check map

| Program | Independent construction or check | Recorded evidence |
|---|---|---|
| [check_collection_vacuum.py](check_collection_vacuum.py) | Reconstruct the full real-quadrature partial-transpose CP matrix for complex canonical blocks; compare its spectrum and sign with the scalar boundary, including efficiency endpoints and equality cases | 1,530 cases; maximum spectral error $`1.78\times10^{-14}`$ |
| [check_collection_thermal.py](check_collection_thermal.py) | Build physical gauge-invariant auxiliary covariance matrices, including correlated idlers; compare full CP spectra, optimal feedback and a finite-energy NPT witness | 1,050 channel cases and 3,150 finite-energy cases; maximum listed residual $`2.11\times10^{-13}`$ |
| [check_rates.py](check_rates.py) | Propagate a full TMSV covariance, heterodyne by a Schur complement, calculate symplectic spectra; check the Choi cubic by exact rational trace/minor/determinant identities; compare finite squeezing with its limit and the PLOB formula with its integral | 80 conditional covariance cases, 30 exact rational polynomial cases; covariance residual $`2.54\times10^{-14}`$ |
| [check_scattering.py](check_scattering.py) | Construct sharp noise matrices, sample admissible complex canonical blocks, test feasibility and the extra-positive-port correction; explicitly check a passive counterexample | 2,000 random cases; saturator residual $`3.56\times10^{-15}`$ |
| [check_atomic_model.py](check_atomic_model.py) | Complete the particle-hole canonical dynamics, check drift stability and resonant scattering, enumerate atomic selection conditions, compare integrated flux with the stationary covariance, and retain all packet auxiliary Gram matrices | Canonical error $`2.23\times10^{-15}`$; minimum tested drift margin $`0.2199515671\kappa`$; finite-packet NPT example below |

Case counts describe finite checks, not a probability of theorem correctness.
The stability bound and resonance-selection uniqueness also have analytical
derivations in [the atomic model](../science/stable_atomic_model.md); sampled
values do not alone establish a uniform bound. The code's microscopic
selection calculation tests the displayed free-ring resonances. It is not a
many-body simulation of pump depletion or a realized atom experiment.

## Reference numerical values

For unity forward gain and reverse power $`R=0.01`$:

| Quantity | Expected value |
|---|---:|
| General reduced-channel upper envelope $`F(1,R)`$ | $`0.00007261928623`$ |
| Ideal-collection achievable rate $`I_1(R)`$ | $`0.002772854522`$ |
| Full ideal-collection quantum-capacity upper bound $`U(R)`$ | $`0.028624834491`$ |
| Collection threshold $`\eta_{\rm crit}`$ | $`0.987654320988`$ |
| Finite-packet PT symplectic eigenvalue, $`\sigma/\kappa=0.01`$, mean-one probe | $`0.497235712955`$ |
| Receiver occupation for that centered finite packet | $`0.998765982108`$ |

The finite-packet partial-transpose eigenvalue is below the vacuum value
$`1/2`$. It witnesses an entangled resource at this operating point. It
does not compute the packet's optimal capacity or establish a rate per
second. The table's reduced-channel number is a general bound; this stable
family's actual discarded-return capacity is zero at this operating point.

At perfect reverse isolation, the effective model's vacuum spectral
occupations are $`(1,2,3)`$ for source, receiver and idler. Its integrated
three-output flux is instead

```math
\frac{\Gamma_{\rm all}}\kappa
=\frac{11}{13+6\sqrt2}=0.511978400860.
```

The numerical integral agrees with the stationary covariance and this
analytic expression. Spectral occupation, intracavity population and
integrated flux have different meanings and units.

## Figure

Generate [rates-and-collection.svg](../figures/rates-and-collection.svg) with:

```bash
python verification/plot_results.py
```

The plot imports the verified rate functions from `check_rates.py`. It uses
$`G=1`$ and $`10^{-4}\le R\le0.24`$, within the family's reduced-channel
entanglement-breaking range. Panel A shows the exact functions $`I_1,U,F`$
from [Communication rates](../science/communication_rates.md), with a shaded
band between the ideal-collection quantum-capacity bounds. The curve $`F`$
is a reduced-channel upper envelope for the full model class, not this
family's actual reduced capacity. Panel B shows
$`1-\eta_{\rm crit}=R/(1-\sqrt R)^2`$: the positive region is strictly
below the curve, and equality is on the zero-capacity side.

The SVG is generated directly by Matplotlib, contains no external assets,
and has deterministic SVG identifiers. The script also writes a disposable
PNG preview in the system temporary directory for visual inspection.

## What remains analytical or model-dependent

The arbitrary-input and adaptive converse relies on the exact separable
faithful-state/instrument construction, rather than finite Fock cutoffs in
a numerical test. Positivity uses Gaussian NPT distillability with general
local operations. The rate upper bound uses local teleportation simulation
with the stated order of limits and logarithmic negativity. Those external
theorems are attributed in [Related work](../references/RELATED_WORK.md).

The microscopic atomic implementation requires the stated condensate,
drive, reference, filtering and Markov approximations. Finite checks of its
effective scattering equations do not remove those assumptions. A
frequency-local result alone is not a whole-band result; the
[finite-bandwidth account](../science/finite_bandwidth.md) supplies the
separate hypotheses and temporal-mode bookkeeping.

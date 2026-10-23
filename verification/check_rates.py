"""Independent covariance and exact-polynomial checks for communication_rates.md.

Run directly with Python. The finite tests audit analytic formulas; they do not
prove the asymptotic capacity converse or replace its cited theorems.
"""

from fractions import Fraction as F
import json
import numpy as np
from scipy.integrate import quad


def entropy(n):
    n = np.asarray(n, dtype=float)
    if np.any(n < -1e-10):
        raise ValueError("Negative thermal occupation")
    n = np.maximum(n, 0)
    # A scalar loop avoids evaluating log(0) in an unused np.where branch.
    out = np.zeros_like(n)
    positive = n > 0
    out[positive] = ((n[positive] + 1) * np.log1p(n[positive])
                     - n[positive] * np.log(n[positive])) / np.log(2)
    return float(out) if out.ndim == 0 else out


def lower_bound(reverse):
    x = reverse / (2 - np.sqrt(reverse)) ** 2
    return 2 - entropy(1 - x)


def upper_bound(reverse):
    p = 1 - np.sqrt(reverse)
    return np.log2((p*p + reverse + np.sqrt(1 + 4*reverse*p*p)) / (2*p))


def reduced_bound(gain, reverse):
    if not (0 <= reverse < min(gain, 1)):
        raise ValueError("Integral check uses the interior domain")
    return quad(lambda u: (reverse-u)/((1-u)*(gain-u)), 0, reverse,
                epsabs=1e-14, epsrel=1e-12)[0] / np.log(2)


def realify(a):
    ans = np.empty((2*a.shape[0], 2*a.shape[1]))
    ans[0::2, 0::2] = a.real
    ans[0::2, 1::2] = -a.imag
    ans[1::2, 0::2] = a.imag
    ans[1::2, 1::2] = a.real
    return ans


def symplectic_values(cov):
    omega = np.kron(np.eye(cov.shape[0]//2), [[0, 1], [-1, 0]])
    # Every symplectic eigenvalue occurs twice; group adjacent equal values.
    vals = np.sort(np.abs(np.linalg.eigvals(1j*omega @ cov)))
    return (vals[0::2] + vals[1::2])/2


def joint_covariance(gain, reverse, n):
    """Build the three-mode output from a full input covariance and channel."""
    f, b = np.sqrt(gain), np.sqrt(reverse)
    d = f - b
    r = np.sqrt((1-b)*(1+f))
    a = np.array([[r, b], [-f, r]], complex)
    noise = a @ a.conj().T - np.eye(2)
    v = np.zeros((6, 6))
    v[:2, :2] = (n+.5)*np.eye(2)
    v[2:, 2:] = .5*np.eye(4) + realify(noise)
    transfer = realify(a[:, :1])
    v[2:, 2:] += n * transfer @ transfer.T
    cross = np.sqrt(n*(n+1)) * np.diag([1, -1]) @ transfer.T
    v[:2, 2:] = cross
    v[2:, :2] = cross.T
    return v


def conditional_check(gain, reverse, n):
    cov = joint_covariance(gain, reverse, n)
    kept = [0, 1, 4, 5]
    measured = [2, 3]
    k = cov[np.ix_(kept, kept)]
    c = cov[np.ix_(kept, measured)]
    v = k - c @ np.linalg.solve(cov[np.ix_(measured, measured)] + .5*np.eye(2), c.T)
    f, b = np.sqrt(gain), np.sqrt(reverse)
    d = f - b
    den = (1-b)*(1+f)*n + d*(1-b) + 1
    na = n*reverse/den
    nb = (n+1)*(1+d)**2/den - 1
    m = -np.sqrt(n*(n+1))*b*(1+d)/den
    expected = np.diag([na+.5, na+.5, nb+.5, nb+.5])
    expected[:2, 2:] = expected[2:, :2] = np.diag([m, -m])
    err = np.max(abs(v-expected))
    sym = symplectic_values(v)
    err = max(err, np.max(abs(sym - [.5, nb-na+.5])),
              abs(m*m-na*(nb+1)))
    assert err < 2e-9
    if reverse > 0:
        assert entropy(nb)-entropy(nb-na) > 0
    return err


def polynomial_check():
    """Exact rational trace/minor/determinant identities, no radical numerics."""
    cases = 0
    for s in [F(0), F(1,100), F(1,10), F(1,2), F(9,10), F(1)]:
        p = 1-s
        for n in [F(0), F(1,10), F(1), F(10), F(10000)]:
            aa = n+F(1,2)
            dd = 2*p*n+p*p+F(1,2)
            ff = n+2*p+F(1,2)
            b2 = 2*p*n*(n+1)
            c2 = n*(n+1)
            e2 = 2*p*(n+p)**2
            bce = 2*p*n*(n+1)*(n+p)
            trace = -aa+dd-ff
            second = -aa*dd+b2+aa*ff-c2-dd*ff+e2
            det = aa*dd*ff+2*bce-aa*e2-dd*c2-ff*b2
            assert -trace == 2*s*n+F(3,2)-s*s
            assert second == -(p*p+s*s)*n-p*p-F(1,4)
            assert -det == -p*n/2-p*p/4-p/2-F(1,8)
            cases += 1
    return cases


def finite_logneg(reverse, n):
    v = joint_covariance(1, reverse, n)
    pt = np.diag([1, 1, 1, 1, 1, -1])
    sym = symplectic_values(pt @ v @ pt)
    return np.maximum(0, -np.log2(2*sym)).sum()


def main():
    errors = []
    for gain in [.2, 1, 2, 5]:
        for reverse in [0, .0001, .01, .1, min(gain,1)*.9]:
            if reverse > min(gain,1):
                continue
            for n in [.01, .2, 1, 10]:
                errors.append(conditional_check(gain, reverse, n))
    exact = polynomial_check()
    limits = []
    for reverse in [.0001, .01, .1, .25, .81]:
        value = finite_logneg(reverse, 10000)
        limit = upper_bound(reverse)
        # A finite Choi probe need not saturate the asymptotic resource bound.
        assert 0 <= limit-value < 5e-4
        limits.append({"R": reverse, "finite_n_10000": value, "limit": limit})
    for reverse in np.geomspace(1e-6, .95, 100):
        assert 0 < lower_bound(reverse) <= upper_bound(reverse)
    r = 1e-5
    assert abs(lower_bound(r)/r - .25) < .001
    assert abs(upper_bound(r)/r - 2/np.log(2)) < .001
    for gain in [.2, 1, 5]:
        val = reduced_bound(gain, r)
        assert abs(val/(r*r/(2*gain*np.log(2)))-1) < 1e-4
    for gain in [.2, .9, 1, 1.1, 5]:
        for reverse in [.0001, .01, .1]:
            numerical = reduced_bound(gain, reverse)
            if gain == 1:
                formula = (-reverse-np.log1p(-reverse))/np.log(2)
            else:
                formula = ((gain-reverse)*np.log1p(-reverse/gain)
                           -(1-reverse)*np.log1p(-reverse))/(1-gain)/np.log(2)
            assert abs(formula-numerical) < 1e-12
    example = .01
    print(json.dumps({
        "conditional_covariance_cases": len(errors),
        "maximum_covariance_or_entropy_spectrum_error": max(errors),
        "exact_rational_polynomial_cases": exact,
        "finite_choi_limit_checks": limits,
        "example_R_0.01": {
            "reduced_upper_bound": reduced_bound(1,example),
            "ideal_collection_lower_bound": lower_bound(example),
            "ideal_collection_upper_bound": upper_bound(example),
            "collection_threshold": (1-2*np.sqrt(example))/(1-np.sqrt(example))**2,
        },
        "status": "PASS",
    }, indent=2))


if __name__ == "__main__":
    main()

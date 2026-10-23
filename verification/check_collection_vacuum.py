"""Independent reconstruction of the full-output Gaussian partial-transpose CP test.

The source holds the reference and a loss-attenuated reflected output; the
receiver holds one positive-norm output. All other inputs are vacuum and all
negative-norm outputs are traced. This is independent of the reduced 2x2 proof.
"""
import json
import numpy as np


def realify(a):
    out = np.empty((2*a.shape[0], 2*a.shape[1]))
    out[0::2, 0::2] = a.real
    out[0::2, 1::2] = -a.imag
    out[1::2, 0::2] = a.imag
    out[1::2, 1::2] = a.real
    return out


def test(a, efficiency):
    noise = a @ a.conj().T - np.eye(2)
    assert np.linalg.eigvalsh(noise)[0] > -1e-12
    loss = np.diag([np.sqrt(efficiency), 1.0])
    x = realify(loss @ a[:, :1])
    # Full vacuum output covariance, then subtract the signal's vacuum input.
    v = np.eye(4)/2 + realify(loss @ noise @ loss)
    y = v - x @ x.T / 2
    omega1 = np.array([[0, 1], [-1, 0]])
    omega2 = np.kron(np.eye(2), omega1)
    pt = np.diag([1, 1, 1, -1])
    xpt = pt @ x
    cp = pt @ y @ pt + 0.5j*(omega2 - xpt @ omega1 @ xpt.T)
    direct = np.linalg.eigvalsh(cp)
    reverse = abs(a[0, 1])**2
    forward = abs(a[1, 0])**2
    c = noise[1, 1].real - forward
    m = np.array([[1-efficiency*(1-reverse),
                   np.sqrt(efficiency)*a[0, 1]*a[1, 1].conjugate()],
                  [np.sqrt(efficiency)*a[0, 1].conjugate()*a[1, 1], c]])
    other = np.diag([0, 1]) + loss @ noise @ loss
    reduced = np.sort(np.concatenate([np.linalg.eigvalsh(m),
                                     np.linalg.eigvalsh(other)]))
    mismatch = np.max(abs(direct-reduced))
    condition = c >= -1e-11 and (1-efficiency)*c >= efficiency*reverse-1e-11
    assert (direct[0] >= -1e-11) == condition
    assert mismatch < 1e-10
    return mismatch


if __name__ == '__main__':
    rng = np.random.default_rng(20261023)
    errors = []
    for _ in range(500):
        u, _ = np.linalg.qr(rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))
        v, _ = np.linalg.qr(rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))
        singular = 1 + rng.random(2)*4
        if rng.random() < 0.5:
            singular[0] = 1.0  # Includes rank-one idler/noise sector.
        a = u @ np.diag(singular) @ v.conj().T
        for efficiency in [0.0, 1.0, rng.random()]:
            errors.append(test(a, efficiency))
    for reverse in [0.0, 0.0001, 0.01, 0.1, 0.25, 0.49]:
        b = np.sqrt(reverse)
        r = np.sqrt(2*(1-b))
        a = np.array([[r, b], [-1, r]], dtype=complex)
        c = r*r-1
        critical = c/(c+reverse) if c > 0 else 0.0
        for efficiency in [0, 1, critical, max(0, critical-1e-7), min(1, critical+1e-7)]:
            errors.append(test(a, efficiency))
    print(json.dumps({'cases':len(errors), 'max_spectrum_error':max(errors),
                      'criterion':'N>=G and (1-efficiency)*(N-G)>=efficiency*R'}))

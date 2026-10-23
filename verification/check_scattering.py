"""Canonical scattering, sharp noise constructions and port-accounting checks."""
import json
import numpy as np


def positive_noise_family(f, b):
    d = f-b
    r = np.sqrt((1-b)*(1+f))
    a = np.array([[r,b],[-f,r]], complex)
    noise_column = np.sqrt(d)*np.array([[np.sqrt(1-b)],[-np.sqrt(1+f)]])
    return a, noise_column


def receiver_saturator(gain, reverse, ell=0):
    t = reverse+ell
    u = np.array([-np.sqrt(1-t),np.sqrt(t)])
    v = np.array([np.sqrt(t),np.sqrt(1-t)])
    a = np.column_stack([np.sqrt(gain/t)*u,np.sqrt(reverse/t)*v])
    c = np.sqrt(ell/t)*v[:,None]
    b = np.sqrt(gain/t-1)*u[:,None]
    return a,b,c


def main():
    rng = np.random.default_rng(20261023)
    residuals, slacks = [], []
    for f,b in [(1,0),(.8,.3),(2,.5),(1.5,1),(1,1),(.1,0)]:
        a,noise = positive_noise_family(f,b)
        residuals.append(np.max(abs(a@a.conj().T-noise@noise.conj().T-np.eye(2))))
        assert abs(np.sum(abs(noise)**2)-(f-b)*(f-b+2)) < 1e-12
    for gain,reverse,ell in [(1,.01,0),(1,0,.01),(.8,.03,.02),(5,.1,.2),(1,0,1)]:
        a,b,c = receiver_saturator(gain,reverse,ell)
        residuals.append(np.max(abs(a@a.T+c@c.T-b@b.T-np.eye(2))))
        assert abs((b@b.T)[1,1]-(gain-reverse-ell)) < 1e-12
        assert abs((c@c.T)[0,0]-ell) < 1e-12
    # A passive additional port invalidates a noise bound based on R alone.
    a=np.array([[0,0],[1,0]])
    c=np.array([[1],[0]])
    assert np.array_equal(a@a.T+c@c.T,np.eye(2))
    for _ in range(2000):
        u,_ = np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)))
        v,_ = np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)))
        singular=1+3*rng.random(2)
        a=u@np.diag(singular)@v
        n=a@a.conj().T-np.eye(2)
        gain,reverse=abs(a[1,0])**2,abs(a[0,1])**2
        d=abs(np.sqrt(gain)-np.sqrt(reverse))
        slack=np.trace(n).real-d*(d+2)
        assert slack >= -1e-11
        assert n[1,1].real >= gain-reverse-1e-11
        # The phase-minimized feasibility inequality is necessary for this A.
        source,receiver=n[0,0].real,n[1,1].real
        lhs=(np.sqrt(gain)*np.sqrt(max(0,1+source-reverse))
             -np.sqrt(reverse)*np.sqrt(max(0,1+receiver-gain)))**2
        assert lhs <= source*receiver+1e-9
        slacks.append(slack)
    assert max(residuals) < 1e-11
    print(json.dumps({"random_canonical_cases":len(slacks),
                      "maximum_saturator_residual":float(max(residuals)),
                      "minimum_total_noise_slack":float(min(slacks)),
                      "passive_extra_port_counterexample":"PASS",
                      "status":"PASS"},indent=2))


if __name__ == "__main__":
    main()

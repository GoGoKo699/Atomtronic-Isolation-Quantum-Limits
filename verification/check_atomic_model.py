"""Stable atomic model, microscopic selection and finite-wavepacket checks.

Dimensionless microscopic energies are m**2 * hbar*omega_L.  Scattering
frequencies and linewidths are separately expressed in units of kappa.
This checks explicit assumptions and consequences, not laboratory readiness.

Run with Python 3, NumPy and SciPy.  Standard output is deterministic JSON;
all failures raise AssertionError.  No files or scratch imports are needed.
"""

import json
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov


def resonances(scale=1):
    """Enumerate first-order pair/normal processes driven by each grating."""
    a, c, b = scale, 2 * scale, 3 * scale
    extent = 10 * scale + 10
    out = {}
    for name, Q, Omega, target in [
        ("pair_ac", a+c, a*a+c*c, (a,c)),
        ("pair_bc", b+c, b*b+c*c, (c,b)),
    ]:
        pairs = []
        pair_detunings = []
        normal = []
        normal_detunings = []
        for m in range(-extent, extent+1):
            n = Q-m
            if m <= n:
                detuning = m*m+n*n-Omega
                if detuning == 0:
                    pairs.append([m,n])
                else:
                    pair_detunings.append(abs(detuning))
            detuning = (m+Q)**2-m*m-Omega
            if detuning == 0:
                normal.append([m,m+Q])
            else:
                normal_detunings.append(abs(detuning))
        assert pairs == [list(target)], (name,pairs,target)
        out[name] = dict(Q=Q,Omega=Omega,pair_resonances=pairs,
                         normal_resonances=normal,
                         minimum_other_pair_gap=min(pair_detunings),
                         minimum_normal_gap=min(normal_detunings),
                         forced_pump_gap=abs(Q*Q-Omega))
    Q, Omega = b-a, b*b-a*a
    normal = [[m,m+Q] for m in range(-extent,extent+1)
              if (m+Q)**2-m*m == Omega]
    assert normal == [[a,b]]
    out["bragg_ab"] = dict(Q=Q,Omega=Omega,normal_resonances=normal,
                             minimum_other_normal_gap=2*abs(Q))
    return out


def matrix_family(reverse_power):
    b = np.sqrt(reverse_power)
    d = 1-b
    r = np.sqrt(2*d)
    p = (2-r)/(2+r)
    u = r/(2+r)
    K = .5j*np.array([[0,p,u],[-p,0,-u],[u,-u,0]],complex)
    delay_source = 3-b+1.5*r
    delay_receiver = 4-2*b+2*r
    return K,np.array([delay_source,delay_receiver])


def stable_family_checks():
    """Check the full annihilation/creation completion as well as reduced S."""
    metric3=np.diag([1.,1.,-1.])
    metric6=np.diag([1.,1.,1.,-1.,-1.,-1.])
    swap=np.block([[np.zeros((3,3)),np.eye(3)],
                   [np.eye(3),np.zeros((3,3))]])
    bound=.5*(1-np.sqrt(8*np.sqrt(2)-11))
    errors=[]
    margins=[]
    for R in [0.,.0001,.01,.1,.5,1.]:
        K,_=matrix_family(R)
        beta=np.sqrt(R);d=1-beta;r=np.sqrt(2*d)
        expected=-np.array([[r,beta,d],[-1,r,-r],[r,-d,1+d]])
        J=K[0,1];Ga=K[0,2];Gb=K[1,2]
        h=np.array([[0,J,0],[J.conjugate(),0,0],[0,0,0]],complex)
        delta=np.array([[0,0,Ga],[0,0,Gb],[Ga,Gb,0]],complex)
        full=np.block([[h,delta],[-delta.conj(),-h.conj()]])
        indices=[0,1,5]
        assert np.max(abs(full[np.ix_(indices,indices)]-K))<2e-14
        drift=-1j*full-.5*np.eye(6)
        margin=-np.max(np.linalg.eigvals(drift).real)
        assert margin>=bound-2e-14
        margins.append(float(margin))
        assert np.max(abs(K.conj().T@metric3-metric3@K))<2e-14
        for omega in [0.,.1,.9]:
            S=np.eye(3)-np.linalg.inv(.5*np.eye(3)+1j*K-1j*omega*np.eye(3))
            S6=np.eye(6)-np.linalg.inv(.5*np.eye(6)+1j*full-1j*omega*np.eye(6))
            Sm6=np.eye(6)-np.linalg.inv(.5*np.eye(6)+1j*full+1j*omega*np.eye(6))
            error=max(np.max(abs(S@metric3@S.conj().T-metric3)),
                      np.max(abs(S6@metric6@S6.conj().T-metric6)),
                      np.max(abs(S6-swap@Sm6.conj()@swap)))
            assert error<2e-13
            errors.append(float(error))
            if omega==0:
                assert np.max(abs(S-expected))<2e-14
                assert abs(abs(S[1,0])**2-1)<2e-14
                assert abs(abs(S[0,1])**2-R)<2e-14
                assert np.max(abs(abs(S[:2,2])**2-[d*d,2*d]))<2e-14
                assert abs(np.sum(abs(S[2,:2])**2)-d*(d+2))<2e-14
    return dict(carrier_parameters=6,frequency_points_per_parameter=3,
                maximum_canonical_completion_error=max(errors),
                minimum_drift_margin_over_kappa=min(margins),
                analytic_uniform_margin_over_kappa=float(bound))


def vacuum_budget(reverse_power):
    """Intracavity occupations; all physical-port vacuum fluxes in units kappa."""
    K,_=matrix_family(reverse_power)
    drift=-1j*K-.5*np.eye(3)
    covariance=solve_continuous_lyapunov(drift,-np.diag([1.,1.,0.]))
    occupations=np.diag(covariance).real-np.array([1.,1.,0.])
    assert abs(occupations[0]+occupations[1]-occupations[2])<2e-12
    b=np.sqrt(reverse_power);r=np.sqrt(2*(1-b))
    nc=r*r*(3*r*r+16)/(4*(3*r*r+12*r+20))
    assert abs(nc-occupations[2])<2e-12
    return dict(reverse_carrier=reverse_power,
                intracavity_occupations=occupations.tolist(),
                positive_flux_over_kappa=float(occupations[:2].sum()),
                idler_flux_over_kappa=float(occupations[2]),
                all_physical_flux_over_kappa=float(occupations.sum()))


def integrated_vacuum_check():
    """Independent scattering-spectrum integral fixes the flux convention."""
    K,_=matrix_family(0.)
    def spectral_flux(omega):
        S=np.eye(3)-np.linalg.inv(.5*np.eye(3)+1j*K-1j*omega*np.eye(3))
        positive=np.sum(abs(S[:2,2])**2)
        idler=np.sum(abs(S[2,:2])**2)
        return float((positive+idler)/np.pi)
    integral,error=quad(spectral_flux,0.,np.inf,epsabs=2e-12,epsrel=2e-12)
    exact=11/(13+6*np.sqrt(2))
    assert abs(integral-exact)<2e-12
    return dict(all_physical_flux_over_kappa=float(integral),
                analytic_flux_over_kappa=float(exact),
                quadrature_error_estimate=float(error))


def centered_probe(A,Bgram,probe_occupation=1.):
    """Finite TMSV probe; heterodyne source return and center both parties.

    N_ij=<d_i^dagger d_j>, P_ij=<d_i d_j>, with modes ordered as
    reference, source output, receiver output. All temporal auxiliary
    inputs represented by the packet channel's Gram matrices are vacuum.
    """
    n=probe_occupation
    N=np.zeros((3,3),complex)
    P=np.zeros((3,3),complex)
    N[0,0]=n
    N[1:,1:]=n*np.outer(A[:,0].conj(),A[:,0])+Bgram.T
    P[0,1:]=np.sqrt(n*(n+1))*A[:,0]
    P[1:,0]=P[0,1:]
    V=np.zeros((6,6))
    for i in range(3):
        for j in range(3):
            vacuum=.5 if i==j else 0.
            V[2*i,2*j]=vacuum+(N[i,j]+P[i,j]).real
            V[2*i+1,2*j+1]=vacuum+(N[i,j]-P[i,j]).real
            V[2*i,2*j+1]=(P[i,j]+N[i,j]).imag
            V[2*i+1,2*j]=(P[i,j]-N[i,j]).imag
    keep=[0,1,4,5];measure=[2,3]
    cross=V[np.ix_(keep,measure)]
    gain=cross@np.linalg.inv(V[np.ix_(measure,measure)]+.5*np.eye(2))
    conditional=V[np.ix_(keep,keep)]-gain@cross.T
    partial_transpose=np.diag([1.,1.,1.,-1.])
    Vpt=partial_transpose@conditional@partial_transpose
    symplectic=np.kron(np.eye(2),np.array([[0,1],[-1,0]]))
    nu=float(np.min(abs(np.linalg.eigvals(1j*symplectic@Vpt))))
    uncertainty=float(np.min(np.linalg.eigvalsh(Vpt+.5j*symplectic)))
    return dict(reference_occupation=float((np.trace(conditional[:2,:2])-1)/2),
                receiver_occupation=float((np.trace(conditional[2:,2:])-1)/2),
                partially_transposed_symplectic_minimum=nu,
                partially_transposed_uncertainty_minimum=uncertainty,
                maximum_conditional_mean_gain=float(np.max(abs(gain))),
                entangled=bool(nu<.5-1e-12))


def centered_carrier_checks():
    """Verify the bounded-output analytic finite-probe formulas."""
    results=[]
    for R in [0.,.0001,.01,.1,.5,1.]:
        K,_=matrix_family(R)
        S=np.eye(3)-np.linalg.inv(.5*np.eye(3)+1j*K)
        Bgram=S[:2,2:]@S[:2,2:].conj().T
        result=centered_probe(S[:2,:2],Bgram)
        x=R/(2-np.sqrt(R))**2
        nu=(x+2-np.sqrt(x*x+6*x+1))/2
        assert abs(result['reference_occupation']-x)<2e-14
        assert abs(result['receiver_occupation']-1)<2e-14
        assert abs(result['partially_transposed_symplectic_minimum']-nu)<2e-14
        assert result['entangled']==bool(R>0)
        result['reverse_carrier']=R
        results.append(result)
    return results


def wavepacket(reverse_power, sigma, quadrature_order=160):
    """Gaussian packets; output phases remove the two signal group delays.

    Aeff is the matrix between two selected input and output wavepackets.
    Cgram is the exact Gram matrix of all discarded positive input temporal
    modes.  Bgram includes the continuum of negative/idler temporal modes.
    """
    K, delays = matrix_family(reverse_power)
    nodes, weights = hermgauss(quadrature_order)
    frequencies = np.sqrt(2)*sigma*nodes
    weights = weights/np.sqrt(np.pi)
    Am = np.zeros((2,2),complex)
    Agram = np.zeros((2,2),complex)
    Bgram = np.zeros((2,2),complex)
    reverse_spectral = 0.
    for omega, weight in zip(frequencies,weights):
        S = np.eye(3)-np.linalg.inv(.5*np.eye(3)+1j*K-1j*omega*np.eye(3))
        phase = np.diag(np.exp(-1j*omega*delays))
        A = phase@S[:2,:2]
        B = phase@S[:2,2:]
        Am += weight*A
        Agram += weight*(A@A.conj().T)
        Bgram += weight*(B@B.conj().T)
        reverse_spectral += weight*abs(S[0,1])**2
    Cgram = Agram-Am@Am.conj().T
    residual = np.max(abs(Am@Am.conj().T+Cgram-Bgram-np.eye(2)))
    assert residual < 2e-12
    assert np.min(np.linalg.eigvalsh(Cgram)) > -2e-12
    G = abs(Am[1,0])**2
    R = abs(Am[0,1])**2
    ell_source = Cgram[0,0].real
    noise_receiver = Bgram[1,1].real
    t = R+ell_source
    assert noise_receiver >= G-t-2e-12
    result = dict(reverse_carrier=reverse_power,sigma_over_kappa=sigma,
                  G_packet=float(G),R_packet=float(R),
                  R_spectral=float(reverse_spectral),
                  ell_source=float(ell_source),t_packet=float(t),
                  variance_reflection=float(t-reverse_spectral),
                  N_receiver=float(noise_receiver),
                  canonical_residual=float(residual))
    result['conditional_centering']=centered_probe(Am,Bgram)
    if reverse_power > 0:
        k = -Am[1,1]/Am[0,1]
        row = np.array([k,1.])
        gain = abs(row@Am[:,0])**2
        noise = (row@Bgram@row.conj()).real+abs(k)**2
        extra_positive = (row@Cgram@row.conj()).real
        assert abs(noise-gain-(extra_positive-1)) < 2e-9
        result.update(recovery_gain=float(gain),recovery_noise=float(noise),
                      recovery_positive_noise=float(extra_positive),
                      recovery_non_EB=bool(extra_positive<1))
    return result


if __name__ == "__main__":
    result={"stable_family":stable_family_checks(),
            "microscopic_m1":resonances(1),
            "microscopic_m11":resonances(11),
            "vacuum_budgets":[vacuum_budget(R) for R in [0.,.01,.1,.5,1.]],
            "integrated_vacuum_flux":integrated_vacuum_check(),
            "centered_carriers":centered_carrier_checks(),
            "wavepackets":[]}
    for R in [0.,.01,.1]:
        for sigma in [.0005,.002,.01,.03]:
            packet=wavepacket(R,sigma)
            if R>0:
                assert packet['conditional_centering']['entangled']
            result["wavepackets"].append(packet)
    print(json.dumps(result,indent=2))

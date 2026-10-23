# A stable pumped atomic module

The three-mode channel in [Model and main results](model.md) has an explicit
stable Hamiltonian realization. Its atomic interpretation can be obtained
from a number-conserving contact-interaction model with two driven collision
processes and one Bragg conversion. The exact scattering formulas below
belong to the effective linear model. The reduction from the many-atom model
requires an undepleted condensate, resolved resonances, controlled unwanted
modes, and specified phase references.

The construction describes a driven matter-wave frequency converter. It
does not identify a finite-bias Josephson critical-current asymmetry with
linear scattering on a fixed background. See [Physical interpretation](interpretation.md)
for the operational distinction.

## 1. Hamiltonian and the physical channels

Let $`a,b,c`$ be three ordinary atomic annihilation operators. The effective
Hamiltonian, in rotating frames at their carrier frequencies, is

```math
\frac{H_{\mathrm{eff}}}{\hbar}
=J a^\dagger b+G_a a^\dagger c^\dagger
 +G_b b^\dagger c^\dagger+\mathrm{h.c.}
```

Each mode couples to a separate atomic continuum with the same linewidth
$`\kappa`$. The source controls the incoming field of $`a`$, the receiver
collects the outgoing field of $`b`$, and $`c`$ is an inaccessible idler.
The source may collect the outgoing field of $`a`$ with the efficiency
specified in [Collection boundary](collection_boundary.md). The other
incoming signal and the idler are vacuum in the central model.

At rotating-frame frequency $`\omega`$, the closed Nambu vector is
$`v=(a[\omega],b[\omega],c^\dagger[-\omega])^T`$. Its metric is
$`\mathcal J=\operatorname{diag}(1,1,-1)`$. The last minus sign is the
commutator of a creation operator. The laboratory idler has positive atom
number and need not have negative laboratory energy. The conjugate block at
$`-\omega`$ completes the physical six-dimensional canonical evolution.

The number-conserving continuum coupling before the Markov approximation is

```math
\frac{H_{\mathrm{port}}}{\hbar}
=\sum_{j=a,b,c}\int d\nu\,\nu\,r_{j\nu}^\dagger r_{j\nu}
 +\sum_{j=a,b,c}\int d\nu\,
 \sqrt{\frac{\kappa}{2\pi}}
 \left(d_j^\dagger r_{j\nu}+r_{j\nu}^\dagger d_j\right).
```

Here frequencies are detunings from the carrier of each port. A flat
coupling over the working band gives
$`\dot v=(-iK-\kappa I/2)v+\sqrt\kappa\,v_{\mathrm{in}}`$ and
$`v_{\mathrm{out}}=v_{\mathrm{in}}-\sqrt\kappa\,v`$.

## 2. An exact stable family with unity forward power

For a desired resonant reverse power $`0\le R\le1`$, put

```math
\beta=\sqrt R,\qquad d=1-\beta,\qquad r=\sqrt{2d},\qquad
p=\frac{2-r}{2+r},\qquad u=\frac{r}{2+r}.
```

Choose

```math
J=\frac{i\kappa p}{2},\qquad
G_a=\frac{i\kappa u}{2},\qquad
G_b=-\frac{i\kappa u}{2}.
```

The equations of motion give

```math
K=\frac{i\kappa}{2}
\begin{pmatrix}
0&p&u\\
-p&0&-u\\
u&-u&0
\end{pmatrix},\qquad
K^\dagger\mathcal J=\mathcal J K,
```

and the complete three-channel scattering matrix is

```math
S(\omega)=I-\kappa
\left(\frac\kappa2I+iK-i\omega I\right)^{-1}.
```

At resonance this becomes

```math
\boxed{
S(0)=-
\begin{pmatrix}
r&\beta&d\\
-1&r&-r\\
r&-d&1+d
\end{pmatrix}.}
```

The matrix obeys $`S(\omega)\mathcal J S(\omega)^\dagger=\mathcal J`$
at every real frequency. Its top-left block has
$`G=|S_{21}(0)|^2=1`$ and $`|S_{12}(0)|^2=R`$.
The overall minus sign is an output phase and has no effect on these powers
or on the communication statements.

The drift eigenvalues are

```math
-\frac\kappa2,\qquad
-\frac\kappa2\pm\frac\kappa2\sqrt{2u^2-p^2}.
```

Since $`0\le u\le\sqrt2-1`$ and $`p=1-2u`$, every eigenvalue has real
part at most

```math
-\gamma_*=-\frac\kappa2
\left[1-\sqrt{8\sqrt2-11}\right]
\simeq-0.2199515671\,\kappa.
```

The conjugate block has the same stability margin. Perfect reverse isolation
at $`R=0`$ is therefore reached without approaching a parametric instability
in this effective model. The couplings also remain bounded: $`|J|\le\kappa/2`$
and $`|G_a|=|G_b|\le(\sqrt2-1)\kappa/2`$.

### Resonant occupations and the collection threshold

With all incoming modes in vacuum, the positive output occupations are

```math
n_1=d^2,\qquad N=2d,\qquad n_1+N=d(d+2).
```

This is the minimum summed **positive-output** occupation from
[Scattering and noise](scattering_noise.md). The idler output has occupation
$`d(d+2)`$ as well, so the sum over all three physical atomic outputs is
$`2d(d+2)`$. At $`R=0`$ the occupations are $`(1,2,3)`$; their sum is
$`6`$. These are spectral occupations, not an atom flux.

For $`0\le R\le1/4`$, the reduced forward channel is entanglement breaking,
because $`N\ge G`$. In the same range the exact threshold for the collected
return is

```math
\eta\le\eta_c(R)
=\frac{1-2\sqrt R}{(1-\sqrt R)^2}.
```

The equality side is the zero-capacity side. For any $`R>0`$ ideal collection
lies outside that region. The achievable protocol and the meaning of its
rate are treated in [Communication rates](communication_rates.md).

## 3. A number-conserving collision model in a ring

Take a tightly confined quasi-one-dimensional ring of circumference $`L`$,
with $`\theta=2\pi x/L`$, atomic mass $`M`$, and field

```math
\Psi(x)=\frac1{\sqrt L}\sum_{m\in\mathbb Z}d_m e^{im\theta},\qquad
\epsilon_m=\hbar\omega_L m^2,\qquad
\omega_L=\frac{\hbar}{2M}\left(\frac{2\pi}{L}\right)^2.
```

The microscopic Hamiltonian is

```math
H=\int_0^L dx\,
\Psi^\dagger\left[-\frac{\hbar^2\partial_x^2}{2M}+V(x,t)\right]\Psi
+\frac12\int_0^L dx\,g(x,t)\Psi^{\dagger2}\Psi^2.
```

Both terms commute with the total atomic number. The applied fields supply
energy and angular momentum, while each pair-production event transfers two
atoms out of a condensate mode. Let the pump be $`p_0=d_0`$ with occupation
$`N_0`$ and density $`n_0=N_0/L`$. The explicit free-mode selection below
takes $`g_0=0`$; weak static interactions can be included as described later.
Choose

| Role | Ring mode | Free carrier frequency |
|---|---:|---:|
| Source mode $`a`$ | $`d_1`$ | $`\omega_L`$ |
| Idler mode $`c`$ | $`d_2`$ | $`4\omega_L`$ |
| Receiver mode $`b`$ | $`d_3`$ | $`9\omega_L`$ |

Apply two traveling interaction gratings,

```math
g(\theta,t)=g_0
+g_a e^{i(3\theta-5\omega_Lt)}
+g_b e^{i(5\theta-13\omega_Lt)}+\mathrm{c.c.},
```

and a Bragg conversion potential

```math
V_J(\theta,t)=\hbar J e^{-i(2\theta-8\omega_Lt)}+\mathrm{c.c.}
```

The amplitudes $`g_a,g_b`$ have units of energy times length and have
independently set phases. The reality of $`g`$ fixes each opposite Fourier
component to its complex conjugate; it does not equate the phases of the two
different gratings.

For the convention $`g(\theta,t)=\sum_Q g_Q(t)e^{iQ\theta}`$, the exact
contact term is

```math
H_{\mathrm{int}}
=\frac1{2L}\sum_{m,n,p,q}
g_{m+n-p-q}(t)d_m^\dagger d_n^\dagger d_p d_q.
```

Its desired resonant terms are

```math
H_{\mathrm{pair}}
=\frac{g_a}{L}e^{-5i\omega_Lt}a^\dagger c^\dagger p_0^2
+\frac{g_b}{L}e^{-13i\omega_Lt}b^\dagger c^\dagger p_0^2
+\mathrm{h.c.}
```

The factor $`1/2`$ is cancelled by the two orderings of the distinct created
modes. Each term explicitly conserves atom number. In frames rotating at the
free carriers, replacing
$`p_0\to\sqrt{N_0}e^{i\theta_0}`$ gives the effective couplings

```math
G_a=\frac{n_0g_a}{\hbar}e^{2i\theta_0},\qquad
G_b=\frac{n_0g_b}{\hbar}e^{2i\theta_0}.
```

The stated Fourier component of $`V_J`$ supplies $`J a^\dagger b`$.
Consequently the invariant loop phase is

```math
\Phi=\arg(JG_a^*G_b).
```

The common condensate phase cancels from $`\Phi`$. The three externally
controlled drive phases set it independently; the stable family uses
$`\Phi=-\pi/2`$ when its pairing links are nonzero. The frequency and angular
momentum closure relations are
$`13-5=8`$ and $`5-3=2`$. They permit a stationary effective loop with a
fixed physical phase.

Spatial and temporal optical control of atomic interactions has been
demonstrated by [Yamazaki et al. (2010)](https://doi.org/10.1103/PhysRevLett.105.050405)
and [Clark et al. (2015)](https://doi.org/10.1103/PhysRevLett.115.155301).
Interaction modulation producing correlated atomic pairs is supported by
the driven-gas experiment of
[Clark et al. (2017)](https://doi.org/10.1038/nature24272) and the microscopic
theory of [Chih and Holland (2020)](https://doi.org/10.1088/1367-2630/ab7140).
Independently controlled Bragg amplitudes, phases and detunings are established
in atomic momentum lattices by
[An, Meier and Gadway (2017)](https://doi.org/10.1038/s41467-017-00387-w).
These works support the control primitives. They do not demonstrate the
combined three-port ring proposed here.

## 4. Resonance selection and terms that remain to be controlled

For a grating with angular momentum $`Q`$ and positive frequency $`\Omega`$,
creation of two atoms out of $`d_0`$ is resonant only if

```math
m+n=Q,\qquad (m^2+n^2)\omega_L=\Omega.
```

The two equations have just the unordered solutions $`\{1,2\}`$ for
$`(Q,\Omega/\omega_L)=(3,5)`$, and $`\{2,3\}`$ for $`(5,13)`$.
The same interaction gratings also produce normal Bogoliubov terms. Their
resonance condition is $`2Qm+Q^2=\Omega/\omega_L`$; it would require
$`m=-2/3`$ or $`m=-6/5`$, so neither is a ring mode. The Bragg condition
$`(m+2)^2-m^2=8`$ selects $`m=1`$ uniquely.

| Drive | Intended process | Nearest other pair detuning | Nearest unwanted normal detuning |
|---|---|---:|---:|
| $`(Q,\Omega/\omega_L)=(3,5)`$ | $`0+0\leftrightarrow1+2`$ | $`4\omega_L`$ | $`2\omega_L`$ |
| $`(5,13)`$ | $`0+0\leftrightarrow2+3`$ | $`4\omega_L`$ | $`2\omega_L`$ |
| $`(2,8)`$ | $`1\leftrightarrow3`$ | No direct pairing from this one-body term | $`4\omega_L`$ |

This proves first-order selection, including the otherwise dangerous normal
terms. It does not remove the following effects.

**Coherent pump response.** The gratings force pump components $`d_3,d_5`$
with detunings $`4\omega_L,12\omega_L`$. The Bragg tone forces $`d_2`$
with detuning magnitude $`4\omega_L`$. Their oppositely traveling conjugate
components are also off resonance. One may solve for the weak periodic
Gross–Pitaevskii pump and linearize about that solution. Alternatively, an
additional number-conserving potential

```math
V_{\mathrm{comp}}(\theta,t)=-n_0[g(\theta,t)-g_0]
```

cancels the interaction-induced mean-field force on a uniform pump. It
leaves the pair terms intact and changes the normal coefficient from
$`2n_0\delta g`$ to $`n_0\delta g`$, whose resonances remain absent.
The Bragg-induced pump response must still be included. Its relative
amplitude is of order $`|J|/(4\omega_L)`$ in this weak-drive limit.

**Static interactions and virtual shifts.** A nonzero $`g_0`$ changes the
particle carriers to Bogoliubov frequencies

```math
\omega_m=\frac1\hbar
\sqrt{\epsilon_m(\epsilon_m+2g_0n_0)}.
```

The drive frequencies must then be calibrated to
$`\Omega_a=\omega_a+\omega_c`$,
$`\Omega_b=\omega_b+\omega_c`$ and
$`\Omega_J=\omega_b-\omega_a`$. The Bogoliubov overlaps change the coupling
strengths as well. Small shifts compared with the unwanted-mode gaps
preserve resonance isolation. Off-resonant terms also produce virtual
frequency shifts of order coupling squared divided by detuning; those shifts
belong in the calibration. With appreciable static interactions, the port
couplings must also be transformed to the Bogoliubov basis and all open
branches retained. A bare atomic outcoupling term is not automatically a
single quasiparticle port.

**Higher Floquet processes.** Integer quadratic energies and commensurate
drives allow higher-order paths that the table does not exclude. A controlled
three-mode description needs

```math
\kappa,\ |J|,\ |G_a|,\ |G_b|,
\ |g_0|n_0/\hbar\ll\Delta_{\mathrm{sel}},
```

small pump depletion, and transverse confinement above the relevant carrier
and drive energies. Here the first-order selection gap is
$`\Delta_{\mathrm{sel}}=2\omega_L`$. This is a controlled finite-time
effective reduction, not a proof of global stability of an infinite driven
ring. Extra open sidebands and optical loss contribute additional physical
channels; they must be included when applying the canonical inequalities.

The selection gap can also be increased by using modes $`K,2K,3K`$. The
drive pairs become $`(3K,5K^2)`$, $`(5K,13K^2)`$ and $`(2K,8K^2)`$.
Multiples of $`3`$ or $`5`$ can introduce resonant normal terms and must not
be chosen blindly. For $`K=11`$, the nearest other pair gap is
$`20\omega_L`$, the unwanted normal gaps of both pair gratings are
$`22\omega_L`$, and the other Bragg transitions are detuned by at least
$`44\omega_L`$. Higher angular resolution, carrier frequencies and
transverse confinement are then required.

## 5. Port selectivity and number/phase references

A number-conserving Raman outcoupler has the form

```math
H_R=\sum_j\int dx\,
\hbar\Omega_j(x)e^{-i\omega_jt}
\Psi_{\mathrm{guide},j}^\dagger(x)\Psi_{\mathrm{ring}}(x)
+\mathrm{h.c.}
```

Its spatial overlap selects angular momentum and its drive frequency
selects the carrier. Separate internal states or guides distinguish the
three continua. Frequency selection alone is insufficient for an unfiltered
continuum: a different ring mode can emit at a different continuum energy.
An explicit way to supply the required selectivity is an atomic resonant
filter before each outgoing guide.

For example, give filter $`j`$ an auxiliary internal-state ring manifold
$`f_{j,\ell}`$ with the same free angular curvature. A Raman profile
$`e^{-im_j\theta}`$ couples $`d_m`$ to $`f_{j,m-m_j}`$. Tune its frequency
so that $`d_{m_j}\leftrightarrow f_{j,0}`$ is resonant. Every other mode has
detuning

```math
\Delta_{j,m}
=\omega_L[(m-m_j)^2-m^2+m_j^2]
=-2m_j(m-m_j)\omega_L.
```

Thus the target is unique, with an unwanted-mode gap of at least
$`2|m_j|\omega_L`$. Let $`f_{j,0}`$ have guide linewidth $`W_j`$ and
Raman coupling $`\lambda_j`$. Eliminating this resonant filter in
$`\kappa_j\ll W_j\ll\Delta_{\mathrm{port}}`$ gives

```math
\kappa_j=\frac{4|\lambda_j|^2}{W_j}.
```

This is a finite-band route to the assumed atomic port. The filter gives
memory corrections of order $`\kappa_j/W_j`$ across the device band. If
other filter angular modes are also broadened, off-target coupling powers
are suppressed by $`O(W_j^2/\Delta_{j,m}^2)`$ relative to the resonant
port. They are still additional positive channels, not identically zero.
Off-resonant pump extraction, if present, must also enter the atom budget.
Both filter and guide couplings conserve atom number before the reservoirs
are traced out.

Coherent momentum-resolved Raman extraction of atoms from a
condensate was demonstrated by
[Hagley et al. (1999)](https://doi.org/10.1126/science.283.5408.1706).
Engineering three independently selective, approximately flat continua is an
additional requirement of this architecture. A real outcoupler must be
characterized for unwanted channels; selecting a two-by-two submatrix of a
larger device does not establish a two-positive-port model.

The atomic Hamiltonian can also be expanded with number-conserving
fluctuations $`\Lambda_m=p_0^\dagger d_m/\sqrt{N_0}`$. Their exact
commutator is

```math
[\Lambda_m,\Lambda_n^\dagger]
=\delta_{mn}\frac{p_0^\dagger p_0}{N_0}
 -\frac{d_n^\dagger d_m}{N_0}.
```

It becomes canonical only in the small-depletion limit. This is the
controlled number-conserving Bogoliubov logic developed by
[Gardiner (1997)](https://doi.org/10.1103/PhysRevA.56.1414) and
[Castin and Dum (1998)](https://doi.org/10.1103/PhysRevA.57.3008).

Quadrature preparation, heterodyne measurement and atomic displacement also
need a condensate/local-oscillator reference, or an explicit relational
encoding that keeps the reference. An exact fixed-number pump traced out at
finite occupation does not by itself give the absolute-phase Gaussian
channel assumed in those protocols. The classical-pump treatment means a
large phase-referenced reservoir with negligible depletion and sufficiently
small fluctuations over the operation. The local references do not provide
shared entanglement, but their atoms and coherence are resources.

## 6. Spectral noise, atom flux, and pump cost

The stable model permits a complete vacuum-emission budget, rather than an
estimate from the resonance alone. Let
$`D=-iK-\kappa I/2`$ and $`Q=\langle vv^\dagger\rangle`$. The stationary
vacuum covariance solves

```math
DQ+QD^\dagger+\kappa\operatorname{diag}(1,1,0)=0.
```

The intracavity physical occupations are
$`(n_a,n_b,n_c)=(Q_{11}-1,Q_{22}-1,Q_{33})`$. The conserved difference
between signal and idler numbers gives $`n_a+n_b=n_c`$. Solving the
Lyapunov equation gives

```math
n_c=\frac{r^2(3r^2+16)}{4(3r^2+12r+20)},\qquad
\Gamma_{\mathrm{atoms}}=\kappa(n_a+n_b+n_c)=2\kappa n_c.
```

The rational function is increasing for $`0\le r\le\sqrt2`$, as follows
by differentiating its positive-coefficient numerator after combining terms.
Therefore

```math
0\le\Gamma_{\mathrm{atoms}}
\le\frac{11}{13+6\sqrt2}\,\kappa
\simeq0.5119784009\,\kappa.
```

Equivalently, this flux is the sum of the three output spectra integrated
with $`d\omega/(2\pi)`$ in the effective wide-band Markov model. A physical
reservoir needs a flat working window $`W\gg\kappa`$ that still lies within
the carrier and resonance-selection regime. Since anomalous amplitudes fall
as $`\kappa^2/\omega^2`$ at large detuning, truncating the ideal-model
vacuum integral outside such a window changes it by
$`O(\kappa^4/W^3)`$; other microscopic emission processes need a separate
budget. In the particle limit every atom emitted through the three modeled ports
comes from the condensate in vacuum operation. Over a working interval
$`T`$, an undepleted pump requires at least
$`\Gamma_{\mathrm{atoms}}T\ll N_0`$, in addition to any input-induced
depletion, preparation cost and loss. At nonzero static interactions,
quasiparticle occupation and physical atom number have additional
Bogoliubov-overlap factors.

The finite-energy protocol in [Communication rates](communication_rates.md)
uses conditional centering. With a two-mode squeezed probe of mean signal
occupation $`n`$, define

```math
D_n=2dn+d^2+1.
```

After heterodyne of the complete return, the source and receiver subtract
their respective conditional means. Up to local phases, the residual
reference/receiver moments are

```math
n_A=\frac{nR}{D_n},\qquad
n_B+1=\frac{(n+1)(1+d)^2}{D_n},\qquad
m_{AB}=-\frac{\sqrt{n(n+1)}\sqrt R(1+d)}{D_n}.
```

At $`n=1`$ one has $`D_1=(1+d)^2`$ and $`n_B=1`$ exactly. The classical
conditional-mean gains remain bounded as $`R\to0`$; there is no intermediate
amplification to a divergent occupation in this implementation. The raw
positive output occupations before measurement are also bounded:
$`2dn+d^2`$ at the source and $`n+2d`$ at the receiver. An alternative
feedforward rule that cancels an input operator has corrected-channel power
gain proportional to $`1/R`$ and a different resource budget; that divergence is not a necessary
cost of the conditional-centering protocol.

Bounded signal occupation and a finite integrated spontaneous flux still do
not imply a bounded total cost as $`R\to0`$. Pump/reference quality,
collection loss, detector noise, unwanted-mode coupling, bandwidth and
operating time must resolve the relevant entanglement margin.

For fixed $`R>0`$ the effective theory has an open neighborhood of sufficiently
accurate microscopic implementations. Claims about the limit $`R\to0`$
require an explicit joint limit: fixed finite-pump and rotating-wave errors
cannot be ignored as the non-positive-partial-transpose margin shrinks.
A conservative sufficient design hierarchy is that the induced scattering
and covariance errors be much smaller than that margin; an asserted
$`O(R)`$ advantage requires errors controlled below its stated order.
[Finite bandwidth](finite_bandwidth.md) gives the corresponding packet
accounting and the distinction between a resonant point and a band.

## Verification and scope

The finite checks enumerate the intended and unwanted first-order
resonances, verify canonical scattering and uniform drift stability, compare
the analytic atom-flux formula with the Lyapunov solution, and retain the
extra temporal modes in packet calculations. They do not replace a
multimode finite-pump Floquet calculation, a measured loss budget, or a
laboratory demonstration. See [Verification](../verification/README.md)
and the source inventory in [Related work](../references/RELATED_WORK.md).

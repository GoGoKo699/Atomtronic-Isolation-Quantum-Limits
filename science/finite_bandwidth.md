# From spectral channels to finite wave packets

A scattering matrix at one frequency describes a monochromatic component.
An actual atom pulse is a normalized wave packet. Two different statements
connect the [spectral model](model.md) to such pulses: a separable channel at
almost every frequency in an accessible band remains unable to distribute
entanglement across that band, while a strict entanglement witness at a
continuous frequency survives for a sufficiently narrow finite packet.
Neither statement turns an isolated cancellation point into a broadband
claim.

## 1. A whole-band zero-capacity statement

Suppose the stationary channel decomposes by frequency into the complete
two-positive-port form

```math
\boldsymbol b(\omega)
=A(\omega)\boldsymbol a(\omega)
 +B(\omega)\boldsymbol e^\dagger(-\omega),\qquad
A(\omega)A(\omega)^\dagger-B(\omega)B(\omega)^\dagger=I_2.
```

The auxiliary signal and idler inputs are independent vacuum, the idlers are
inaccessible, and source collection has transmissivity $`\eta(\omega)`$.
For each frequency define $`G,R,N`$ as in [Model](model.md), and
$`c(\omega)=N(\omega)-G(\omega)`$.

If, almost everywhere in the accessible band $`\mathcal B`$,

```math
c(\omega)\ge0,\qquad
[1-\eta(\omega)]c(\omega)\ge\eta(\omega)R(\omega),
```

then the [collection-boundary theorem](collection_boundary.md) supplies a
sender-local instrument followed by receiver-state preparation at each
frequency. Products of these maps are still local operations with classical
communication across the sender/receiver cut. They cannot distribute
entanglement even when the sender entangles different input frequencies,
retains a reference, or adapts later uses to earlier classical results.
Fourier mixing, pulse shaping and mode recombination performed locally by
each party do not change that conclusion.

The continuum statement can be defined using finite frequency-bin
regularizations followed by their physical finite-energy limit. It does not
assume that an arbitrary pair of selected temporal modes forms a closed
two-by-two scattering matrix. Under the untrusted-environment assumption of
the main theorem, the corresponding secret-key statement follows as well.
Memory or pump fluctuations coupling different frequencies are outside this
product-channel premise and require their own channel model.

For the [stable family](stable_atomic_model.md), $`R(0)=0`$ at the endpoint
and $`c(0)=1`$. Any fixed collection efficiency $`\eta<1`$ gives a strict
inequality there, so continuity yields a nonzero surrounding band in the
zero-capacity region. With ideal collection $`\eta=1`$, the resonant
equality alone supplies no such band: reverse transmission is nonzero at
neighboring frequencies.

## 2. Exact accounting for selected packet modes

Use continuum normalization
$`[a_j(\omega),a_k^\dagger(\omega')]=2\pi\delta_{jk}\delta(\omega-\omega')`$.
Let $`f`$ obey

```math
\int\frac{d\omega}{2\pi}|f(\omega)|^2=1,\qquad
a_{j,f}=\int\frac{d\omega}{2\pi}f(\omega)^*a_j(\omega).
```

Select output profiles $`g_i(\omega)=e^{i\tau_i\omega}f(\omega)`$, allowing
a separately calibrated delay at each physical output. Write
$`P(\omega)=\mathrm{diag}(e^{-i\tau_1\omega},e^{-i\tau_2\omega})`$,
$`\widetilde A=P A`$, $`\widetilde B=P B`$, and
$`\langle X\rangle_f=\int |f|^2X\,d\omega/(2\pi)`$.

The exact two-output packet channel is

```math
\boldsymbol b_g=A_f\boldsymbol a_f
 +C_f\boldsymbol h_+ +B_f\boldsymbol h_-^\dagger,
```

with Gram matrices

```math
\begin{aligned}
A_f&=\langle\widetilde A\rangle_f,\\
C_fC_f^\dagger
&=\langle\widetilde A\widetilde A^\dagger\rangle_f-A_fA_f^\dagger,\\
B_fB_f^\dagger
&=\langle\widetilde B\widetilde B^\dagger\rangle_f.
\end{aligned}
```

The modes $`\boldsymbol h_+`$ are positive-signature input wave packets
orthogonal to the selected $`f`$ modes. The modes $`\boldsymbol h_-`$ are
idler wave packets. For this single-packet channel, all unselected positive
temporal input modes and all idler inputs are assumed to be vacuum. Then the
$`\boldsymbol h_\pm`$ can be chosen as independent canonical vacuum modes,
and the displayed Gram matrices determine their relevant noise correlations.
Arbitrary encodings across occupied packets instead require the joint
multimode channel; the preceding whole-band converse already permits such
encodings. Matrix variance is positive, and the exact packet commutator is

```math
A_fA_f^\dagger+C_fC_f^\dagger-B_fB_f^\dagger=I_2.
```

Thus even a complete two-positive-port spectral channel generally acquires
positive auxiliary **temporal** modes after projection onto one pulse per
port. This is modal mismatch, not necessarily physical dissipation.

Define packet quantities

```math
G_f=|(A_f)_{21}|^2,\quad R_f=|(A_f)_{12}|^2,\quad
\ell_{1f}=(C_fC_f^\dagger)_{11},\quad
N_f=(B_fB_f^\dagger)_{22},\quad t_f=R_f+\ell_{1f}.
```

The exact auxiliary-port inequality in
[Scattering and noise](scattering_noise.md) gives

```math
N_f\ge G_f-t_f.
```

An informative equivalent expression is

```math
\boxed{
t_f=\left\langle|A_{12}|^2\right\rangle_f
+\left\langle|A_{11}|^2\right\rangle_f
-\left|\left\langle e^{-i\tau_1\omega}A_{11}\right\rangle_f\right|^2.}
```

The first term is spectrally integrated reverse power in the packet. The
remaining terms are the variance of the delayed source-reflection
amplitude. Averaging reverse amplitudes can make $`R_f`$ small through phase
cancellation; $`t_f`$ retains the associated positive auxiliary channels.
It is therefore the quantity to use in the reduced-channel bounds.

In particular, $`t_f\le1/2`$ gives zero unassisted reduced quantum capacity.
In the domain $`0\le t_f\le\min(G_f,1)`$, the established upper bound
$`F(G_f,t_f)`$ from [Communication rates](communication_rates.md) applies to
the reduced packet channel. The scalar two-positive-port collection
threshold should not simply be reused with $`R_f`$: the new correlation
matrix $`C_fC_f^\dagger`$ must be retained in the full-channel test.

## 3. A finite packet around the stable cancellation point

For the stable family write $`\beta=\sqrt{R_0}`$ for the reverse power
parameter at the carrier, $`r=\sqrt{2(1-\beta)}`$, and keep the linewidth
$`\kappa`$ explicit. Differentiating the resolvent gives

```math
S'(0)=-\frac{i}{\kappa}[I-S(0)]^2.
```

For $`R_0<1`$, output delays

```math
\tau_1=\frac{3-\beta+3r/2}{\kappa},\qquad
\tau_2=\frac{4-2\beta+2r}{\kappa}
```

remove the first-order frequency variation of the source reflection and the
forward signal, respectively. At $`R_0=0`$ one has

```math
A_{12}(0)=0,\qquad A_{12}'(0)=\frac{i}{\kappa},\qquad
A_{11}'(0)=-\frac{3i(1+\sqrt2)}{\kappa},\qquad
A_{21}'(0)=\frac{i(4+2\sqrt2)}{\kappa}.
```

Take a symmetric packet centered on zero, of spectral variance $`\sigma^2`$
and fourth moment of order $`\sigma^4`$. Then

```math
G_f=1+O\!\left(\frac{\sigma^2}{\kappa^2}\right),\qquad
t_f=\frac{\sigma^2}{\kappa^2}
 +O\!\left(\frac{\sigma^4}{\kappa^4}\right).
```

The reverse packet amplitude starts at second order, so
$`R_f=O(\sigma^4/\kappa^4)`$, while its integrated reverse spectral power
starts at $`\sigma^2/\kappa^2`$. The missing contribution appears in
$`\ell_{1f}`$. The group-delay correction is relevant: without it the
source-reflection variance generally also starts at second order.

For example, Gaussian integration at $`\sigma/\kappa=0.002`$ gives

| Quantity | Value |
|---|---:|
| Forward packet power $`G_f`$ | $`0.9998987661`$ |
| Reverse packet power $`R_f`$ | $`1.1717835\times10^{-10}`$ |
| Reverse spectral power $`\langle\lvert A_{12}\rvert^2\rangle_f`$ | $`3.9987375\times10^{-6}`$ |
| Source positive auxiliary coupling $`\ell_{1f}`$ | $`4.0004664\times10^{-6}`$ |
| Corrected reverse resource $`t_f`$ | $`4.0005836\times10^{-6}`$ |

The reduced-channel capacity envelope is consequently of order
$`\sigma^4/\kappa^4`$, using
$`F(G_f,t_f)=t_f^2/(2G_f\ln2)+O(t_f^3)`$. This is an upper bound, not an
attained rate. It also concerns the reduced interface that discards the
source return.

For fixed $`R_0>0`$, continuity instead gives
$`t_f=R_0+O(\sigma^2/\kappa^2)`$. A sufficient narrowing hierarchy for
resolving the small-$`R_0`$ behavior is
$`\sigma/\kappa\ll\sqrt{R_0}`$, along with control of the microscopic
and collection errors described below.

## 4. Finite-energy entanglement survives a sufficiently narrow band

Fix a carrier outside the zero-capacity region and a two-mode squeezed probe
with finite nonzero mean signal occupation. Keep its reference at the
source. Include the physical source-collection loss, perform heterodyne on
the collected return, and subtract the conditional local means as in
[Communication rates](communication_rates.md). The conditional covariance
is independent of the heterodyne outcome.

At the carrier let the partially transposed covariance violate the
uncertainty relation strictly: the smallest eigenvalue of
$`V^{\mathrm{PT}}+i\Omega/2`$ is $`-\delta<0`$. If the scattering and
collection coefficients are continuous there, the packet covariance and its
conditional Schur complement converge to their carrier values as the
packet narrows. The heterodyne covariance is nonsingular because it includes
vacuum measurement noise. For a packet narrow enough that its covariance
perturbation has operator norm below $`\delta`$, the negative eigenvalue
persists. This proves an entangled normalizable pulse with finite probe
energy and a finite characteristic duration; no infinite-squeezing Choi
state is required for this implication.

For the stable unity-forward family, ideal collection and a probe of mean
occupation one give, after conditional centering,

```math
x=\frac{R_0}{(2-\sqrt{R_0})^2},\qquad
n_A=x,\qquad n_B=1,\qquad |m_{AB}|^2=2x.
```

The smaller partially transposed symplectic eigenvalue is

```math
\widetilde\nu_-
=\frac{x+2-\sqrt{x^2+6x+1}}2
=\frac12-x+O(x^2).
```

It is below $`1/2`$ for every $`R_0>0`$. The receiver occupation stays
bounded; the margin nevertheless shrinks as $`R_0/4`$. This explains why
finite bandwidth and fixed implementation errors cannot be held unchanged
while claiming the asymptotic ideal rate all the way to $`R_0=0`$.

The complete packet calculation also gives a concrete finite-band witness.
For a Gaussian profile with $`R_0=0.01`$, $`\sigma/\kappa=0.01`$ and probe
occupation one, conditional centering gives

| Quantity | Finite-packet value |
|---|---:|
| Source reference occupation | $`0.00279923185`$ |
| Receiver occupation | $`0.9987659821`$ |
| Smallest partially transposed symplectic eigenvalue | $`0.4972357130`$ |
| Largest quadrature conditional-mean coefficient | $`0.7054680394`$ |

The symplectic eigenvalue is below the vacuum threshold $`1/2`$. All
positive temporal auxiliary modes are retained in this calculation. The
Gaussian has an rms bandwidth rather than compact frequency support. It
can be truncated and renormalized inside a sufficiently wide valid working
window: the discarded Gaussian weight and covariance change can be made
smaller than the strict witness margin. A hard finite time window introduces
the corresponding small spectral correction, which must be included rather
than assumed absent.

### An independent packet check with raw cancellation feedforward

A useful check, separate from the bounded-output protocol, is to set
$`k=-(A_f)_{22}/(A_f)_{12}`$ and use heterodyne feedforward to cancel the
selected second input. The resulting single-mode channel has

```math
G_{\mathrm{rec}}=|(k,1)A_f(1,0)^T|^2,\qquad
N_{\mathrm{rec}}=(k,1)B_fB_f^\dagger(k,1)^\dagger+|k|^2.
```

The heterodyne vacuum accounts for $`|k|^2`$. The packet commutator gives
the exact identity

```math
N_{\mathrm{rec}}-G_{\mathrm{rec}}
=(k,1)C_fC_f^\dagger(k,1)^\dagger-1.
```

This channel is non-entanglement-breaking precisely when the positive
temporal-mode residual on the right, before subtracting one, is below one.
For the Gaussian packet with $`R_0=0.01`$ and $`\sigma/\kappa=0.01`$, the
residual is $`0.00826508`$, well below one. The recovered gain is about
$`359.3583`$. These numbers verify finite-packet survival and explicit
auxiliary-mode accounting; that large amplifier gain is not a necessary
resource of the bounded-output conditional-centering protocol above.

## 5. Order of limits and rates per time

There are distinct resources: packet duration, source collection, pump
depletion and fluctuations, uncollected positive channels, thermal noise,
mode-selective detection, and local phase references. At any fixed
$`R_0>0`$, sufficiently small errors preserve a strict witness. A claim as
$`R_0\to0`$ requires those errors to shrink relative to the calculated
margin. The effective model does not establish such a joint limit for a
fixed finite atom reservoir.

The bandwidth hierarchy $`\sigma/\kappa\ll\sqrt{R_0}`$ is sufficient for
the perturbative packet statements given here. It is not an optimized
bandwidth bound or a universal time-resource lower bound. Microscopic
Floquet sidebands or frequency-dependent collection can require a stricter
condition. The relevant test is the complete covariance or channel, not
only the averaged reverse amplitude.

The rates in [Communication rates](communication_rates.md) are per
independent use. Converting them to ebits or secret bits per second requires
a normalized set of usable orthogonal temporal modes and its production
rate. Closely overlapping pulses are not automatically independent uses.
The frequency-integrated atom flux in
[Stable atomic model](stable_atomic_model.md) is a separate quantity from
either the occupation of one normalized packet or the communication rate.

The finite checks in
[check_atomic_model.py](../verification/check_atomic_model.py) evaluate the
packet Gram matrices directly and verify the canonical relation, positive
auxiliary covariance, noise floor, conditional covariance and recovery
identity. See [Verification](../verification/README.md).

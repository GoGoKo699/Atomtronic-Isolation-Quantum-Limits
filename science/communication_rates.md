# Communication rates near reverse isolation

The reflected output changes the rate law as well as the exact zero-capacity
boundary. With that output discarded, the two-positive-port canonical
constraint gives a quadratic upper bound in reverse power. With ideal access
to the reflection, a stable unity-forward-gain family has a two-way quantum
capacity bounded above and below by positive constants times reverse power.
The lower bound needs a signal probe of mean occupation one.

The [model](model.md) fixes the parties, inaccessible modes and covariance
convention. The [collection theorem](collection_boundary.md) establishes
positivity and impossibility for arbitrary collection efficiencies. This
page quantifies rates. All rates are per independent normalized mode;
[finite bandwidth](finite_bandwidth.md) is a separate resource question.

## 1. The reduced forward channel

Tracing the reflection leaves a one-mode phase-insensitive Gaussian channel

```math
V\longmapsto GV+\left[N+\frac{1-G}{2}\right]I_2.
```

Here $`N`$ is its vacuum-output occupation. Complete positivity requires
$`N\ge\max(0,G-1)`$. The channel is entanglement breaking exactly when
$`N\ge G`$ [Holevo 2008](https://doi.org/10.1134/S0032946008030010).
This condition concerns the reduced channel only.

When $`N<G`$, set

```math
\tau=G-N,\qquad g=G/\tau.
```

The channel is a quantum-limited amplifier of gain $`g`$ followed by pure
loss of transmissivity $`\tau`$:

```math
\Phi=\mathcal L_\tau\circ\mathcal A_g,
\qquad 0<\tau\le\min(G,1).
```

Indeed the concatenation has forward gain $`\tau g=G`$ and vacuum-output
occupation $`\tau(g-1)=G-\tau=N`$. This amplifier-then-loss decomposition
is established Gaussian-channel machinery
[Noh, Albert and Jiang 2019](https://doi.org/10.1109/TIT.2018.2873764).
The [canonical scattering inequality](scattering_noise.md) implies

```math
\tau=G-N\le R.
```

Pure loss with transmissivity at most one half is antidegradable
[Wolf, Pérez-García and Giedke 2007](https://doi.org/10.1103/PhysRevLett.98.130501). Its
complement can reconstruct its output, and preceding it by an amplifier does
not remove that property: the full complementary output contains the loss
environment. Therefore

```math
R\le\tfrac12\quad\Longrightarrow\quad Q(\Phi)=0.
```

For $`0\le R<1`$, data processing also gives

```math
Q(\Phi)\le\left[\log_2\frac{R}{1-R}\right]_+.
```

The right-hand side at $`R=0`$ is defined as zero by continuity.
The conclusion includes the entanglement-breaking case, where all the
capacities under discussion vanish. It does not rule out two-way-assisted
communication outside the entanglement-breaking region.

### A quadratic upper bound on assisted rates

For $`G>0`$ and $`0\le R\le\min(G,1)`$, the canonical inequality gives
$`N\ge G-R`$.
Adding independent Gaussian displacement noise at the receiver is a local
channel. The established relative-entropy bounds of
[Pirandola, Laurenza, Ottaviani and Banchi](https://doi.org/10.1038/ncomms15043),
Eqs. (23), (26), and (29), therefore imply

```math
Q_2(\Phi)\le K(\Phi)\le F(G,R),
```

where

```math
F(G,R)=
\begin{cases}
\displaystyle
\frac{(G-R)\log_2(1-R/G)-(1-R)\log_2(1-R)}{1-G},&G\ne1,\\[6pt]
\displaystyle\frac{-R-\ln(1-R)}{\ln2},&G=1.
\end{cases}
```

Terms at a zero logarithm are defined by continuity. The endpoint
$`G=R=1`$ has an infinite energy-unconstrained bound. For transparency, the
standard one-mode formulas from which this expression follows are

| Channel | Thermal occupation parameter | Assisted-capacity upper bound |
|---|---|---|
| Attenuator, $`0<G<1`$ | $`\bar n=N/(1-G)`$ | $`-\log_2[(1-G)G^{\bar n}]-h(\bar n)`$ |
| Amplifier, $`G>1`$ | $`\bar n=N/(G-1)-1`$ | $`\log_2[G^{\bar n+1}/(G-1)]-h(\bar n)`$ |
| Additive noise, $`G=1,\ N<1`$ | Vacuum-output occupation $`N`$ | $`(N-1)/\ln2-\log_2N`$ |

In this table $`h(x)=(x+1)\log_2(x+1)-x\log_2x`$, with $`h(0)=0`$.
Substitution of $`N=G-R`$ gives $`F`$. These are upper bounds for the
generally noisy channels, not exact capacity formulas.
At $`G=0`$ the reduced channel is input independent and its capacities are
zero; the expression containing $`R/G`$ is not used there.

A particularly useful verification and numerically stable representation is

```math
F(G,0)=\partial_RF(G,0)=0,\qquad
\partial_R^2F(G,R)=\frac{1}{\ln2\,(1-R)(G-R)},
```

```math
F(G,R)=\frac1{\ln2}\int_0^R
\frac{R-u}{(1-u)(G-u)}\,du.
```

Consequently, at fixed $`G>0`$,

```math
F(G,R)=\frac{R^2}{2G\ln2}+O(R^3).
```

This is a universal quadratic **upper bound** within the stated two-port
vacuum class. It is not a universal quadratic achievable rate. For the
explicit family below, the reduced channel is already entanglement breaking
throughout $`0\le R\le1/4`$.

## 2. A finite-energy protocol with ideal reflection collection

Use the minimum-positive-output-noise family of
[Scattering and noise](scattering_noise.md). Write

```math
f=\sqrt G,\quad b=\sqrt R,\quad d=f-b,\quad
r^2=(1-b)(1+f),
\qquad
A=\begin{pmatrix}r&b\\-f&r\end{pmatrix}.
```

Its spontaneous occupations are $`n_1=d(1-b)`$ and $`N=d(1+f)`$,
and $`\det A=1+d`$. The allowed domain is $`0\le b\le\min(f,1)`$.
The sender prepares a local two-mode squeezed state with a retained
reference and signal mean occupation $`n>0`$. After scattering, the sender
heterodynes $`b_1`$, announces the outcome, and both parties displace their
remaining modes by the negative conditional mean. This is a deterministic
protocol; it has no outcome selection.

Gaussian conditioning gives, with $`D=r^2n+n_1+1`$,

```math
n_A=\frac{nR}{D},\qquad
n_B+1=\frac{(n+1)(1+d)^2}{D},\qquad
n_B-n_A=\frac{(n+1)N}{D},
```

```math
m=-\frac{\sqrt{n(n+1)}\,b(1+d)}{D},
\qquad |m|^2=n_A(n_B+1).
```

$`n_A,n_B`$ are the occupations of the centered conditional reference and
receiver modes; $`m=\langle a_Aa_B\rangle`$. The two symplectic
occupations are $`0`$ and $`n_B-n_A`$. The conditional covariance is
independent of the measured outcome. Thus the two parties can produce
identical centered states on every use, with coherent information

```math
I_n(G,R)=h(n_B)-h(n_B-n_A)>0\qquad(R>0).
```

The hashing inequality makes this a one-way entanglement-distillation rate
after the classical return measurement has been communicated
[Devetak and Winter 2005](https://doi.org/10.1098/rspa.2004.1372).
Therefore it is an achievable rate for $`Q_2(\Psi_1)`$.
The distillation operation is not required to be Gaussian.

To justify applying finite-dimensional hashing, let $`\rho_{AB}`$ be the
centered conditional state and locally apply the finite-output channel

```math
\mathcal C_L(\sigma)=P_L\sigma P_L
+\mathrm{Tr}[(I-P_L)\sigma]|0\rangle\langle0|,
\qquad P_L=\sum_{j=0}^L|j\rangle\langle j|.
```

The states $`\rho^{(L)}=(\mathcal C_L\otimes\mathcal C_L)(\rho)`$
converge in trace norm to $`\rho`$. This local, trace-preserving truncation
does not increase either mean occupation. Entropy continuity under the
one- and two-oscillator energy bounds therefore gives
$`S(\rho_B^{(L)})\to S(\rho_B)`$ and
$`S(\rho_{AB}^{(L)})\to S(\rho_{AB})`$; see
[Winter 2016, Lemma 15](https://arxiv.org/pdf/1507.07775).
Finite-dimensional hashing at each fixed $`L`$, followed by $`L\to\infty`$,
achieves every rate below $`I_n(G,R)`$. No postselection or unconstrained
infinite-dimensional entropy-continuity assumption is needed.

### Unity forward gain and one quantum per probe

Set $`G=1`$, $`n=1`$, $`s=\sqrt R`$, and $`p=1-s`$. Then

```math
r^2=2p,\qquad n_1=p^2,\qquad N=2p,\qquad
D=(2-s)^2,
```

```math
n_A=\frac{R}{(2-\sqrt R)^2},\qquad n_B=1,
```

```math
I_1(R)=2-h\!\left(1-\frac{R}{(2-\sqrt R)^2}\right)
=\frac R4+O(R^{3/2}).
```

Both the probe and the corrected receiver occupation stay bounded. In the
usual complex heterodyne outcome convention, the conditional means before
centering are

```math
\langle a_A\rangle_y=\frac{r\sqrt{n(n+1)}}{D}\,y^*,
\qquad
\langle b_2\rangle_y=-\frac{r(n+p)}{D}\,y
\quad(G=1).
```

Their coefficients and the outcome variance $`D`$ stay bounded as
$`R\downarrow0`$ at fixed $`n`$. This avoids the divergent corrected-output
energy of the separate, operator-level cancellation protocol discussed in
the [collection proof](collection_boundary.md). It does not make pumps,
atomic phase references or mode-selective detection free resources.

## 3. A matching linear-order upper bound on the full channel

The following bound applies to the complete collected-return channel,
including arbitrary non-Gaussian encodings and adaptive local protocols.
It is an upper bound on $`Q_2`$, **not** a general upper bound on secret-key
capacity.

### Local teleportation simulation

The channel is displacement covariant: an input displacement $`D(\alpha)`$
induces displacements $`D(A_{11}\alpha)`$ on the sender's return and
$`D(A_{21}\alpha)`$ on the receiver. The corrections are local across the
communication cut. Let

```math
J_n=(\mathrm{id}\otimes\Psi_1)
(|\mathrm{TMSV}_n\rangle\langle\mathrm{TMSV}_n|),
```

with the reference and return held by the sender. Braunstein–Kimble
teleportation using this resource implements $`\Psi_1\circ\mathcal T_n`$,
where the teleportation noise channel $`\mathcal T_n`$ tends strongly to the
identity as $`n\to\infty`$; see
[Pirandola, Laurenza and Braunstein 2018](https://doi.org/10.1140/epjd/e2018-90253-1).
The convergence holds on each fixed input state together with any retained
reference. It extends from finite-energy states to arbitrary trace-class
states by finite-support approximation and trace-norm contractivity.

For a fixed $`m`$-use adaptive protocol, let $`\sigma_j`$ be its joint input
and memory state immediately before the $`j`$th **exact** channel use.
Telescoping from exact prefixes to simulated suffixes and applying
contractivity gives

```math
\|\rho_m^{(n)}-\rho_m\|_1
\le\sum_{j=1}^m
\left\|\bigl[(\Psi_1\circ\mathcal T_n-\Psi_1)
\otimes\mathrm{id}\bigr](\sigma_j)\right\|_1
\longrightarrow0.
```

Each $`\sigma_j`$ is fixed independently of $`n`$, so strong convergence
suffices term by term. This pointwise statement does not assert an
unconstrained diamond-norm limit uniform over all input energies.

Define logarithmic negativity across receiver versus sender by
$`E_N(\rho)=\log_2\|\rho^{T_B}\|_1`$. It is additive and monotone under
deterministic LOCC
[Vidal and Werner 2002](https://doi.org/10.1103/PhysRevA.65.032314).
If the final target is a maximally entangled state of Schmidt rank $`M`$,
its overlap $`F=\langle\Phi_M|\rho|\Phi_M\rangle`$ with the actual
output obeys

```math
MF\le\|\rho^{T_B}\|_1.
```

This follows from $`\|\Phi_M^{T_B}\|_\infty=1/M`$ and trace-norm duality.
For the simulation of an $`m`$-use protocol, write its target overlap as
$`F_n`$. The simulated output is an LOCC map of $`J_n^{\otimes m}`$,
which gives

```math
\frac{\log_2M}{m}\le E_N(J_n)-\frac{\log_2F_n}{m}.
```

First take $`n\to\infty`$ for the fixed protocol, so that $`F_n\to F`$
and its target overlap is reproduced; then take the achievable coding sequence
$`m\to\infty`$, with error tending to zero. No asymptotic-continuity
assumption for logarithmic negativity is needed. It follows that

```math
Q_2(\Psi_1)\le\lim_{n\to\infty}E_N(J_n).
```

### Evaluation for the stable family

For $`G=1`$, define $`s=\sqrt R`$, $`p=1-s`$, and $`r=\sqrt{2p}`$.
In the position-quadrature order (reference, return, receiver), the Choi
covariance block is

```math
X=\begin{pmatrix}
n+\tfrac12&r\sqrt{n(n+1)}&-\sqrt{n(n+1)}\\
r\sqrt{n(n+1)}&2pn+p^2+\tfrac12&-r(n+p)\\
-\sqrt{n(n+1)}&-r(n+p)&n+2p+\tfrac12
\end{pmatrix}.
```

The momentum block is $`\mathrm{diag}(-1,1,1)X
\mathrm{diag}(-1,1,1)`$. After the receiver's partial transpose,
the symplectic eigenvalues are the absolute eigenvalues of
$`X\mathrm{diag}(-1,1,-1)`$. Its characteristic polynomial is

```math
\lambda^3+(2sn+\tfrac32-s^2)\lambda^2
-\left[(p^2+s^2)n+p^2+\tfrac14\right]\lambda
-\left[\frac{pn}{2}+\frac{p^2}{4}+\frac p2+\frac18\right]=0.
```

For fixed $`0<s<1`$, one eigenvalue is $`-2sn+O(1)`$. The two finite
eigenvalues solve

```math
2s\lambda^2-(p^2+s^2)\lambda-\frac p2=0.
```

The quadratic has value $`-p^2`$ at $`\lambda=1/2`$ and value $`s^2`$
at $`\lambda=-1/2`$. Its positive root is therefore above $`1/2`$ and
its negative root lies between $`-1/2`$ and zero. The latter's absolute
value is

```math
\nu_-=
\frac{p}{p^2+s^2+\sqrt{1+4Rp^2}}<\frac12.
```

It is the only limiting symplectic eigenvalue below the vacuum value.
Consequently

```math
U(R)=\lim_{n\to\infty}E_N(J_n)
=\log_2\frac{p^2+R+\sqrt{1+4Rp^2}}{2p},
\qquad p=1-\sqrt R,
```

```math
U(R)=\frac{2R}{\ln2}-\frac{2R^2}{\ln2}+O(R^{5/2}).
```

Combining the two sides gives the principal rate statement:

```math
\boxed{\quad I_1(R)\le Q_2(\Psi_1)\le U(R),\qquad
Q_2(\Psi_1)=\Theta(R)\quad(R\downarrow0).\quad}
```

The constants are not matched, so the exact capacity remains undetermined.
The upper bound allows unbounded encoding energy; the lower bound already
works with one quantum of mean signal occupation. At $`R=0`$ the exact
collection theorem gives zero. At $`R=1`$ the effective family is a unitary
forward channel, whose unconstrained capacity is infinite; the one-quantum
protocol remains finite. Neither endpoint is obtained by interchanging the
small-$`R`$ and infinite-squeezing limits without justification.

## 4. Collection accuracy and a numerical example

For the unity-gain family, $`c=N-G=1-2\sqrt R`$. In the range
$`0<R<1/4`$, the exact [collection boundary](collection_boundary.md) is

```math
\eta_{\mathrm{crit}}(R)=\frac{1-2\sqrt R}{(1-\sqrt R)^2},
\qquad
1-\eta_{\mathrm{crit}}=\frac{R}{(1-\sqrt R)^2}.
```

Positive two-way capacity requires strict inequality
$`\eta>\eta_{\mathrm{crit}}`$. Hence the tolerated uncollected fraction is
of order $`R`$ near perfect isolation. A fixed collection efficiency below
one eventually puts the family on the zero-capacity side. Positivity just
above threshold does not establish the ideal-collection linear rate there.

At $`G=1`$, $`R=0.01`$:

| Quantity | Value per normalized mode |
|---|---:|
| General reduced-channel upper bound $`F(1,R)`$ | $`7.262\times10^{-5}`$ bits/use |
| This family's reduced-channel capacity | Zero, because $`N=1.8>G`$ |
| Ideal-collection achievable rate $`I_1(R)`$ | $`2.773\times10^{-3}`$ ebits/use |
| Ideal-collection full-channel upper bound $`U(R)`$ | $`2.862\times10^{-2}`$ ebits/use |
| Collection threshold $`\eta_{\mathrm{crit}}`$ | $`0.98765432099`$ |

The collection gap is operationally significant. It should not be inferred
from forward transmission alone or from the quantum character of one
particular Gaussian detection scheme.

## 5. Dependencies and limits

The noise inequality is derived in [Scattering and noise](scattering_noise.md).
The Gaussian capacity formulas, hashing inequality, logarithmic negativity,
and continuous-variable teleportation simulation are established inputs,
identified in [Related work](../references/RELATED_WORK.md) and the
[bibliography](../references/references.bib). The finite conditional-state
calculation and Choi polynomial are reproduced by
[the verification suite](../verification/README.md), including exact rational
coefficient checks. Numerical checks illustrate and audit the analysis;
they do not establish an infinite-dimensional converse or a priority claim.

The matched rate order is for the specified stationary linear model with
ideal return collection and arbitrary local quantum processing. The
[atomic realization](stable_atomic_model.md) has finite pump, phase-reference
and approximation requirements. The [wave-packet analysis](finite_bandwidth.md)
explains why per-mode scaling alone does not fix the rate per second, and why
microscopic errors must decrease when the target entanglement margin shrinks.

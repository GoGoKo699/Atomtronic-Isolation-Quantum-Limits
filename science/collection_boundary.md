# An exact boundary for reflection-assisted communication

Collecting the reflected output changes the quantum communication resource
provided by a directional scatterer. This section establishes the exact
collection efficiency needed to distribute entanglement when the receiver
accesses one positive-norm output. The converse permits arbitrary inputs,
quantum memories, adaptive protocols, and non-Gaussian operations. A
heterodyne measurement and linear feedforward attain the complementary
positive-capacity region.

The [operational model](model.md) specifies the modes and normalization.
The [scattering-noise constraints](scattering_noise.md) connect the boundary
to reverse transmission. Achievable rates and rate upper bounds are treated
separately in [communication rates](communication_rates.md). A
[stable atomic model](stable_atomic_model.md) supplies a physical realization;
[interpretation and scope](interpretation.md) discusses mode access and
experimental meaning.

## 1. Resource and notation

At one normalized frequency mode, the two positive outputs are

```math
b_+=Aa_++Be^\dagger,
\qquad
A\in\mathbb C^{2\times2},
\qquad
AA^\dagger-BB^\dagger=I_2.
```

Alice controls $`a_1`$. The other positive input $`a_2`$ and all negative
inputs $`e`$ are independent vacuum. Bob receives only $`b_2`$. Alice receives
the reflected mode through pure loss:

```math
z=\sqrt\eta\,b_1+\sqrt{1-\eta}\,v,
\qquad 0\le\eta\le1,
```

with independent vacuum $`v`$. The resulting broadcast channel is
$`\Psi_\eta:a_1\longrightarrow(z,b_2)`$: the first output stays with
Alice and the second goes to Bob. All remaining outputs are inaccessible.
Define

```math
G=|A_{21}|^2,\qquad
R=|A_{12}|^2,\qquad
N=(BB^\dagger)_{22},\qquad
c=N-G=|A_{22}|^2-1.
```

$`G`$ and $`R`$ are flux-normalized forward and reverse powers. $`N`$ is the
receiver's spontaneous occupation for vacuum inputs. Canonical feasibility
implies

```math
AA^\dagger\ge I_2
\ \Longrightarrow\ A^\dagger A\ge I_2
\ \Longrightarrow\ c+R\ge0.
```

The square two-channel positive block is essential to the last implication
and its interpretation as a constraint on reverse power.

**Collection precedes processing.** The loss defining $`\eta`$ occurs
before Alice can use the reflected field. An inefficiency of one optional
detector is insufficient to define an all-protocol limit if Alice can instead
process the full reflected quantum mode. The theorem concerns the quantum
mode actually available to her.

The capacities below use independent memoryless channel uses, unrestricted
local operations, and unlimited public classical communication. No
entanglement or secret key is initially shared. The secret-key statement
assumes an adversary holding the complete purifying inaccessible environment.

## 2. The exact zero-versus-positive theorem

**Theorem.** Two-way entanglement distribution and secret-key generation
through $`\Psi_\eta`$ are impossible exactly in the region

```math
\boxed{
c\ge0,\qquad (1-\eta)c\ge\eta R.
}
```

In this region the entire channel can be implemented by an instrument local
to Alice, public communication of its outcome, and conditional state
preparation at Bob. Thus the impossibility includes arbitrary non-Gaussian
inputs, retained references, collective coding, quantum memories, and
adaptive local operations.

Outside this region, heterodyne monitoring of $`z`$ and a displacement at Bob
yield a non-entanglement-breaking phase-insensitive channel. Sending one half
of a two-mode squeezed state through it produces distillable entanglement
for every strictly positive finite input occupation. Hence both the two-way
entanglement-distribution capacity $`Q_2`$ and secret-key capacity $`K`$ are
strictly positive there.

For $`c\ge0`$ and $`c+R>0`$, the zero-capacity region can be written

```math
\eta\le\eta_{\mathrm{crit}},
\qquad
\boxed{\eta_{\mathrm{crit}}=\frac{N-G}{N-G+R}.}
```

Equality belongs to the zero-capacity side. At degenerate parameters, use the
two inequalities in the theorem instead of the ratio. The result classifies
zero versus positive capacity; it does not give the value of the positive
capacity. The positive statement applies under any strictly positive signal
energy budget. An exactly zero occupation budget forces the signal to remain
vacuum and is a different case.

## 3. Gaussian complete-positivity calculation

Use vacuum quadrature covariance $`I/2`$ and the order
$`(q_z,q_B,p_z,p_B)`$. For a complex matrix, define its realification by

```math
\mathcal R(H)=
\begin{pmatrix}
\mathrm{Re}H&-\mathrm{Im}H\\
\mathrm{Im}H&\mathrm{Re}H
\end{pmatrix}.
```

Set

```math
L=\mathrm{diag}(\sqrt\eta,1),\qquad
t=LA_{:1},\qquad C=LBB^\dagger L,\qquad
Z=\mathrm{diag}(1,-1).
```

The channel's real quadrature matrices are

```math
X=\mathcal R(t),\qquad
Y=\frac12\mathcal R(I_2-tt^\dagger+2C).
```

Indeed, $`C`$ is its output normal-occupation matrix for a vacuum signal, so
the vacuum output covariance is $`\mathcal R(C+I_2/2)`$.
Subtracting the signal contribution $`XX^T/2`$ gives $`Y`$.

The standard Gaussian CP criterion is

```math
Y+\frac i2\left(\Omega_{\mathrm{out}}-X\Omega_{\mathrm{in}}X^T\right)\ge0,
```

where $`\Omega_m=\mathcal R(-iI_m)`$. See
[Holevo, Eq. (29)](https://arxiv.org/html/0802.0235v1).

Partial transpose on Bob flips $`p_B`$ and has matrix
$`T=\mathrm{diag}(I_2,Z)`$. Congruence by $`T`$ takes the CP matrix
of the transposed Gaussian map to

```math
\frac12\left[
\mathcal R(I_2-tt^\dagger+2C)
+i\mathcal R\bigl(-i(Z-tt^\dagger)\bigr)
\right].
```

The unitary change to annihilation and creation coordinates,

```math
U=\frac1{\sqrt2}
\begin{pmatrix}I_2&iI_2\\I_2&-iI_2\end{pmatrix},
```

block diagonalizes this matrix into $`M\oplus M_+^*`$, with

```math
M=\mathrm{diag}(1,0)-tt^\dagger+C,
\qquad
M_+=\mathrm{diag}(0,1)+C\ge0.
```

The canonical scattering identities reduce the only nonautomatic block to

```math
\boxed{
M=
\begin{pmatrix}
1-\eta+\eta R&
\sqrt\eta\,A_{12}A_{22}^*\\
\sqrt\eta\,A_{12}^*A_{22}&c
\end{pmatrix}.
}
```

Its first diagonal entry is nonnegative and

```math
\det M=(1-\eta)c-\eta R.
```

Consequently the transposed map is CP exactly in the region stated by the
theorem. The calculation holds for arbitrary complex coefficients and any
number of negative modes; it does not assume that all phases can be removed.

## 4. From a Gaussian test to an arbitrary-input converse

### 4.1 A faithful finite-energy state

Fix any $`0<\tau<1`$ and prepare the faithful two-mode squeezed state

```math
|\psi_\tau\rangle_{FA}
=\sum_{n\ge0}\sqrt{p_n}\,|n\rangle_F|n\rangle_A,
\qquad p_n=(1-\tau^2)\tau^{2n}>0.
```

Alice retains the reference $`F`$. Let

```math
J_\tau=(\mathrm{id}_F\otimes\Psi_\eta)
\bigl(|\psi_\tau\rangle\langle\psi_\tau|\bigr).
```

When $`M\ge0`$, this finite-covariance Gaussian state is PPT across
$`B:(F,z)`$. Bob has one mode and the other side has two. The
[Werner–Wolf theorem](https://arxiv.org/html/quant-ph/0009118v1) says that a
Gaussian state of one mode versus any number of modes is separable if and
only if it is PPT. Hence $`J_\tau`$ is separable across this partition.

This step uses Gaussianity only for the faithful test state. The following
argument extends the conclusion to arbitrary input states; it does not
apply a Gaussian separability criterion directly to a non-Gaussian state.

### 4.2 Exact local-instrument representation

The integral representation of separable states in infinite dimensions gives

```math
J_\tau=
\int |\xi_x\rangle\langle\xi_x|_{Fz}
\otimes|\phi_x\rangle\langle\phi_x|_B\,\mu(dx),
```

with normalized measurable vector representatives. A continuous integral,
rather than a countable decomposition, is allowed and sometimes necessary;
see [Holevo, Shirokov, and Werner, Eq. (4)](https://arxiv.org/pdf/quant-ph/0504204).

Expand $`|\xi_x\rangle=\sum_n|n\rangle_F|\xi_n(x)\rangle_z`$.
The reference marginal of $`J_\tau`$ is $`\sum_n p_n|n\rangle\langle n|`$,
so

```math
\int\langle\xi_m(x)|\xi_n(x)\rangle\,\mu(dx)=p_n\delta_{mn}.
```

Define on finite Fock superpositions

```math
(V|n\rangle)(x)=\frac{|\xi_n(x)\rangle_z}{\sqrt{p_n}}.
```

The preceding normalization makes $`V`$ an isometry into
$`L^2(\mu;\mathcal H_z)\simeq\mathcal H_z\otimes L^2(\mu)`$. It extends
uniquely to a bounded isometry on the full input Hilbert space. Thus the
inverse Schmidt weights have not been used as an unbounded physical filter:
the combined map is isometric.

Alice can apply $`V`$, measure the multiplication PVM of its $`L^2(\mu)`$
register, retain the output $`z`$, and announce $`x`$. Bob prepares
$`|\phi_x\rangle`$. Call the resulting channel $`\Gamma`$. On every matrix
unit,

```math
\begin{aligned}
\Gamma(|m\rangle\langle n|)
&=\frac1{\sqrt{p_m p_n}}
\int |\xi_m(x)\rangle\langle\xi_n(x)|
\otimes|\phi_x\rangle\langle\phi_x|\,\mu(dx)\\
&=\Psi_\eta(|m\rangle\langle n|).
\end{aligned}
```

The second equality is the corresponding reference matrix element of
$`J_\tau`$. Equality on matrix units, trace-norm boundedness, and density of
finite-rank operators imply $`\Gamma=\Psi_\eta`$ for every trace-class
input. This is an exact infinite-dimensional local-instrument simulation.

For a measurable event $`E`$, its Alice instrument map is

```math
\Lambda_E(\rho)=
\mathrm{Tr}_{L^2(\mu)}
\left[(I_z\otimes P_E)V\rho V^\dagger(I_z\otimes P_E)\right],
```

where $`P_E`$ is the multiplication PVM. These maps are completely positive,
countably additive, and sum to a trace-preserving map. Their definition does
not require pointwise bounded Kraus densities.

### 4.3 Adaptive protocols

Each channel use is now a local instrument plus public communication and
local preparation. Inserting such uses into an arbitrary adaptive LOCC
protocol cannot generate entanglement from an initially separable state.
The statement includes all local reference and purification registers and
allows non-Gaussian operations. No energy bound, entropy-continuity estimate,
or unconstrained diamond-norm limit is needed for this converse.

### 4.4 Secret key requires the stronger simulation

PPT alone does not imply zero distillable secret key. Here the instrument
representation supplies the additional conclusion. An isometry for the
same channel is

```math
(W|\psi\rangle)(x)
=(V|\psi\rangle)(x)\otimes|\phi_x\rangle_B.
```

The environment is the $`L^2(\mu)`$ register. Measuring its multiplication
PVM yields $`x`$, conditioned on which Bob has a fixed prepared state
independent of Alice's remaining quantum information. By Stinespring
uniqueness, an adversary holding the complete physical purifying complement
can realize this measurement on an equivalent dilation. The transcript is
not a trusted hidden resource created by choosing a different representation.

Every use is therefore simulable with public communication and local
operations, without preshared secrecy. Such a resource cannot generate
secret key. If some inaccessible environment is trusted and excluded from
the adversary, the entanglement converse still follows from the channel,
but the stated secret-key prohibition requires a separate security model.

## 5. Optimal monitoring and finite-energy achievability

Heterodyne the actual collected mode $`z`$. Its complex outcome has a
Naimark representation $`m=z+h^\dagger`$, where $`h`$ is independent vacuum;
the real and imaginary parts of $`m`$ commute. Bob applies the displacement
$`k m`$.

The corrected phase-insensitive channel has signal amplitude
$`\alpha=t_2+k t_1`$, gain $`g_k=|\alpha|^2`$, and added occupation

```math
n_k=C_{22}+|k|^2(C_{11}+1)+2\mathrm{Re}(kC_{12}).
```

Subtracting gives the same quadratic form as the converse:

```math
g_k-n_k=-M_{22}-M_{11}|k|^2-2\mathrm{Re}(kM_{12}).
```

For $`a=M_{11}>0`$,

```math
\boxed{
k_*=-\frac{M_{12}^*}{a},\qquad
\max_k(g_k-n_k)=-\frac{\det M}{a}.
}
```

Every point outside the zero-capacity region has $`a>0`$ and $`\det M<0`$;
the singular corner is treated below. Thus the corrected channel has
$`g_*>n_*`$, exactly the non-entanglement-breaking condition in the
occupation convention used here.

For comparison with an outcome normalized to the original reflected field,
let $`\lambda=(1-\eta)/\eta`$ when $`\eta>0`$. The
normalized outcome is
$`m_{\rm raw}=b_1+\sqrt\lambda\,v+h^\dagger/\sqrt\eta`$, and the
corresponding gain is

```math
k_{\rm raw}=-\frac{A_{22}A_{12}^*}{R+\lambda}.
```

It gives

```math
q_{\min}=\frac{|A_{22}|^2\lambda}{R+\lambda},
\qquad
g_*-n_*=1-q_{\min}.
```

The strict condition $`q_{\min}<1`$ is precisely
$`(1-\eta)c<\eta R`$. At zero collection, use the original
channel directly: $`g=G,n=N`$.

### Finite input energy is sufficient

Prepare a TMSV with signal mean occupation $`x>0`$. After the corrected
channel, local phase rotations put its two-mode covariance in standard
form, with

```math
n_A=x,\qquad n_B=g_*x+n_*,\qquad |m|^2=g_*x(x+1).
```

The partial-transpose condition is violated exactly when

```math
\boxed{|m|^2-n_A n_B=x(g_*-n_*)>0.}
```

Hence every nonzero finite $`x`$ gives NPT Gaussian entanglement on the
positive side. The
[Giedke–Duan–Cirac–Zoller distillability theorem](https://arxiv.org/html/quant-ph/0104072v2)
then yields a strictly positive EPR distillation rate using unrestricted
local operations. Measuring the distilled pairs yields secret key. General
non-Gaussian distillation is permitted; this is not a claim that Gaussian
operations alone distill Gaussian entanglement.

For ideal collection and $`R>0`$, the gain cancels the unwanted positive
input and produces a quantum-limited amplifier:

```math
g_{\rm ff}=\frac{|\det A|^2}{R},\qquad n_{\rm ff}=g_{\rm ff}-1.
```

This corrected channel establishes achievability. It need not maximize the
original broadcast resource's capacity. Its gain and output occupation can
grow as $`R\to0`$; the bounded-energy rate construction in
[communication rates](communication_rates.md) addresses that distinct
resource question.

## 6. Gauge-invariant Gaussian noise

The vacuum scalar boundary extends to an exact matrix criterion when the
auxiliaries have gauge-invariant Gaussian noise. Suppose $`a_2`$ has
occupation $`n_2\ge0`$ and the negative modes have a jointly gauge-invariant
Gaussian state with

```math
(n_-)_{ij}=\langle e_j^\dagger e_i\rangle,
\qquad \langle e_i e_j\rangle=0.
```

The positive and negative auxiliary blocks are independent of each other
and of the signal; correlations within the negative block are allowed. For
vacuum signal the full positive-output normal-occupation matrix is

```math
\mathsf K=B(I+n_-^T)B^\dagger+n_2 A_{:2}A_{:2}^\dagger.
```

After pure-loss collection, set $`C=L\mathsf K L`$ and $`t=LA_{:1}`$.
The Gaussian calculation, instrument proof, and monitoring construction
remain valid. The exact zero-capacity condition is

```math
\boxed{M=\mathrm{diag}(1,0)-tt^\dagger+L\mathsf K L\ge0.}
```

In scalar form, write

```math
a=1+\eta(\mathsf K_{11}-|A_{11}|^2),\qquad
d=\mathsf K_{12}-A_{11}A_{21}^*,\qquad
c_T=\mathsf K_{22}-G.
```

Then

```math
M=\begin{pmatrix}a&\sqrt\eta d\\
\sqrt\eta d^*&c_T\end{pmatrix},
\qquad
\det M=a c_T-\eta|d|^2.
```

When $`a>0`$, the optimal raw-reflection gain is
$`k_{\rm raw}=-\eta d^*/a`$, and the maximum corrected
$`g-n`$ is $`-\det M/a`$. Thus the constructive and impossible regions
still coincide exactly.

Thermal noise satisfies $`\mathsf K\ge BB^\dagger`$, so it increases
$`M`$ in positive-semidefinite order. The vacuum zero-capacity region
therefore remains inaccessible. Additional noise may enlarge it.
The three scalars $`G,R,N`$ no longer determine the exact thermal boundary:
source noise and complex cross-correlations also enter $`\mathsf K`$.

An independent thermal collection bath of occupation $`n_v`$ adds
$`\mathrm{diag}((1-\eta)n_v,0)`$ to $`C`$. The same matrix
criterion applies. Consecutive pure-loss stages before Alice's access
multiply their transmissivities.

### General Gaussian form and the singular case

The preceding argument also supplies a general lemma: a centered,
finite-covariance, gauge-covariant Gaussian channel with one input mode and
two outputs is specified here by $`t,C`$, with physicality conditions

```math
C\ge0,\qquad P=I-tt^\dagger+C\ge0.
```

It is local-instrument simulable across Alice's first output versus Bob's
second exactly when $`M=\mathrm{diag}(1,0)-tt^\dagger+C\ge0`$.
Otherwise heterodyne monitoring and feedforward produce distillable
entanglement as above.

To close the singular case, let $`a=M_{11}=P_{11}=0`$. Positivity of $`P`$
forces $`P_{12}=M_{12}=0`$. Positivity of $`C`$ requires
$`|t_1|\ge1`$. If $`|t_1|=1`$, it also forces $`t_2=0`$, hence
$`M_{22}\ge0`$. If $`|t_1|>1`$, its determinant gives

```math
M_{22}\ge\frac{|t_2|^2}{|t_1|^2-1}\ge0.
```

Thus $`a=0`$ always belongs to the zero region. Every nonlocal channel has
$`a>0`$ and a well-defined finite optimizer. This lemma concerns
gauge-covariant Gaussian channels; arbitrary phase-sensitive or
non-Gaussian auxiliary resources require a different analysis.

## 7. Boundary and degenerate cases

| Case | Evaluation | Result |
|---|---|---|
| $`\eta=0`$ | $`M=\mathrm{diag}(1,c)`$ | Zero exactly when $`N\ge G`$. |
| $`R=0`$ | Feasibility gives $`c\ge0`$ and $`M_{12}=0`$ | Zero for every collection efficiency, including one. |
| $`c=0,R>0`$ | $`\det M=-\eta R`$ | Zero at zero collection; positive for every $`\eta>0`$. |
| $`c<0`$ | $`M_{22}<0`$ | The direct channel already works for every efficiency. |
| $`c>0,R>0`$ | $`\eta_{\rm crit}=c/(c+R)`$ | Equality and smaller efficiencies give zero capacity. |
| $`c=R=0`$ | Both original inequalities hold | Zero for every efficiency; the vacuum canonical model also forces $`G=N=0`$. |
| $`\eta=1,R=0`$ | $`M=\mathrm{diag}(0,c)`$ | Zero; do not substitute $`0/0`$ into a feedback formula. |
| Passive device with no negative modes | $`N=0,R=G`$ | Positive exactly when $`G>0`$. |

The corner $`c=R=0`$ forces $`G=0`$ because $`A_{12}=0`$ and
$`|A_{22}|=1`$ make $`\det(AA^\dagger-I)=-G`$.

If $`G=0,R>0`$ is canonically feasible, ideal return assistance can still
distribute entanglement. Bob's unassisted marginal being input independent
does not make the full active broadcast resource local: the measurement
outcome from Alice's correlated return is an additional resource. The
theorem concerns that complete accessible resource rather than coherent
forward power alone.

## 8. Consequences and limits

For the unity-forward minimum-noise family, let $`s=\sqrt R`$. In its
entanglement-breaking forward regime, $`0<R<1/4`$,

```math
c=1-2\sqrt R,\qquad
\eta_{\rm crit}
=\frac{1-2\sqrt R}{(1-\sqrt R)^2}
=1-\frac{R}{(1-\sqrt R)^2}.
```

At one percent reverse power this requires
$`\eta>0.9876543209876543`$ for entanglement distribution. The
uncollected reflection fraction must scale as order $`R`$ near perfect
isolation. This requirement belongs to the accessible channel itself;
another non-Gaussian decoder cannot remove it within the model.

The theorem does not prohibit passive multiport isolation, communication
with access to negative partners, or protocols that control additional
inputs. It does not identify nonlinear critical-current asymmetry with
linear scattering nonreciprocity. Those distinctions are detailed in
[interpretation](interpretation.md).

The exact boundary is a two-way entanglement and key result. A
non-entanglement-breaking corrected Gaussian channel can still have zero
unassisted quantum capacity. Actual rates, resource costs, and the
difference between discarding and monitoring the return belong to
[communication rates](communication_rates.md).

## Appendix: finite-input verification of the faithful-state argument

The direct-integral proof above can also be checked through ordinary
finite-input Choi matrices. For $`d=M+1`$, apply to the reference the bounded
finite-rank filter

```math
F_M=\sum_{n=0}^M\frac{|n\rangle\langle n|}{\sqrt{d p_n}}.
```

It converts $`J_\tau`$ exactly to the normalized Choi state for the input
subspace spanned by $`|0\rangle,\ldots,|M\rangle`$:

```math
(F_M\otimes I)J_\tau(F_M^\dagger\otimes I)
=(\mathrm{id}\otimes\Psi_\eta)
\bigl(|\Omega_d\rangle\langle\Omega_d|\bigr),
\qquad
|\Omega_d\rangle=\frac1{\sqrt d}\sum_{n=0}^M|n,n\rangle.
```

This operator has trace one because the reference marginal is diagonal with
weights $`p_n`$. Rescaling $`F_M`$ to a physical filter only changes its
success probability. The filtered Choi state remains separable across Bob
versus reference plus return. Choi inversion gives an Alice-local
instrument and conditional Bob preparation for every finite input cutoff.
Trace-norm approximation then proves separability for arbitrary inputs.
The exact direct-integral isometry in Section 4 supplies the stronger
full-space instrument statement without taking a channel-norm limit.

## References used in the proof

- A. S. Holevo, **Entanglement-breaking channels in infinite dimensions**,
  Problems of Information Transmission **44**, 171–184 (2008).
  [arXiv:0802.0235](https://arxiv.org/abs/0802.0235).
- R. F. Werner and M. M. Wolf, **Bound Entangled Gaussian States**,
  Physical Review Letters **86**, 3658–3661 (2001).
  [DOI](https://doi.org/10.1103/PhysRevLett.86.3658),
  [arXiv:quant-ph/0009118](https://arxiv.org/abs/quant-ph/0009118).
- A. S. Holevo, M. E. Shirokov, and R. F. Werner, **Separability and
  Entanglement-Breaking in Infinite Dimensions**, Russian Mathematical
  Surveys **60**, No. 2 (2005).
  [arXiv:quant-ph/0504204](https://arxiv.org/abs/quant-ph/0504204).
- G. Giedke, L.-M. Duan, J. I. Cirac, and P. Zoller,
  **Distillability Criterion for all Bipartite Gaussian States**,
  Quantum Information and Computation **1**(3), 79–86 (2001).
  [DOI](https://doi.org/10.26421/QIC1.3-7),
  [arXiv:quant-ph/0104072](https://arxiv.org/abs/quant-ph/0104072).

The relationship to environmental correction and directional-amplifier
literature is discussed in [related work](../references/RELATED_WORK.md).

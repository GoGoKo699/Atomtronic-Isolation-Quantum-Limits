# Weedbrook: source-to-project bridge

**Single educational anchor:** C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro and S. Lloyd, *Gaussian Quantum Information*, Reviews of Modern Physics **84**, 621–669 (2012), [doi:10.1103/RevModPhys.84.621](https://doi.org/10.1103/RevModPhys.84.621).

Section and equation pointers below refer specifically to the freely available [arXiv:1110.3234v1](https://arxiv.org/abs/1110.3234v1), submitted 14 October 2011, rather than to journal page numbering. The review is the foundation, not a source for this project's collection theorem or atomic implementation. Use the [30-milestone map](MILESTONES.md) to connect these prerequisites to the full scientific account.

## 1. Source map

Read selected sections as needed; reading the entire review is not a prerequisite.

| Anchor sections in arXiv v1 | Use here | Milestones |
|---|---|---|
| I.D; II.A.1–2 | Conventions, covariance matrices, Gaussian transformations | M01–M04 |
| II.B.1–3, 6–7 | Thermal modes, displacements, beam splitters, squeezed probes | M05–M07 |
| II.C.1, 3; II.D.1–2 | Symplectic eigenvalues, entropy, partial transpose, entanglement | M08, M10, M21–M22 |
| II.E.1–3, especially Eq. (65) | Heterodyne measurement and conditional covariance | M06–M07, M19, M21 |
| IV.A | Continuous-variable teleportation | M22 |
| V.A–B, D, F | Channels, quantum capacity, entanglement distribution and key | M09–M11, M16–M23 |

Atomic collisions, mode selection and finite-packet accounting are supplied locally in the [atomic model](../science/stable_atomic_model.md) and [bandwidth analysis](../science/finite_bandwidth.md). They are not silently assigned to the review.

## 2. Translate conventions before applying a formula

This project uses $`[q,p]=i`$ and vacuum covariance $`I/2`$. The review uses $`[q_W,p_W]=2i`$ and vacuum covariance $`I`$. The same physical state therefore has

```math
q_W=\sqrt2 q,\qquad p_W=\sqrt2 p,\qquad V_W=2V.
```

A symplectic eigenvalue likewise obeys $`\nu_W=2\nu`$. Physical covariance matrices have $`\nu\ge1/2`$ in project units; the associated thermal occupation is $`\nu-1/2`$. The vacuum threshold in a partial-transpose calculation is also $`1/2`$, not one.

The mode operator $`a=(q+ip)/\sqrt2=(q_W+ip_W)/2`$ is unchanged. Consequently occupations, transmission powers, and the complex coherent-state label are unchanged by this quadrature rescaling. Do not multiply $`G,R,N`$ by two.

The review normally orders quadratures mode by mode. The collection proof uses all positions followed by all momenta, $`(q_z,q_B,p_z,p_B)`$. A permutation changes the displayed matrices, not the channel. In this order,

```math
\Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix},\qquad
V+\frac{i\Omega}{2}\ge0.
```

For a centered one-mode state, mean occupation is $`(\operatorname{Tr}V-1)/2`$. Nonzero first moments add a separate displacement-energy contribution. These conversions prevent a factor-of-two error from moving an apparent entanglement boundary.

## 3. From an atomic scattering experiment to a channel

Imagine sending an atomic wave packet into port 1. The receiver obtains the transmitted field. A reflected field returns toward the sender, while idler outputs remain inaccessible. The receiver's quantum state depends on all those assignments, not merely on how much coherent signal was transmitted.

For the stationary two-positive-port vacuum model,

```math
\boldsymbol b=A\boldsymbol a+B\boldsymbol e^\dagger,
\qquad AA^\dagger-BB^\dagger=I_2.
```

The creation operators contribute a minus sign to the commutator. They represent pumped idler channels, not permission to omit ordinary positive ports. Define

```math
G=|A_{21}|^2,\qquad R=|A_{12}|^2,\qquad
N=(BB^\dagger)_{22}.
```

Here $`R`$ is reverse **power**, not reverse amplitude. $`N`$ is the receiver occupation when the signal and auxiliaries are vacuum. If the reflection is discarded, the receiver sees

```math
V\longmapsto GV+\left[N+\frac{1-G}{2}\right]I_2.
```

Substituting vacuum input $`V=I_2/2`$ yields $`(N+1/2)I_2`$, which checks the occupation convention. This reduced channel is entanglement breaking at $`N\ge G`$; its derivation and imported channel results are in [Communication rates §1](../science/communication_rates.md#1-the-reduced-forward-channel).

Collecting the return changes the channel itself:

```math
z=\sqrt\eta\,b_1+\sqrt{1-\eta}\,v,
\qquad \Psi_\eta:a_1\longrightarrow(z,b_2).
```

The output $`z`$ stays with the sender. Collection loss occurs **before** any usable processing. An inefficient optional detector does not impose the same restriction when the full reflected quantum mode is otherwise available. See [Model §2](../science/model.md#2-two-operational-interfaces).

## 4. One worked threshold example

Set $`c=N-G`$. The project's exact vacuum condition is

```math
Q_2(\Psi_\eta)=K(\Psi_\eta)=0
\quad\Longleftrightarrow\quad
c\ge0\ \text{and}\ (1-\eta)c\ge\eta R.
```

It is a statement about the specified memoryless channel, initially unentangled parties, arbitrary local operations and public classical communication. The key statement additionally assumes that the inaccessible environment is untrusted and held by a purifying adversary.

The [stable unity-forward family](../science/stable_atomic_model.md#resonant-occupations-and-the-collection-threshold) at $`R=1/100`$ has $`G=1`$ and $`N=9/5`$. Thus $`c=4/5`$ and

```math
\eta_{\rm crit}=\frac{c}{c+R}=\frac{80}{81}
\simeq0.987654321.
```

At collection $`\eta=0.98`$, the determinant expression is $`(1-\eta)c-\eta R=0.0062`$: the channel cannot distribute entanglement. At $`\eta=0.99`$, it is $`-0.0019`$: a constructive protocol distributes entanglement. Equality at $`80/81`$ belongs to the zero side. Discarding the return gives zero capacity for this family because $`N>G`$.

This is not an exact formula for the positive capacity. It says which side can communicate at all. At $`c=R=0`$ the ratio is undefined; the original pair of inequalities remains valid. The [boundary cases](../science/collection_boundary.md#7-boundary-and-degenerate-cases) must not be replaced by division by zero.

## 5. Why the boundary covers more than Gaussian receivers

The proof introduces the Hermitian matrix

```math
M=\begin{pmatrix}
1-\eta+\eta R&\sqrt\eta\,A_{12}A_{22}^*\\
\sqrt\eta\,A_{12}^*A_{22}&c
\end{pmatrix},\qquad
\det M=(1-\eta)c-\eta R.
```

Its positivity is equivalent to complete positivity after partial transpose at the receiver. That Gaussian calculation is only the first step. A faithful finite-energy squeezed probe produces a Gaussian state with one receiver mode versus two sender modes. The one-versus-many Gaussian PPT/separability theorem applies to that state. An explicit isometric construction then turns its separable decomposition into a sender-local instrument plus conditional receiver preparation, agreeing with the channel on every input matrix unit and hence on every trace-class input.

This additional argument is why non-Gaussian encodings, memories and adaptive protocols are included. A covariance test on one chosen input would not establish that conclusion. Nor does PPT by itself imply zero secret key: the proof separately uses the public instrument outcome and the purifying environment. Follow [Collection boundary §§3–4](../science/collection_boundary.md#3-gaussian-complete-positivity-calculation), including the cited primary theorems.

On the other side, heterodyne the available return and communicate its outcome. A calibrated displacement at the receiver gives a phase-insensitive channel with corrected gain $`g`$ and noise occupation $`n`$. For $`a=M_{11}>0`$ the optimal value satisfies

```math
\max(g-n)=-\frac{\det M}{a}.
```

For a squeezed probe with mean signal occupation $`x>0`$, the resulting two-party correlations obey $`|m|^2-n_A n_B=x(g-n)`$. A positive value witnesses NPT Gaussian entanglement. Distillation then permits general local operations; the result does **not** claim that Gaussian operations alone distill Gaussian entanglement. See [Collection boundary §5](../science/collection_boundary.md#5-optimal-monitoring-and-finite-energy-achievability).

## 6. From Gaussian conditioning to a finite-energy rate

For joint covariance blocks $`V_{AB},V_z,C`$, heterodyne conditioning in project units gives

```math
V_{AB|z}=V_{AB}-C(V_z+I_2/2)^{-1}C^T.
```

The added half-unit is measurement vacuum noise. The conditional covariance is independent of the outcome; local displacements remove the outcome-dependent means. No favorable outcomes are selected. This is the project-unit version of the review's Eq. (65).

For the stable family, ideal collection and a mean-one signal probe, the centered state has

```math
n_A=\frac{R}{(2-\sqrt R)^2},\qquad n_B=1,
\qquad I_1(R)=2-h(1-n_A),
```

where $`h(x)=(x+1)\log_2(x+1)-x\log_2x`$ is a thermal-mode entropy and $`h(0)=0`$. A hashing argument makes $`I_1`$ an achievable entanglement rate. The canonical account justifies finite-dimensional truncation before invoking that coding theorem.

The full-channel upper bound uses local teleportation simulation and logarithmic negativity, with simulation accuracy taken to its limit for each fixed protocol **before** the coding-length limit. It does not claim energy-unconstrained diamond-norm convergence. The resulting bounds give

```math
I_1(R)=R/4+O(R^{3/2}),\qquad
Q_2(\Psi_1)\le U(R)=2R/\ln2+O(R^2).
```

Thus the ideal-collection family has matched linear order, not a known exact capacity. The discarded-return expression of order $`R^2`$ is a general **upper envelope**, not an achievable rate for that same family. Its actual discarded-return capacity is zero near isolation. Logarithmic negativity bounds the stated quantum capacity; it is not a general secret-key bound. See [Communication rates](../science/communication_rates.md).

## 7. The atomic and finite-pulse bridge

The effective Hamiltonian combines one conversion term with two pairing terms. The [microscopic construction](../science/stable_atomic_model.md#3-a-number-conserving-collision-model-in-a-ring) obtains the pairing links from number-conserving collisions involving a populated pump. Replacing the pump by a coherent amplitude is a controlled approximation, not a violation of atom-number conservation. Pump replenishment, a phase reference, selective ports and unwanted resonances remain physical requirements. A stable linear drift matrix alone does not verify all of them.

Projecting a frequency-dependent scatterer onto selected finite packets introduces unused positive temporal modes. Their coupling matrix must be retained in the commutator equation. Consequently a very small averaged reverse amplitude is not sufficient to substitute that pulse into the closed two-port theorem. The [finite-bandwidth account](../science/finite_bandwidth.md) supplies the corrected channel and a finite-energy entanglement witness.

Finally, ebits per normalized use are not ebits per second. Bandwidth, orthogonal-mode throughput, collection loss, and microscopic errors must be controlled relative to the shrinking entanglement margin. The [interpretation](../science/interpretation.md) connects those requirements to calibration.

## 8. What the anchor does not replace

The [primary-source account](../references/RELATED_WORK.md) attributes separability, distillability, hashing, channel bounds and environmental-feedback methods. The collection theorem, scattering-variable reduction, stable family, conditional-state calculations and pulse bookkeeping are developed in the canonical project pages. The [verification suite](../verification/README.md) audits finite instances and algebra; it is not a replacement for the general proofs or an independent experimental validation.

Continue with the [milestone map](MILESTONES.md) or return to the [learning overview](README.md).

# What isolation does and does not certify

Classical isolation specifies how a coherent probe propagates in opposite
directions. The quantum communication resource also depends on spontaneous
noise and access to outgoing fields. This distinction is particularly useful
for atomtronic devices, where a pumped condensate can mix annihilation and
creation operators and a laboratory loss port can hide an additional
positive-signature channel.

## 1. The physical question answered

The [model](model.md) contains exactly two positive input and output ports,
an arbitrary number of conjugated idler ports, and vacuum auxiliary inputs.
The receiver obtains one positive output. The sender may collect the other
output through a specified loss before processing it. The two parties can
use arbitrary local quantum operations and public classical communication.

Within that model, complete commutator accounting turns measured reverse
transmission into a receiver-noise restriction. Discarding the return gives
a reduced channel with assisted capacities at most quadratic in small
reverse power. Collecting the return changes the resource. The
[exact boundary](collection_boundary.md) determines whether *any* protocol
can distribute entanglement, and the [rate calculation](communication_rates.md)
establishes a linear-order two-way quantum capacity for one stable family
under ideal collection.

The zero-capacity result concerns the channel, so changing the code from a
Gaussian code to an arbitrary squeezed, non-Gaussian, collective or adaptive
code does not evade it. The positive-side protocol uses a Gaussian probe and
measurement to create an entangled resource, followed by unrestricted
distillation. Gaussian-only distillation is not claimed.

## 2. Distinctions needed for an experimental comparison

| Observation or device property | What it establishes | Additional information needed here |
|---|---|---|
| Unequal forward and reverse coherent transmission | A directional linear response at the calibrated operating point | Complete mode count, flux normalization, spontaneous noise and output access |
| Unequal critical currents under opposite bias | A nonlinear transport asymmetry | A common stationary background and its linear scattering matrix |
| A two-port measured submatrix | Response between monitored channels | Couplings to unmonitored positive baths and idler ports |
| Entangled outgoing signal and idler | A propagating output-entanglement resource | Whether the receiver in the communication task actually accesses that idler |
| No entanglement with one chosen Gaussian receiver | Failure of that particular receiver | An all-protocol channel converse such as the instrument construction |
| Positive capacity at one spectral frequency | A statement about the corresponding ideal mode | A finite wave packet, its unused temporal modes and the available bandwidth |

In spatial Bogoliubov scattering, a negative-norm branch is a creation input
in the canonical map. Its presence does not license dropping a
counterpropagating dispersive positive branch. In a driven-mode realization,
the conjugated sector can be an ordinary positive-energy atomic mode powered
by a pump. The operational channel depends on the canonical input-output
assignment, rather than the sign of an unshifted laboratory energy alone.

The constructed unity-gain family is not impedance matched: at perfect
reverse isolation both positive reflection powers equal two. The example
therefore establishes a stable directional channel with its stated noise
and access properties, not a matched passive isolator.

## 3. Calibrating the boundary

In the vacuum two-positive-port class, measure at the same operating point
the forward power $`G`$, reverse power $`R`$, receiver vacuum-output
occupation $`N`$, and collection transmissivity $`\eta`$. The exact test is

```math
c=N-G\ge0,
\qquad (1-\eta)c-\eta R\ge0.
```

Both inequalities are needed. Collection refers to the fraction of the
return field available to the sender before usable processing; the quantum
efficiency of an optional downstream detector is not automatically the same
resource constraint. Mode overlap, propagation and fixed coupling losses
can contribute to this collection loss when their unused outputs are
inaccessible.

For gauge-invariant thermal auxiliaries, measure the complete complex
normal-occupation matrix $`\mathsf K`$ of the two positive outputs with the
signal in vacuum. The correct test is

```math
M=\operatorname{diag}(1,0)-tt^\dagger+L\mathsf K L\ge0,
\qquad L=\operatorname{diag}(\sqrt\eta,1),\quad t=LA_{:1}.
```

Thermal source noise and output correlations enter this matrix. Three scalar
power measurements alone do not establish the thermal threshold. The
[thermal proof](collection_boundary.md#6-gauge-invariant-gaussian-noise)
states the auxiliary independence and covariance assumptions explicitly.

### Finite calibration margins

Suppose the effective Gaussian model is calibrated as $`t,C`$, where
$`C=L\mathsf K L`$, with operator-norm errors
$`\|\Delta t\|\le\epsilon_t`$ and
$`\|\Delta C\|\le\epsilon_C`$. Then

```math
\|\Delta M\|\le
2\|t\|\epsilon_t+\epsilon_t^2+\epsilon_C.
```

Weyl's inequality gives a direct error margin: a nominal smallest eigenvalue
larger than this bound certifies the zero region for all consistent Gaussian
channels; one smaller than its negative certifies the positive region. If
the uncertainty interval crosses zero, the calibration does not decide the
side. This is a deterministic error bound, not a statistical confidence
interval without a measurement-error model.

At ideal collection in the stable small-$`R`$ family, the negative
eigenvalue approaches zero with order $`R`$. Thus near-perfect isolation
requires increasingly accurate noise, mode and collection characterization.
This sensitivity is consistent with the collection-loss tolerance
$`1-\eta_{\rm crit}=R/(1-\sqrt R)^2`$.

## 4. Atomic resources and the order of limits

The [atomic construction](stable_atomic_model.md) begins with
number-conserving collisions in ring modes and independently phased drives.
A populated pump and its coherent reference produce two pair-creation links;
a Bragg conversion link closes the loop. Linearization, mode selection and
Markov ports yield a three-mode effective Hamiltonian with a uniform
stability margin. The constituent control operations have experimental
precedent, cited there. Their combination and the complete communication
experiment are a proposed realization, not a reported experiment.

The resources remain distinct:

| Resource | Accounting in this model |
|---|---|
| Signal probe | Mean occupation one suffices for the explicit linear-order lower bound |
| Corrected receiver state | Mean occupation one in that protocol, uniformly near isolation |
| Pump population and replenishment | The condensate supplies atoms and the external drives supply excitation energy; pump depletion must be controlled |
| Coherent atomic references | Required for the quadrature measurement and conditional displacement; not supplied by a Fock-state condensate without further reference resources |
| Phase and frequency control | Sets loop interference and resolves unwanted collisions and Bragg transitions |
| Output collection | Must approach unity as reverse power decreases to retain positive capacity in this family |
| Bandwidth and duration | Determine independent-mode throughput and total emitted flux |

At exact reverse isolation the two positive vacuum spectral occupations
sum to three, the idler occupation is three, and the three physical outputs
sum to six. These are resonant occupations per normalized frequency mode.
They are not six atoms per second or the integrated output flux. The atomic
page evaluates the frequency integral separately.

The effective linear model permits the mathematical limit $`R\to0`$ while
remaining stable. A microscopic implementation with a fixed finite pump,
fixed sideband separation and fixed detection losses does not thereby
inherit the ideal asymptotic rate law uniformly. For each finite target
$`R>0`$, residual nonlinear and mode-selection errors must lie below the
entanglement or coherent-information margin being claimed. An exact
all-input converse for the Gaussian model cannot automatically be applied to
a non-Gaussian microscopic channel on the basis of second moments alone.

## 5. Which changed resources alter the conclusion?

An additional positive bath changes the commutator equation to
$`AA^\dagger+CC^\dagger-BB^\dagger=I`$. The corrected receiver-noise
floor depends on $`R+(CC^\dagger)_{11}`$. A passive three-port circulator
gives a simple zero-noise counterexample to applying the two-port bound
outside its domain; the explicit matrices appear in
[Scattering and noise](scattering_noise.md#4-additional-positive-auxiliary-inputs).

Giving the receiver an idler output changes the bipartition and the channel.
Giving the receiver control of the second input allows an interactive
quantum communication resource absent from the model. A phase-sensitive
scattering map, a different engineered auxiliary covariance, or memory
between uses also calls for a new channel analysis. These are meaningful
extensions, not consequences established by the present theorem.

Secret-key capacity additionally depends on which inaccessible systems a
purifying adversary possesses. The zero-key proof uses an explicit
local/public simulation and the full untrusted complement. Logarithmic
negativity supplies the linear-order **quantum-capacity** upper bound; it
does not supply a secret-key upper bound in the positive region.

## 6. Relation to existing results

Environmental heterodyne and feedforward recovery, quantum-limited amplifier
noise, Gaussian separability, and bosonic capacity bounds are established
methods. The [related-work account](../references/RELATED_WORK.md) gives
direct comparisons and a parameter-level embedding of the earlier thermal
beam-splitter recovery protocol. It makes no priority claim for a scalar
amplifier-noise inequality whose closest noise-synthesis papers have not
been fully compared.

The contribution developed here is the exact all-protocol access boundary
in calibrated scattering variables and the matched linear-order quantum
rate for the explicit stable ideal-collection family, together with the
discarded-return upper envelope and physical resource accounting. The
proofs and independent finite checks are public in the
[science](model.md) and [verification](../verification/README.md) routes.

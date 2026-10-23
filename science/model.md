# Directional matter waves and the accessible quantum channel

A directional circuit is usually characterized by its response to a classical
probe. Quantum communication requires additional information: the spontaneous
noise, the complete set of scattering modes, and which outgoing modes each
party can use. This account relates those quantities for linear atomtronic
circuits and identifies an exact boundary for entanglement distribution.

The main result concerns a sender who may collect the reflected field and a
receiver who obtains one transmitted field. The same device defines a different
channel if the reflection is discarded. The distinction changes both the
zero-capacity boundary and the attainable rate near perfect reverse isolation.

## 1. Canonical scattering convention

At a fixed frequency, write the complete positive-signature output block as

```math
\boldsymbol b=A\boldsymbol a+B\boldsymbol e^\dagger,
\qquad AA^\dagger-BB^\dagger=I_2.
```

Here $`\boldsymbol a=(a_1,a_2)^T`$ and $`\boldsymbol b=(b_1,b_2)^T`$
contain exactly two positive-signature signal ports. The $`q`$ components of
$`\boldsymbol e`$ are independent idler inputs. The minus sign records the
commutator of creation operators in the Nambu representation. In a pumped
atomic module the idler is an ordinary atomic mode appearing as a creation
operator in this block; it need not have negative laboratory energy.

For spatial Bogoliubov scattering, use the full flux-normalized basis at the
same stationary background. Include dispersive branches, evanescent modes in
matching conditions, and every propagating or dissipative channel. Comparing
critical currents of two separately biased nonlinear backgrounds does not
measure the matrix $`A`$ above.

The central vacuum model assumes that $`a_2`$ and all idlers are independent
vacuum inputs. The sender controls $`a_1`$. Define

```math
G=|A_{21}|^2,\qquad R=|A_{12}|^2,\qquad
n_1=(BB^\dagger)_{11},\qquad N=(BB^\dagger)_{22}.
```

$`G`$ and $`R`$ are forward and reverse power transmission, respectively.
$`n_1`$ and $`N`$ are the spontaneous output occupations when the signal is
also vacuum. They are quasiparticle occupations per normalized mode, rather
than raw atom numbers or input-referred half-quantum noise. A stationary
spectral occupation contributes a flux through an integral
$`\int n(\omega)\,d\omega/(2\pi)`$.

We use $`[q,p]=i`$ and vacuum covariance $`I_2/2`$. All rates are in bits or
ebits per independent channel use. A rate per second additionally requires a
specified bandwidth and mode-production rate.

## 2. Two operational interfaces

| Interface | Sender receives after scattering | Receiver receives | Inaccessible outputs |
|---|---|---|---|
| Reduced forward channel $`\Phi`$ | Nothing from the scatterer | $`b_2`$ | Reflection and every idler |
| Collected-return channel $`\Psi_\eta`$ | $`z=\sqrt\eta\,b_1+\sqrt{1-\eta}\,v`$ | $`b_2`$ | Lost reflection and every idler |

The loss input $`v`$ is independent vacuum and $`0\le\eta\le1`$.
**Collection loss occurs before any usable processing by the sender.** If the
sender instead possesses the complete reflected field and merely chooses an
inefficient detector, that detector does not impose the all-protocol converse.

The sender can retain an arbitrary reference and quantum memory. The two
parties may perform arbitrary local operations, including non-Gaussian ones,
with unlimited public classical communication. Independent channel uses may
be connected adaptively. Initially they share no entanglement or secret key.
The second scattering input remains a fixed auxiliary state; the receiver
does not independently encode into it.

$`Q`$ denotes unassisted quantum capacity of the reduced channel. $`Q_2`$
denotes quantum capacity with two-way classical communication, equivalently
the optimal entanglement-distribution rate with that communication. $`K`$
denotes secret-key capacity when the inaccessible environment is untrusted
and may be held by a purifying adversary. The key statements require that
cryptographic assumption; the entanglement statements do not.

The collected-return map has one input and two outputs held by different
parties. A zero-capacity map here can retain quantum information locally at
the sender. It is therefore described as a channel with a local-instrument
simulation across the sender/receiver cut, not as an ordinary
entanglement-breaking channel into its combined output.

## 3. Principal statements and their domains

### Exact collection boundary

Let $`c=N-G=|A_{22}|^2-1`$. For the vacuum model,

```math
Q_2(\Psi_\eta)=K(\Psi_\eta)=0
\quad\Longleftrightarrow\quad
c\ge0\ \text{and}\ (1-\eta)c\ge\eta R.
```

The equality boundary belongs to the zero-capacity region. Below it the full
channel has a sender-local instrument followed by receiver-state preparation.
Outside it, heterodyne of the collected return and a displacement at the
receiver yield a non-entanglement-breaking channel. Any positive-energy
two-mode squeezed probe then supplies distillable entanglement. The
[collection-boundary proof](collection_boundary.md) treats arbitrary input
states, adaptive protocols, degenerate cases, and a thermal-noise extension.

### Reverse power bounds the reduced channel

The canonical relation implies

```math
N\ge G-R.
```

For the reduced interface, $`R\le1/2`$ forces $`Q(\Phi)=0`$.
For $`0\le R\le\min(G,1)`$, an established Gaussian capacity bound gives

```math
Q_2(\Phi)\le K(\Phi)\le F(G,R),
\qquad F(G,R)=\frac{R^2}{2G\ln2}+O(R^3)
```

at fixed $`G>0`$. The exact function and proof are in
[Communication rates](communication_rates.md). This is an upper bound, not
an asserted exact reduced-channel capacity.

### Attained rate order with ideal return collection

A [stable family](stable_atomic_model.md) with $`G=1`$ and variable $`R`$
has, at $`\eta=1`$,

```math
Q_2(\Psi_1)=\Theta(R),\qquad R\downarrow0.
```

The lower bound uses a probe of mean occupation one and has bounded corrected
receiver occupation. The upper bound permits arbitrary encodings, memories
and local processing. Their constants do not coincide; only the linear order
is matched. This statement is a quantum-capacity result, not a matching
secret-key-capacity formula. For the same family the reduced channel is
entanglement breaking throughout $`0\le R\le1/4`$.

### A sharp positive-output noise bound

Let $`d=\sqrt G-\sqrt R\ge0`$, with $`\sqrt R\le1`$. Then

```math
n_1+N\ge d(d+2),
```

and an explicit canonical matrix attains equality. This sum covers the two
positive outputs. The idler output has additional occupation and must be
included when counting all emitted atoms or pump depletion. The bound,
noise-allocation tradeoffs, and extra-positive-port correction are proved in
[Scattering and noise](scattering_noise.md). No priority claim for a new
general amplifier-noise principle is made; see
[Related work](../references/RELATED_WORK.md).

## 4. Physical scope

The exact results concern an effective linear stationary channel. The
[atomic model](stable_atomic_model.md) derives its links from number-conserving
driven collisions and a mode-conversion drive in a ring, followed by a
controlled undepleted-pump and resonant-mode approximation. Pump atoms,
coherent phase references, thermal occupations and unwanted modes remain
physical resources. A finite-pump condensate is not claimed to realize an
exact Gaussian channel at arbitrarily small $`R`$.

[Finite bandwidth](finite_bandwidth.md) explains when spectral results imply
statements about actual wave packets. A perfect-isolation point at one
frequency does not by itself establish a broadband quantum no-go.

Extra positive ports can evade the two-port obstruction. Access to an idler
at the receiver can also change the result, including at exact reverse
isolation. Nonclassical environment engineering, a phase-sensitive scattering
map, uncontrolled memory, and a receiver-controlled second input are different
models. Phase-sensitive signal encodings, including squeezed inputs, are
already covered by the arbitrary-input converse for the stated channel.
These qualifications identify the channel being tested; they are not small
corrections to an unrestricted isolation theorem.

## Reading route

Continue with the [exact collection boundary](collection_boundary.md), then
the [communication-rate consequences](communication_rates.md). The
[scattering inequalities](scattering_noise.md) explain the canonical
constraint. The [atomic construction](stable_atomic_model.md),
[finite-bandwidth account](finite_bandwidth.md), and
[physical interpretation](interpretation.md) connect the results to a
calibrated device. [Verification](../verification/README.md) separates
reproducible finite checks from the analytical proofs.

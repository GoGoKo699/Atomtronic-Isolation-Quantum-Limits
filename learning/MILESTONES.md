# Atomtronic isolation: 30 understanding milestones

The single educational anchor is **Weedbrook et al., _Gaussian Quantum Information_ (2012)**. Review section pointers use [arXiv:1110.3234v1](https://arxiv.org/abs/1110.3234v1), as specified in the [source-to-project bridge](WEEDBROOK_BRIDGE.md). Research-level dependencies remain in the canonical science and [related work](../references/RELATED_WORK.md).

The map has **13 background/preliminaries milestones** and **17 narrative/innovation milestones**. The background builds from a single mode to a complete communication resource. The narrative builds from the scattering constraint to the theorem, rates and physical interpretation. The allocation reflects the need to connect Gaussian information theory with atomic scattering; it is not a personalized syllabus. The targets describe global understanding, not every technical lemma.

## Background and preliminaries

### M01 — Canonical atomic modes

**Phase:** Background and preliminaries.

**Central question:** What does one normalized atomic mode represent in the communication experiment?

**Understanding target:** Distinguish a mode's occupation from an atom flux, identify the signal and idler operators, and explain the creation-operator commutator sign without assigning negative laboratory atom number.

**Dependencies:** None.

**Story role:** Establish the local physical objects before defining the circuit.

**Conceptual connection:** A canonical input-output assignment determines which fluctuations must be retained.

**Sources:** Review II.A; [model §1](../science/model.md#1-canonical-scattering-convention); [bridge §3](WEEDBROOK_BRIDGE.md#3-from-an-atomic-scattering-experiment-to-a-channel).

### M02 — Quadrature conventions

**Phase:** Background and preliminaries.

**Central question:** How can the same vacuum have covariance one in the review and one half here?

**Understanding target:** Convert quadratures, covariance matrices and symplectic eigenvalues while leaving occupation and transmission power unchanged; account for quadrature ordering separately.

**Dependencies:** M01.

**Story role:** Fix the normalization used by every later threshold.

**Conceptual connection:** A unit conversion cannot change whether a physical state is entangled.

**Sources:** Review I.D and II.A.1; [bridge §2](WEEDBROOK_BRIDGE.md#2-translate-conventions-before-applying-a-formula).

### M03 — Gaussian covariance

**Phase:** Background and preliminaries.

**Central question:** Which information is contained in a covariance matrix, and when is it a complete state description?

**Understanding target:** Identify local variances and cross-correlations, check the uncertainty condition, and distinguish a Gaussian state specified by moments from an arbitrary state with the same moments.

**Dependencies:** M02.

**Story role:** Turn local observables into a usable description of several modes.

**Conceptual connection:** Gaussian calculations are exact for the selected model, but second moments alone do not certify a general microscopic channel.

**Sources:** Review II.A.1; [collection covariance construction](../science/collection_boundary.md#3-gaussian-complete-positivity-calculation); [interpretation §4](../science/interpretation.md#4-atomic-resources-and-the-order-of-limits).

### M04 — Symplectic transformations

**Phase:** Background and preliminaries.

**Central question:** What constrains a linear transformation to preserve quantum commutators?

**Understanding target:** Relate a real symplectic transformation to a Bogoliubov input-output block and explain why conjugated idlers enter with the opposite sign.

**Dependencies:** M01, M03.

**Story role:** Connect individual modes to a physical linear network.

**Conceptual connection:** Commutator preservation is the origin of the noise restriction, not a property inferred from a classical transmission plot.

**Sources:** Review II.A.2 and II.C.2; [model §1](../science/model.md#1-canonical-scattering-convention); [scattering §1](../science/scattering_noise.md#1-receiver-noise-floor).

### M05 — Squeezing and references

**Phase:** Background and preliminaries.

**Central question:** How can the sender test entanglement transmission without initially sharing entanglement with the receiver?

**Understanding target:** Describe a locally prepared two-mode squeezed probe with one retained reference and one transmitted mode; distinguish that reference mode from a phase reference used to implement quadrature operations.

**Dependencies:** M02, M04.

**Story role:** Supply the input resource for the constructive argument.

**Conceptual connection:** Probe entanglement starts entirely in the sender's laboratory and is not a free preshared communication resource.

**Sources:** Review II.B.3, 7; [finite-energy protocol](../science/communication_rates.md#2-a-finite-energy-protocol-with-ideal-reflection-collection); [atomic references](../science/stable_atomic_model.md#5-port-selectivity-and-numberphase-references).

### M06 — Heterodyne measurements

**Phase:** Background and preliminaries.

**Central question:** What information does heterodyne measurement of the return provide, and what noise accompanies it?

**Understanding target:** Explain the complex measurement outcome, its vacuum contribution and its use in a conditional displacement; distinguish collection loss from an optional detector's inefficiency.

**Dependencies:** M02, M03, M05.

**Story role:** Introduce the actual local operation used for recovery.

**Conceptual connection:** Simultaneously measuring two quadratures is not noiseless observation of a classical field.

**Sources:** Review II.E.1–2; [collection §5](../science/collection_boundary.md#5-optimal-monitoring-and-finite-energy-achievability); [model §2](../science/model.md#2-two-operational-interfaces).

### M07 — Conditional Gaussian states

**Phase:** Background and preliminaries.

**Central question:** Why can all heterodyne outcomes lead to the same centered resource state?

**Understanding target:** Interpret the conditional covariance as a Schur complement, identify the measurement-noise term, and explain why removing conditional means is deterministic rather than postselection.

**Dependencies:** M03, M06.

**Story role:** Connect measurement information to the quantum state that remains.

**Conceptual connection:** Conditioning changes correlations while classical feedforward removes the outcome-dependent displacement.

**Sources:** Review II.E.3, Eq. (65); [bridge §6](WEEDBROOK_BRIDGE.md#6-from-gaussian-conditioning-to-a-finite-energy-rate); [finite-energy protocol](../science/communication_rates.md#2-a-finite-energy-protocol-with-ideal-reflection-collection).

### M08 — Partial transpose

**Phase:** Background and preliminaries.

**Central question:** What does a partial-transpose covariance violation establish, and what does it not establish by itself?

**Understanding target:** Identify the receiver momentum flip, the project-unit threshold one half, the Gaussian one-versus-many separability condition, and the distinction between PPT and zero secret key.

**Dependencies:** M03, M04.

**Story role:** Provide the entanglement test while exposing its logical scope.

**Conceptual connection:** The partition of modes matters as much as the covariance spectrum.

**Sources:** Review II.C.1 and II.D.1–2; [faithful-state argument](../science/collection_boundary.md#41-a-faithful-finite-energy-state); [secret-key argument](../science/collection_boundary.md#44-secret-key-requires-the-stronger-simulation).

### M09 — Gaussian channels

**Phase:** Background and preliminaries.

**Central question:** How does tracing inaccessible outputs turn a scattering matrix into a noisy channel?

**Understanding target:** Read the gain and noise matrices in the covariance map, recover the vacuum-output occupation, and distinguish a channel's complete positivity from one input state's physicality.

**Dependencies:** M03, M04.

**Story role:** Move from states and transformations to an input-output resource.

**Conceptual connection:** The same device defines different channels under different output-access assignments.

**Sources:** Review V.A–B; [model §2](../science/model.md#2-two-operational-interfaces); [reduced channel](../science/communication_rates.md#1-the-reduced-forward-channel).

### M10 — Entanglement breaking

**Phase:** Background and preliminaries.

**Central question:** Why does a measure-and-prepare description rule out entanglement transmission even for an entangled input reference?

**Understanding target:** Explain the reduced-channel condition $`N\ge G`$ and distinguish ordinary entanglement breaking from a sender-return channel that retains local quantum information while remaining local across the two laboratories.

**Dependencies:** M08, M09.

**Story role:** Establish the operational meaning of a zero-communication channel.

**Conceptual connection:** Losing transmitted entanglement is different from destroying all quantum information everywhere.

**Sources:** Review V.A–B, F; [model §2](../science/model.md#2-two-operational-interfaces); [collection §4](../science/collection_boundary.md#4-from-a-gaussian-test-to-an-arbitrary-input-converse).

### M11 — Communication capacities

**Phase:** Background and preliminaries.

**Central question:** Which task is measured by unassisted quantum capacity, two-way quantum capacity, or secret-key capacity?

**Understanding target:** Distinguish $`Q,Q_2,K`$, specify the classical communication and adversary assumptions, and separate zero-versus-positive classification, an achievable rate, and an upper bound.

**Dependencies:** M09, M10.

**Story role:** Define what a successful communication claim must prove.

**Conceptual connection:** A positive entanglement witness and an exact capacity value are different achievements.

**Sources:** Review V.D, F; [model §2–3](../science/model.md#2-two-operational-interfaces); [rate dependencies](../science/communication_rates.md#5-dependencies-and-limits).

### M12 — Atomic pumping

**Phase:** Background and preliminaries.

**Central question:** How can an atom-number-conserving system produce effective pair-creation terms?

**Understanding target:** Track atoms transferred from the pump, energy supplied by drives, and the coherent-amplitude approximation that yields the quadratic Hamiltonian; distinguish this approximation from an exact finite-pump description.

**Dependencies:** M01, M04, M05.

**Story role:** Connect the Gaussian machinery to its atomic setting.

**Conceptual connection:** The effective idler sector requires physical pumps and references, not an uncharged abstract noise source.

**Sources:** Review II.A.2 for quadratic transformations; [atomic model §§1, 3](../science/stable_atomic_model.md#1-hamiltonian-and-the-physical-channels); [bridge §7](WEEDBROOK_BRIDGE.md#7-the-atomic-and-finite-pulse-bridge). The microscopic construction is supplied locally.

### M13 — Accessible-mode accounting

**Phase:** Background and preliminaries.

**Central question:** What complete experiment is specified before applying the collection theorem?

**Understanding target:** Assign every input, output, auxiliary, retained memory and public message to its owner; state the two-positive-port, vacuum, memoryless, collection-before-processing and untrusted-environment assumptions.

**Dependencies:** M06, M09, M11, M12.

**Story role:** Integrate the background into one fully specified operational problem.

**Conceptual connection:** Resource ownership determines the communication cut on which the theorem acts.

**Sources:** Review V.A, F; [model](../science/model.md); [collection §1](../science/collection_boundary.md#1-resource-and-notation).

## Narrative and innovation

### M14 — Reverse-power noise floor

**Phase:** Narrative and innovation.

**Central question:** Why does suppressing reverse transmission constrain spontaneous receiver noise in this particular model?

**Understanding target:** Follow the square-matrix singular-value argument from commutator preservation to $`N\ge G-R`$, and identify why a selected submatrix of a larger device does not satisfy its premise.

**Dependencies:** M04, M13.

**Story role:** Derive the first local constraint behind the communication limit.

**Conceptual connection:** The restriction uses complete mode accounting, not nonreciprocity alone.

**Sources:** Review II.A.2 as background; [scattering §1](../science/scattering_noise.md#1-receiver-noise-floor).

### M15 — Noise allocation

**Phase:** Narrative and innovation.

**Central question:** Is minimizing receiver noise the same optimization as minimizing total positive-output noise?

**Understanding target:** Compare the two explicit saturating families, recognize the source-noise divergence of the receiver-optimal family near isolation, and include the idler when counting all emitted particles.

**Dependencies:** M14.

**Story role:** Select a physically informative family rather than treating all noise minima as interchangeable.

**Conceptual connection:** A gain in one output's performance can move the cost into another output.

**Sources:** Review II.B.1 for occupation conventions; [scattering §§2–3](../science/scattering_noise.md#2-minimum-summed-occupation-in-the-positive-outputs).

### M16 — Discarded-return channel

**Phase:** Narrative and innovation.

**Central question:** What can be concluded about communication when the reflection is inaccessible?

**Understanding target:** Connect the amplifier-then-loss factorization to the zero unassisted-capacity condition, and distinguish the general quadratic assisted-capacity upper envelope from this stable family's zero reduced capacity.

**Dependencies:** M10, M11, M14.

**Story role:** Establish the precisely matched baseline for collection-assisted communication.

**Conceptual connection:** A universal upper envelope is not an achieved rate of the example device.

**Sources:** Review V.B, D, F; [communication rates §1](../science/communication_rates.md#1-the-reduced-forward-channel).

### M17 — Collection covariance matrix

**Phase:** Narrative and innovation.

**Central question:** How do measured scattering quantities enter the full-channel positivity test?

**Understanding target:** Construct $`t,C,M`$, identify $`c=N-G`$ and the determinant $`(1-\eta)c-\eta R`$, and locate the equality side without using an undefined threshold ratio at a degenerate point.

**Dependencies:** M03, M06, M13, M14.

**Story role:** Reduce the accessible-channel question to a small matrix with calibrated entries.

**Conceptual connection:** Forward power alone does not determine the sign of the entanglement margin.

**Sources:** Review V.A for the CP formalism; [collection §3](../science/collection_boundary.md#3-gaussian-complete-positivity-calculation); [worked example](WEEDBROOK_BRIDGE.md#4-one-worked-threshold-example).

### M18 — All-input local simulation

**Phase:** Narrative and innovation.

**Central question:** What closes the gap between a Gaussian probe calculation and an arbitrary-protocol impossibility theorem?

**Understanding target:** Explain the faithful finite-energy reference, Gaussian one-versus-many separability, the bounded isometric instrument construction, and extension from matrix units to arbitrary trace-class inputs; identify the additional public-environment reasoning needed for key.

**Dependencies:** M08, M10, M17.

**Story role:** Supply the converse's essential logical step.

**Conceptual connection:** A local simulation of each channel use survives arbitrary memories, non-Gaussian processing and adaptive composition.

**Sources:** Review II.D.1 as foundation; [collection §4](../science/collection_boundary.md#4-from-a-gaussian-test-to-an-arbitrary-input-converse); primary theorem attributions there.

### M19 — Heterodyne achievability

**Phase:** Narrative and innovation.

**Central question:** Why does one monitoring protocol reach every point outside the forbidden region?

**Understanding target:** Relate optimal feedforward to $`-\det M/M_{11}`$, use the finite-energy NPT witness to establish positivity, and distinguish existence of a protocol from an optimal positive-capacity value.

**Dependencies:** M06, M07, M17, M18.

**Story role:** Match the converse with a construction on its entire complementary region.

**Conceptual connection:** The same quadratic form governs both the impossibility test and the feedback optimizer.

**Sources:** Review II.E.2–3 and V.F; [collection §5](../science/collection_boundary.md#5-optimal-monitoring-and-finite-energy-achievability). General non-Gaussian distillation remains allowed.

### M20 — Thermal auxiliaries

**Phase:** Narrative and innovation.

**Central question:** Why are forward power, reverse power and receiver occupation insufficient for the thermal version of the theorem?

**Understanding target:** Replace the vacuum noise by the full gauge-invariant normal-occupation matrix, retain complex cross-correlations, and explain positive-semidefinite enlargement of the zero region and the singular-matrix corner.

**Dependencies:** M17, M18, M19.

**Story role:** Extend the calibrated criterion without discarding its assumptions.

**Conceptual connection:** Thermal noise changes the matrix test, not just a scalar noise label.

**Sources:** Review II.B.1 and V.A–B; [collection §6](../science/collection_boundary.md#6-gauge-invariant-gaussian-noise).

### M21 — Finite-energy rate

**Phase:** Narrative and innovation.

**Central question:** How can collection-assisted communication avoid the large output energy of raw cancellation feedforward?

**Understanding target:** Follow conditioning and local centering of a finite-energy probe, identify the mean-one receiver state, and connect its coherent information to an achievable distillation rate with a justified finite-output truncation.

**Dependencies:** M05, M07, M11, M19.

**Story role:** Turn qualitative positivity into a bounded-signal-energy rate construction.

**Conceptual connection:** Distilling the conditional bipartite state is a different protocol from realizing a high-gain corrected channel.

**Sources:** Review II.C.1, II.E.3 and V.D, F; [communication rates §2](../science/communication_rates.md#2-a-finite-energy-protocol-with-ideal-reflection-collection).

### M22 — Full-channel converse

**Phase:** Narrative and innovation.

**Central question:** How can a rate upper bound cover arbitrary encodings without assuming uniform convergence at unbounded energy?

**Understanding target:** Explain local displacement covariance, finite-protocol teleportation simulation, the target-overlap/logarithmic-negativity inequality, and the order of the simulation and coding limits; keep the quantum-capacity and key claims separate.

**Dependencies:** M08, M09, M11, M18.

**Story role:** Bound the complete accessible resource rather than a chosen receiver.

**Conceptual connection:** Pointwise simulation for each fixed protocol is not an unconstrained diamond-norm statement.

**Sources:** Review II.D.2 and IV.A; [communication rates §3](../science/communication_rates.md#3-a-matching-linear-order-upper-bound-on-the-full-channel).

### M23 — Rate scaling comparison

**Phase:** Narrative and innovation.

**Central question:** Exactly which comparison establishes the linear-order advantage of collecting the return?

**Understanding target:** Combine the lower and upper bounds to identify $`\Theta(R)`$ for the ideal-collection family; contrast that with the reduced-channel quadratic upper envelope and explain why unequal constants leave the exact capacity open.

**Dependencies:** M16, M21, M22.

**Story role:** Integrate the information-theoretic contribution before interpreting its hardware realization.

**Conceptual connection:** Changing accessible outputs changes the operational resource, while the forward and reverse powers remain matched.

**Sources:** Review V.D, F for capacity meanings; [communication rates §§3–4](../science/communication_rates.md#3-a-matching-linear-order-upper-bound-on-the-full-channel).

### M24 — Stable three-mode dynamics

**Phase:** Narrative and innovation.

**Central question:** Can perfect reverse isolation be approached without bringing the effective device to parametric instability?

**Understanding target:** Identify the conversion and pairing links, connect the resolvent to resonant scattering, and explain the uniform drift-decay margin and bounded couplings of the explicit family.

**Dependencies:** M12, M14, M15.

**Story role:** Attach the canonical construction to a controlled dynamical model.

**Conceptual connection:** Stable drift is an independent requirement from commutator preservation or a favorable capacity bound.

**Sources:** Review II.A.2 for quadratic evolution; [atomic model §§1–2](../science/stable_atomic_model.md#2-an-exact-stable-family-with-unity-forward-power).

### M25 — Driven ring collisions

**Phase:** Narrative and innovation.

**Central question:** Which microscopic processes produce the three effective links and their interference phase?

**Understanding target:** Track the chosen ring modes, the two number-conserving pump collisions and the conversion drive; explain frequency/angular-momentum closure and why the common pump phase cancels from the loop phase.

**Dependencies:** M12, M24.

**Story role:** Connect the effective model to a specific microscopic construction.

**Conceptual connection:** Selecting a resonant term does not automatically remove every unwanted collision or sideband.

**Sources:** Review II.A.2 supplies only the Gaussian-language foundation; [atomic model §§3–4](../science/stable_atomic_model.md#3-a-number-conserving-collision-model-in-a-ring) supplies the microscopic derivation.

### M26 — Pump and reference resources

**Phase:** Narrative and innovation.

**Central question:** Which resources remain necessary even though the signal probe and corrected receiver occupations stay bounded?

**Understanding target:** Distinguish pump population, replenishment, coherent references, port selectivity and spectral filtering; separate resonant occupation, intracavity population and frequency-integrated atom flux.

**Dependencies:** M05, M24, M25.

**Story role:** Expose the complete physical cost behind the useful rate.

**Conceptual connection:** Bounded probe energy does not make the driven atomic apparatus resource free.

**Sources:** Review II.B.2–3 and II.E.1 for reference-dependent operations; [atomic model §§5–6](../science/stable_atomic_model.md#5-port-selectivity-and-numberphase-references); [interpretation §4](../science/interpretation.md#4-atomic-resources-and-the-order-of-limits).

### M27 — Finite packet projection

**Phase:** Narrative and innovation.

**Central question:** Why does selecting one finite pulse per port usually destroy the closed two-positive-mode description?

**Understanding target:** Identify the positive temporal auxiliary modes created by projection, retain their Gram matrix in the commutator, and distinguish averaged reverse amplitude from the corrected reverse resource in the reduced-channel bound.

**Dependencies:** M03, M04, M13, M24.

**Story role:** Replace a monochromatic idealization by a complete packet channel.

**Conceptual connection:** Unmeasured temporal modes cannot be erased by redefining the selected pulse.

**Sources:** Review V.A as channel background; [finite bandwidth §2](../science/finite_bandwidth.md#2-exact-accounting-for-selected-packet-modes); [additional-port constraint](../science/scattering_noise.md#4-additional-positive-auxiliary-inputs).

### M28 — Bandwidth and throughput

**Phase:** Narrative and innovation.

**Central question:** When does a spectral entanglement statement imply a useful finite-duration communication resource?

**Understanding target:** Separate the whole-band zero theorem from persistence of a strict finite-packet witness, identify the narrowing/error hierarchy near isolation, and explain why independent-mode throughput is needed for a rate per second.

**Dependencies:** M11, M23, M27.

**Story role:** Connect per-mode information theory to usable temporal resources.

**Conceptual connection:** A cancellation at a single frequency is neither broadband impossibility nor a throughput estimate.

**Sources:** Review V.D, F for per-use capacities; [finite bandwidth §§1, 4–5](../science/finite_bandwidth.md#1-a-whole-band-zero-capacity-statement).

### M29 — Calibration robustness

**Phase:** Narrative and innovation.

**Central question:** What can finite-accuracy measurements certify about the exact boundary?

**Understanding target:** Compare the smallest eigenvalue of the calibrated matrix with the operator-norm perturbation bound, recognize an undecided uncertainty interval, and distinguish a deterministic error margin from a statistical confidence statement.

**Dependencies:** M17, M20, M26, M27.

**Story role:** Turn the theorem into a qualified experimental test.

**Conceptual connection:** Near isolation, shrinking entanglement margins require finer control of noise, collection and model errors.

**Sources:** Review II.A.1 and V.A for covariance/channel parameters; [interpretation §3](../science/interpretation.md#3-calibrating-the-boundary).

### M30 — Complete physical interpretation

**Phase:** Narrative and innovation.

**Central question:** What does the project establish as a whole, and which changes define a different problem?

**Understanding target:** Reconstruct the chain from complete mode accounting to the exact access boundary and matched rate order; distinguish established ingredients, derived claims, finite checks and effective-model assumptions; explain the extra-port, idler-access and finite-resource qualifications.

**Dependencies:** M13, M18, M19, M20, M23, M26, M28, M29.

**Story role:** Integrate the scientific narrative and its physical meaning.

**Conceptual connection:** The central result is about a fully specified accessible quantum channel, not a universal prohibition on every device called an isolator.

**Sources:** Review V.A, D, F; [interpretation](../science/interpretation.md); [related work](../references/RELATED_WORK.md); [verification](../verification/README.md).

Return to the [learning overview](README.md), [bridge](WEEDBROOK_BRIDGE.md), or [scientific entrypoint](../science/model.md).

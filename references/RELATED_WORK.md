# Related work and attribution

This note locates the results in this repository within the literature on Gaussian channels, environmental monitoring, and nonreciprocal bosonic devices. Bibliographic records are collected in [references.bib](references.bib). The physical assumptions and theorems are stated in [the model](../science/model.md), [the collection boundary](../science/collection_boundary.md), and [the scattering-noise analysis](../science/scattering_noise.md).

## 1. The interface under study

The vacuum model includes **exactly two positive-norm channels**, every negative-norm auxiliary channel, and no uncounted positive-norm bath:

```math
b_+=A a_+ +B e^\dagger,\qquad AA^\dagger-BB^\dagger=I_2.
```

Alice supplies the signal input $`a_1`$, Bob receives $`b_2`$, and Alice collects $`\sqrt\eta\,b_1+\sqrt{1-\eta}\,v`$, where $`v`$ is an independent vacuum mode. All other inputs are independent vacuum and all other outputs are inaccessible. The measured quantities are

```math
G=|A_{21}|^2,\qquad R=|A_{12}|^2,\qquad
N=(BB^\dagger)_{22},\qquad c=N-G=|A_{22}|^2-1.
```

Here $`R`$ is the reverse **power** transmission. Counting only observed ports while omitting a positive-norm loss bath does not satisfy this model. A finite set of internal oscillator modes need not equal the complete set of scattering channels.

The principal connection developed here is an operational boundary in these scattering and collection variables. The accessible device cannot generate entanglement or secret key, even with unrestricted adaptive local operations and classical communication, precisely in the closed region

```math
\boxed{c\ge0,\qquad (1-\eta)c\ge\eta R.}
```

The converse uses a local Alice-instrument/Bob-state-preparation representation. Outside that region, a finite-energy entangled input and return heterodyne with conditional displacement produce a distillable resource. The Gaussian mathematics behind this statement has substantial prior history; the attribution below separates those tools from their application to the specified scattering interface.

## 2. Established mathematical and information-theoretic tools

| Ingredient | Prior result used here |
|---|---|
| Commutator preservation and amplifier noise | [Caves (1982)](https://doi.org/10.1103/PhysRevD.26.1817), `Caves1982`, establishes quantum restrictions on linear-amplifier noise. The relation $`AA^\dagger-BB^\dagger=I`$ is a canonical-commutator constraint. |
| Covariance matrices, Gaussian measurements, and conditional states | [Weedbrook et al. (2012)](https://doi.org/10.1103/RevModPhys.84.621), `Weedbrook2012`, reviews these methods, including symplectic transformations, Gaussian separability, heterodyne detection, and one-mode channels. |
| Entanglement breaking | [Holevo (2008)](https://doi.org/10.1134/S0032946008030010), `Holevo2008`, gives the infinite-dimensional characterization and one-mode Gaussian thresholds. In the convention used here, the reduced forward channel is entanglement breaking exactly when $`N\ge G`$. |
| Gaussian separability of the accessible Choi state | [Werner and Wolf (2001)](https://doi.org/10.1103/PhysRevLett.86.3658), `WernerWolf2001`, proves that positivity under partial transpose implies separability for a Gaussian state with one mode on one side and any number on the other. Bob has one mode; Alice's side includes the reference and collected return. |
| Infinite-dimensional separable decompositions | [Holevo, Shirokov, and Werner (2005)](https://arxiv.org/abs/quant-ph/0504204), `HolevoShirokovWerner2005`, supplies the integral representation over product states. Continuous decompositions are important: separable states need not admit a countable product decomposition. |
| Distillation and achievable rates | [Giedke et al. (2001)](https://doi.org/10.26421/QIC1.3-7), `Giedke2001`, gives the distillability criterion for bipartite Gaussian states. [Devetak and Winter (2005)](https://doi.org/10.1098/rspa.2004.1372), `DevetakWinter2005`, supplies the hashing lower bound. Distillation is not restricted to Gaussian operations. |
| Finite-energy truncation | [Winter (2016)](https://doi.org/10.1007/s00220-016-2609-8), `Winter2016`, Lemma 15, bounds entropy changes under oscillator energy constraints. Local finite-Fock truncations can therefore reduce the conditional-state hashing argument to finite dimensions without changing its limiting coherent information. |
| Amplifier–attenuator factorizations | [Rosati, Mari, and Giovannetti (2018)](https://doi.org/10.1038/s41467-018-06848-0), `Rosati2018`, and [Noh, Albert, and Jiang (2019)](https://doi.org/10.1109/TIT.2018.2873764), `Noh2019`, use Gaussian decompositions and data processing to bound noisy bosonic capacities. These are established methods. |
| Quantum capacities of elementary channels | [Wolf, Pérez-García, and Giedke (2007)](https://doi.org/10.1103/PhysRevLett.98.130501), `Wolf2007`, treats bosonic quantum capacities; [Qi and Wilde (2017)](https://doi.org/10.1103/PhysRevA.95.012339), `QiWilde2017`, treats amplifier capacities, including energy-constrained settings. |
| Two-way quantum and secret-key upper bounds | [Pirandola et al. (2017)](https://doi.org/10.1038/ncomms15043), `PLOB2017`, provides relative-entropy bounds and exact capacities for important elementary channels. Its noisy-channel upper bounds need not be exact capacities. |
| Logarithmic negativity | [Vidal and Werner (2002)](https://doi.org/10.1103/PhysRevA.65.032314), `VidalWerner2002`, supplies a computable upper bound on distillable entanglement. This does **not** furnish a general upper bound on secret-key capacity. |
| Bosonic teleportation simulation | [Pirandola, Laurenza, and Braunstein (2018)](https://doi.org/10.1140/epjd/e2018-90253-1), `PirandolaLaurenzaBraunstein2018`, distinguishes strong, energy-bounded uniform, and unconstrained uniform convergence. Adaptive-channel arguments must respect these distinctions rather than assume unrestricted uniform convergence of finite-energy teleportation. |

These references support the proof machinery. The boundary expressed in $`c,R,\eta`$, and its consequences for measured reverse transmission, are the statements studied in this repository.

## 3. Environmental monitoring: direct methodological precedent

[Sabuncu et al. (2010)](https://doi.org/10.1103/PhysRevA.81.012325), `Sabuncu2010`, already uses environmental heterodyne and feedforward to correct continuous-variable communication. Section III B, Eq. (14), obtains a quantum-limited amplifier; Eqs. (20)–(22) address noise optimization, and Sec. V discusses key recovery. Generic recovery from an entanglement-breaking reduced channel by accessing its environment is therefore an established phenomenon.

Their thermal beam-splitter example embeds directly in the present algebra. Let its transmissivity be $`T`$ and bath occupation be $`n`$. A purification gives

```math
A=\begin{pmatrix}
\sqrt{1-T}&-\sqrt{T(n+1)}\\
\sqrt T&\sqrt{(1-T)(n+1)}
\end{pmatrix},\qquad
B=\sqrt n\begin{pmatrix}-\sqrt T\\\sqrt{1-T}\end{pmatrix}.
```

Then

```math
G=T,\qquad R=T(n+1),\qquad c=(1-T)n-T,
\qquad \frac{|\det A|^2}{R}=\frac1T.
```

The ideal corrected amplifier gain is exactly theirs. For $`c\ge0`$, the collection boundary above specializes to $`\eta_{\rm crit}=1-T-T/n`$. This parameter comparison is an algebraic specialization made here. The fixed-$`G`$, small-$`R`$ isolation regime differs from that example's $`R\ge G`$ ordering, but the correction mechanism is shared.

[Pirandola et al. (2021)](https://doi.org/10.1038/s41534-021-00413-2), `Pirandola2021`, also demonstrates environment-assisted reactivation of bosonic communication. That work uses correlations between two noisy links and a relay measurement. It provides further precedent for recovery despite entanglement-breaking marginal channels, with a different distribution of accessible systems.

## 4. Gaussian measurement boundaries and the all-protocol distinction

[Kwiatkowski et al. (2023)](https://doi.org/10.1103/PhysRevA.107.042604), `Kwiatkowski2023`, studies independent Gaussian error channels before a joint Gaussian measurement. Propositions 4.1 and 4.3 identify when all such Gaussian measurements become separable; Sec. 6 gives a dual-channel formulation. The paper explicitly distinguishes this restriction from what non-Gaussian measurements can achieve.

The interface here is instead a correlated one-input/two-output scattering channel, with one output returned to the sender. Its zero-capacity claim permits arbitrary local instruments and adaptive use of the device. The separability construction is therefore essential: proving that a chosen Gaussian receiver fails would not establish the stated converse. This distinction concerns the allowed operations and access to the outputs, rather than a new Gaussian positivity technique.

## 5. Nonreciprocal amplifiers and propagating entanglement

[Metelmann and Clerk (2015)](https://doi.org/10.1103/PhysRevX.5.021025), `MetelmannClerk2015`, establishes directionality through interference between coherent and dissipative interactions. Auxiliary reservoirs are physical resources in that construction and must be counted when comparing scattering-channel restrictions.

[Sliwa et al. (2015)](https://doi.org/10.1103/PhysRevX.5.041020), `Sliwa2015`, demonstrates a reconfigurable Josephson circulator/directional amplifier using conversion and pair-creation links. In its directional-amplifier convention, the strongly isolated signal–idler pair includes a conjugated sector. The two positive-sector ports have approximately unit reverse transmission. This port assignment matters when comparing the experiment with a bound on $`R`$ between two positive-norm channels; the architecture itself is prior art.

[Orr et al. (2023)](https://doi.org/10.1103/PRXQuantum.4.020344), `Orr2023`, uses nonreciprocity to route thermal noise and generate high-purity entanglement between propagating output modes. That output-entanglement problem differs from preserving entanglement between an externally retained reference and a positive-norm receiver, but it already connects nonreciprocity, circuit ordering, and useful quantum correlations.

[Liu et al. (2024)](https://doi.org/10.1103/PhysRevApplied.21.014021), `Liu2024`, treats fully directional, matched, quantum-limited amplification with a minimum four-port construction. Its phase-preserving port structure can include three positive channels and one negative channel. Such a device lies outside the present two-positive-channel assumption. [Landgraf, Peano, and Marquardt (2025)](https://doi.org/10.1103/PhysRevX.15.021038), `Landgraf2025`, develops automated discovery of coupled-mode setups. Its examples further illustrate why internal-mode counts and monitored submatrices cannot replace complete bath accounting.

[Brádler and Adami (2015)](https://doi.org/10.1103/PhysRevD.92.025030), `BradlerAdami2015`, already classifies black-hole transformations as bosonic Gaussian channels and studies their quantum capacities. The use of Gaussian-channel theory in horizon physics is not itself a new contribution.

## 6. Scope of the rate comparison

With the return discarded, the canonical constraint implies $`N\ge G-R`$. Applying established Gaussian-channel bounds gives an $`O(R^2)`$ upper envelope at fixed nonzero $`G`$ for two-way quantum capacity and secret-key capacity. This is an upper bound for the **reduced forward channel**. It is not a bound for a device that also supplies Alice with its returning field.

For the specified unit-forward stable family and ideal return collection, let $`s=\sqrt R`$, $`p=1-s`$, and $`0<R<1`$. A finite-energy conditional-state protocol has the achievable rate

```math
I(R)=2-h\!\left(1-\frac{R}{(2-\sqrt R)^2}\right)
=\frac R4+O(R^{3/2}),
```

where $`h(x)=(x+1)\log_2(x+1)-x\log_2x`$. The channel's displacement covariance and asymptotic Choi-state logarithmic negativity give

```math
Q_2(R)\le U(R)
=\log_2\!\left[
\frac{p^2+s^2+\sqrt{1+4Rp^2}}{2p}
\right]
=\frac{2R}{\ln2}+O(R^2).
```

Together these establish $`Q_2(R)=\Theta(R)`$ for that ideal-access family as $`R\to0`$. The lower bound uses the established hashing theorem; the upper bound uses the established simulation and negativity tools identified above. Neither inequality determines the exact capacity. **The logarithmic-negativity upper bound is not asserted for secret key.** The bounded-energy lower-bound protocol must also be distinguished from direct environmental cancellation, whose corrected amplifier gain can diverge as $`R\to0`$.

## 7. Noise-synthesis priority qualification

[Petersen et al. (2019)](https://doi.org/10.2514/6.2019-0952), `Petersen2019`, and [Petersen et al. (2020)](https://doi.org/10.1109/CDC42340.2020.9304063), `Petersen2020`, specifically address nonreciprocal phase-insensitive amplifier synthesis and minimum noise. Their complete theorem statements have not been compared with this repository's scalar inequality for the summed spontaneous occupation of the two positive-signature outputs. **No priority claim is made for that scalar noise inequality or its three-quanta positive-output endpoint at unit forward power and zero reverse power.**

The operational scattering/access boundary and the monitored-versus-discarded communication comparison should be assessed separately from the scalar-noise result. This reference note documents concrete relationships and assumptions; it is not a certification that no earlier formulation of the operational result exists.

## 8. Atomic implementation references

The bibliography includes primary demonstrations of spatial and temporal interaction control (`Clark2015`, `Yamazaki2010`), driven matter-wave pair emission (`Clark2017`, `ChihHolland2020`), programmable atomic transport (`An2017`), and coherent atom-laser extraction (`Hagley1999`). Number-conserving condensate treatments are provided by `Gardiner1997` and `CastinDum1998`.

These references support constituent physical operations and approximations. They do not by themselves demonstrate the combined scattering module or the return-collection communication protocol proposed in this repository. The implementation discussion must supply that mapping explicitly.

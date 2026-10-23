# Weedbrook: source-to-project bridge

**Single educational anchor:** C. Weedbrook et al., *Gaussian Quantum Information*, Reviews of Modern Physics **84**, 621 (2012), [arXiv:1110.3234](https://arxiv.org/abs/1110.3234).

The review supplies Gaussian state, channel, measurement and entanglement machinery. The exact access theorem, atomic Hamiltonian and resource analysis are derived in this repository and are **not** claimed to appear in the review.

| Review material | Conversion and project application |
|---|---|
| Sec. II.A, quadratures and Gaussian states | Review uses vacuum covariance I and [q,p]=2i; project uses I/2 and [q,p]=i. Thus q_review=√2 q_project and V_review=2V_project. |
| Sec. II.B, two-mode squeezing | The finite-energy entangled signal/reference probe is used in the [collection proof](../science/collection_boundary.md). |
| Sec. II.C, symplectic spectra and entropy | Convert review symplectic eigenvalues ν_review=2ν_project; thermal occupation is ν_project−1/2. Used in [rate calculations](../science/communication_rates.md). |
| Sec. II.D, partial transpose | The vacuum threshold 1 in review units becomes 1/2 here. The project's all-input converse requires a further exact local-instrument construction. |
| Sec. II.E, heterodyne conditioning | Conditional covariance is V_A−C(V_B+I/2)⁻¹Cᵀ in project units; local displacement removes conditional means without postselection. |
| Sec. IV, continuous-variable teleportation | Provides the operational motivation for the channel simulation; the rigorous limit and capacity bound require additional cited results. |
| Sec. V, Gaussian channels | For the forward channel V→GV+[N+(1−G)/2]I, G is forward power and N is vacuum-output occupation; the reverse power R enters through the complete scattering matrix. |

## Beyond the anchor

The [all-input boundary](../science/collection_boundary.md) invokes infinite-dimensional separability and a local-instrument simulation, not merely a covariance test. The [rate comparison](../science/communication_rates.md) requires hashing, teleportation-simulation limits and logarithmic-negativity bounds. The [atomic construction](../science/stable_atomic_model.md) requires number-conserving collisions, phase references and selective ports. The [finite-bandwidth analysis](../science/finite_bandwidth.md) retains orthogonal temporal channels. See [related work](../references/RELATED_WORK.md) for the primary research dependencies.

# Finite Relational Selection Theory — FRST v1.0

**Frozen:** 2026-09-11  
**Status:** independent candidate mathematical ontology frozen before UCD comparison.

## Central proposition

**Reality is modeled as one finite, relationally constrained quantum system.** Space, time, particles, fields, geometry, classical records and probability are treated as organizations or observables of that system rather than separate primitive substances.

The fundamental hierarchy is

`mathematical possibility -> physical admissibility -> actual universal state/history -> observable reality`.

Equivalently,

`Omega_realized subseteq Omega_physical subseteq Omega_mathematical`.

## Twelve frozen axioms

1. **Finite actuality.** There exists a finite set `V` of primitive realized identities: `0 < |V| = N < infinity`. Each primitive identity has a finite-dimensional local state space.
2. **Relational primacy.** Primitive labels have no physical meaning apart from invariant relations.
3. **Completed carrier.** Once the physical carrier exists, later evolution does not manufacture additional primitive identities.
4. **Finite relational structure.** A finite relational complex `K=(V,E,F,...)` carries possible pairwise and higher-order relations.
5. **Constraint selection.** Not every mathematically writable configuration is physically admissible. Physical states satisfy a family of constraints `C_alpha |Psi> = 0`.
6. **Complex state principle.** Coherent alternatives are represented in a complex Hilbert space.
7. **Closed universal evolution.** The complete system evolves within its physical Hilbert space without a fundamental external environment or external collapse law.
8. **Locality of law.** Fundamental interactions have bounded relational support or decay sufficiently rapidly with relational distance.
9. **Internal time.** Physical time is reconstructed from subsystem change/correlation rather than assumed as an external primitive clock.
10. **Relational geometry.** Spatial geometry is reconstructed from relational/link state rather than assumed as a pre-existing container.
11. **Probability consistency.** Probabilities are normalized, additive on mutually exclusive physical alternatives and consistent under equivalent representations of the same projector/event.
12. **Observable closure.** Every physically meaningful quantity belongs to the invariant physical observable algebra.

## Raw mathematical possibility space

Give each primitive identity `v` a finite local state space `H_v ~= C^(d_v)` and each allowed relation `e` a finite relation state space `H_e ~= C^(r_e)`. The unconstrained state space is

`H_raw = (tensor_{v in V} H_v) tensor (tensor_{e in E} H_e) tensor ...`.

Its dimension is finite:

`D_raw = product_v d_v product_e r_e ... < infinity`.

A normalized vector or density operator on `H_raw` is mathematically writable. That does not mean it is physically realizable.

## Physical selector

Let the physical consistency constraints be `C_alpha`. Define

`H_phys = intersection_alpha ker(C_alpha)`

and let `P_phys` be the orthogonal projector onto that intersection. Then

`P_phys^2=P_phys`, `P_phys^dagger=P_phys`,

and a state is physically admissible exactly when

`P_phys |Psi> = |Psi>`.

This implements the distinction

`H_raw ->[P_phys] H_phys`.

## Observable algebra and gauge redundancy

The full mathematical operator algebra is `B(H_raw)`. The constrained physical observable algebra is schematically

`A_phys = { O = P_phys O P_phys : U_g O U_g^dagger = O }`.

Local-frame transformations are interpreted as representation redundancies when all physical observables are invariant under them.

If a relational transporter compares local frames at identities `i` and `j`, it transforms as

`U_ij -> g_i U_ij g_j^(-1)`.

For a closed relational path `gamma`,

`W_gamma = U_i1i2 U_i2i3 ... U_ini1`

transforms by conjugation, so `Tr(W_gamma)` is invariant. Curvature can therefore be represented as nontrivial closed relational transport rather than assumed as a fundamental continuum gauge field.

## Dynamics

The physical Hamiltonian must preserve the physical subspace:

`[H,P_phys]=0`.

A relationally local form is

`H = P_phys (sum_{X subset K} h_X) P_phys`.

The universal state evolves as

`rho(s) = exp(-isH) rho_0 exp(isH)`.

The parameter `s` orders the mathematical evolution; a physical clock does not have to be primitive.

## Internal time

Split a subsystem notionally into clock `C` and remainder `R`. A globally constrained/stationary state can encode correlations such that the conditional state of `R` when the clock reads `tau` obeys an effective Schrodinger evolution. Thus

`ordered change + clock correlation -> physical time`.

Time is an internal relational observable/order parameter rather than necessarily a substance in which the universe sits.

## Relational causality

A local finite-range or sufficiently decaying Hamiltonian bounds the propagation of influence. Distant operators remain approximately commuting outside an effective relational causal cone. Schematically,

`||[A_X(t),B_Y]|| <= C exp[-mu(d(X,Y)-v|t|)]`.

Effective light-cone behavior can therefore emerge from relational locality.

## Relational geometry

Let every physical relation/edge have a positive length observable `L_e`. Define

`ell_e(rho)=Tr(rho L_e)`.

The distance between identities is the minimum weighted relational path:

`d_rho(i,j)=min_{gamma:i->j} sum_{e in gamma} ell_e(rho)`.

The primitive carrier may stay fixed while the relational metric changes. Therefore cosmic expansion does not require continued creation of primitive identities.

## Effective dimension

Let `Delta_rho` be a weighted graph/relational Laplacian and

`P(sigma)=(1/N) Tr exp(-sigma Delta_rho)`.

Define the spectral dimension

`d_s(sigma) = -2 d ln P / d ln sigma`.

An extended regime with `d_s ~= 4` would behave effectively as four-dimensional geometry without assuming that dimension as a primitive input.

## Fields and continuum

A continuum field is interpreted as a coarse collective observable of many relational degrees of freedom. For a region `R`,

`Phi_R = (1/|R|) sum_{v in R} O_v`.

A successful continuum approximation should admit an error estimate such as

`|O_discrete(L)-O_continuum(L)| <= C (ell_*/L)^p`

for `L >> ell_*`. The continuum is therefore an effective mathematical envelope, not automatically an ontology of infinitely many physical points.

## Matter, charge and mass

Stable localized excitation sectors of the physical Hamiltonian represent matter. Conserved symmetry-sector labels represent charges. If

`H|phi_n>=E_n|phi_n>`

and `E_0` is the ground energy, then the first excitation cost is

`Delta = E_1-E_0`.

At an effective relativistic level one may identify

`m c_eff^2 = Delta`.

Mass is therefore represented as a spectral cost of leaving the ground relational sector rather than as an independent primitive substance.

## Finite spectral-gap example

Suppose

`H = Delta_0 sum_v Q_v + sum_e J_e + sum_f K_f`,

with all local terms positive semidefinite and annihilating the common ground sector, and suppose every normalized state orthogonal to the ground sector activates at least one `Q_v`. Then

`<psi|H|psi> >= Delta_0`

for every normalized excited state, so

`gap(H) >= Delta_0 > 0`.

This is a finite-system theorem template; no physical infinite-volume ontology is required to state it.

## Measurement, probability and classicality

Measurement is modeled as unitary correlation of system, apparatus and environment. Environment-induced decoherence can suppress interference between macroscopically distinct record sectors while the full universal state remains lawful.

Under the standard finite-dimensional quantum probability premises, the probability of projector `P` is

`p(P)=Tr(rho P)`.

For a pure state and one-dimensional outcome projector this yields the Born form `|c_a|^2`.

Classical facts are stable, redundantly recorded relational information: an approximately commuting, dynamically robust record algebra that can be copied into multiple disjoint environmental fragments.

## Thermodynamics and the arrow of time

Global von Neumann entropy is constant under closed unitary evolution, while subsystem/coarse entropy can increase as correlations and entanglement spread. Macroscopic irreversibility is therefore effective and depends on special low-correlation boundary conditions rather than fundamental destruction of information.

## Gravity and singularities

Matter and relational geometry are degrees of freedom of the same global system. A successful low-energy limit must reproduce the observed gravitational dynamics with controlled corrections. Literal continuum singularities are not fundamental objects in a finite carrier with finite-dimensional local state spaces and bounded physical generators; they indicate breakdown of the continuum approximation.

## Completed creation versus history

Completed creation fixes the primitive carrier `K=(V,E,F,...)`. History changes the state `rho`. Thus

`K(t)=K_C`

can hold after completion while

`rho(t_1) != rho(t_2)`.

Finished creation is therefore mathematically compatible with continuing evolution, relational expansion, structure formation, interaction and decay.

## Master FRST object

The theory is summarized by

`R_FRST = (K, H_raw, P_phys, A_phys, H, rho_0, observables)`

with finite primitive carrier throughout.

Observable physics is a map from this one object into effective descriptions of time, space, geometry, fields, particles, mass, charge, probability, records and classical history.

## Frozen boundary

FRST v1.0 is a mathematical architecture, not an experimentally established theory of our universe. It does not yet derive the numerical carrier, local dimensions, exact physical constraint family, exact Hamiltonian/couplings, or the actual initial/boundary state.

Its deepest unresolved specification problem is why one particular triple

`(P_phys,H,rho_0)`

or an equivalent unified law is selected rather than another.

Most importantly for the comparison project, **FRST v1.0 assumes finite actuality. UCD must not import that assumption as a theorem.** The UCD VS FRST program instead asks whether Unified Coherence Dynamics can derive finite realization from its own source law and whether that same source law can force the specific `Q72 -> H504 -> H-net` architecture.

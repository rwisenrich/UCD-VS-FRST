# UCD VS FRST v2.0 - Selector, Actuality, and Continuum-Envelope Audit

## Scope
FRST v1.0 remains frozen. UCD remains separate. The hierarchy is sharpened to

`H_raw --P_phys--> H_phys --H--> lawful histories --rho_0--> actual realized history`.

Thus `(P_phys,H,rho_0)` are logically distinct data: the selector says what may exist, the Hamiltonian says how admissible states may evolve, and the initial/boundary rule selects the realized history.

## Constraint-intersection projector theorem
Let `K_alpha = ker C_alpha`. Then `H_phys = intersection_alpha K_alpha` is a subspace. In finite dimension it has a unique orthogonal projector `P_phys=P_phys^dagger=P_phys^2`. This is the safe master-selector definition.

## Product-of-projectors no-go
For noncommuting constraint projectors, a simple product need not be Hermitian or idempotent. Therefore `P_phys=product_alpha P_alpha` is valid only if commutation or another sufficient construction is proved. In general use the orthogonal projector onto the intersection.

## Admissibility, dynamics, actuality
If `dim H_phys >= 2`, multiple normalized states satisfy `P_phys psi=psi`; therefore admissibility does not pick actuality. A fixed nontrivial `P_phys` also admits many distinct Hermitian generators with `[H,P_phys]=0`; therefore the selector does not pick dynamics. For fixed `(P_phys,H)`, multiple physical density operators may serve as `rho_0`; therefore a realized-history rule is separate data.

## Generic selector uniqueness no-go
On `C^4`, the same nontrivial frame symmetry `U=diag(1,-1,1,-1)` commutes with both `P_A=diag(1,1,0,0)` and `P_B=diag(0,0,1,1)`. Both are nonzero orthogonal projectors but select inequivalent subspaces. Finite-dimensionality, projector consistency and nontrivial frame symmetry therefore do not uniquely determine a physical selector.

## Finite capacity is not a finite set of quantum rays
For finite Hilbert dimension `D`, at most `D` orthogonal alternatives are perfectly distinguishable and `S(rho)<=log D`. But for `D>=2`, normalized rays form a continuous projective space, for example `( |0> + exp(i theta)|1> )/sqrt(2)`. Finite actuality must therefore mean finite primitive carrier / finite Hilbert dimension / finite distinguishable capacity, not a finite number of mathematically expressible superpositions.

## Exact finite/continuum identity no-go
A finite-dimensional Hilbert space cannot be unitarily isomorphic to an infinite-dimensional continuum Hilbert space because unitary equivalence preserves dimension. A finite-ontology theory must treat continuum mathematics as controlled approximation, mathematical completion/envelope, or benchmark language rather than literal ontic identity.

## Controlled continuum approximation without physical infinity
For a cycle of `N` sites with spacing `a=L/N`, `lambda_disc = 4 sin^2(pi k/N)/a^2` while the continuum circle gives `lambda_cont=(2 pi k/L)^2`. With `x=pi k/N`, the ratio is `(sin x/x)^2`. For `0<=x<=1`, `sin x >= x-x^3/6`, so

`0 <= 1-(sin x/x)^2 <= x^2/3`,

hence

`|lambda_disc-lambda_cont|/lambda_cont <= pi^2 k^2/(3 N^2)`.

So a finite carrier can reproduce continuum behavior to controlled precision over a finite observational band without asserting a physically infinite point set.

## UCD bridge and firewall
An H504 node is structurally compatible with the generic finite-local-space template by setting `d_v=504`. This does not derive 504, Q72 or H504 from FRST. Existing UCD constraints can be collected definitionally as `H_UCD_phys=intersection ker C_alpha` and `P_UCD=Proj(H_UCD_phys)`, but that does not prove the constraint list complete or uniquely forced. The H504 replay gap `0.19724142334878325` remains a finite subsystem spectral datum only.

FRST v1.0 assumes finite actuality; UCD v14 explicitly leaves P0-FINACT open. No merger may erase that distinction.

## New source target
A complete unique theory must derive `(P_phys,H,rho_0)` or an equivalent unified source law fixing admissibility, dynamics and actuality. For UCD this means deriving `P_UCD`, `H_UCD`, `rho_0,UCD` and separately closing P0-FINACT.

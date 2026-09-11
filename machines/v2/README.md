# UCD VS FRST Selector + Actuality v2.0

This is the first development pass after the frozen FRST v1.0 / UCD comparison baseline. It does not modify FRST v1.0 and does not silently merge FRST assumptions into UCD.

The v2 line separates four logically different layers:

`mathematical possibility -> physical admissibility -> lawful dynamics -> actual realized history`

The corresponding data are `(P_phys, H, rho_0)` plus the raw mathematical carrier.

Main results: the physical selector is safely defined as the orthogonal projector onto the intersection of constraint kernels; products of noncommuting projectors are not a general selector construction; admissibility does not determine actuality; a selector does not determine dynamics; finite physical capacity does not mean finitely many pure-state rays; a finite physical Hilbert space cannot be literally identical to an infinite-dimensional continuum Hilbert space; and a finite cycle nevertheless reproduces continuum low modes with a controlled O((k/N)^2) error.

UCD firewall: FRST finite actuality is not imported as a UCD theorem. UCD v14 still requires P0-FINACT.

Run: `python machines/v2/verify_v2.py`

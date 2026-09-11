# UCD VS FRST

Research repository for the frozen **Finite Relational Selection Theory (FRST)**, the current **Unified Codex Dynamics (UCD)** comparison baseline, reproducible machine checks, theorem ledgers, and explicitly versioned integration work.

## Repository policy

- `frst/` preserves FRST as an independent theory unless a later version explicitly changes it.
- `ucd/` preserves UCD provenance and does not silently import FRST assumptions as UCD theorems.
- `comparison/` contains the formal mapping, firewall checks, and integration ledgers.
- `machines/` contains the next-generation theorem/bridge machines and reproducible outputs.
- `releases/` stores immutable frozen release bundles.
- `paper/` contains human-readable reports.
- `results/` contains master verdicts and checksums.

## Baseline

The first committed baseline is **FRST v1.0 Freeze + UCD Comparison v1.0**. FRST v1.0 is frozen. The UCD side is a replay/comparison snapshot, not a replacement of the main UCD canon.

The baseline keeps the logical distinction

`mathematical possibility -> physical admissibility -> actual realization`

while enforcing a fail-closed rule: a result assumed by FRST is not counted as a theorem of UCD unless independently derived inside UCD.

## Current frontier

The next machine line studies the shared selector problem: which constraints define physical admissibility, how actualization is distinguished from admissibility, whether generic relational axioms determine a unique selector, and how a finite physical carrier can support a continuum approximation without importing physical infinity.

## Status language

Machine results use explicit statuses such as `THEOREM_CLOSED`, `CONDITIONAL`, `NEW_THEOREM_REQUIRED`, `RECONCILIATION_REQUIRED`, and `FAILED_ROUTE_NO_GO`. A computational PASS means the encoded theorem/check passed; it is not by itself empirical proof of a physical theory.

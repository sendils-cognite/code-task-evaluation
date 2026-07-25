# Solution Architect Python Exercise Pack

This pack is for a ten-minute live assessment of Solution Architect candidates who
will work on data-platform projects. It deliberately uses ordinary Python and generic
data-platform concepts; no Cognite or CDF knowledge is required.

The candidate may use an IDE, tests, documentation, internet search, and AI. Code
completion is therefore not enough evidence of seniority. The interviewer should score
how quickly the candidate identifies correctness risks, validates assumptions, and
explains how the code would operate in production.

## Recommended format

- 1 minute: candidate reads the prompt and asks clarifying questions.
- 6 minutes: candidate implements the function and runs the visible tests.
- 3 minutes: interviewer asks two facilitator questions.
- Choose one of the three complete assignments below.
- Give candidates only that assignment's `candidate/` directory.
- Keep every `facilitator/` directory private.

## Complete assignments

1. [`candidate/`](candidate/): published-record reconciliation.
2. [`configuration-contract/`](configuration-contract/): declared versus referenced
   configuration variables.
3. [`multihop-contextualization/`](multihop-contextualization/): validate
   `source row → equipment → location` coverage and diagnose the failed hop.

## Ranked exercise ideas

### 1. Reconcile source and published records

Given source records and identifiers from a published system, report matched, missing,
and extra identifiers. Only active source records are expected, identifiers are
normalized, duplicates collapse, extras do not fail coverage, and an empty expected set
must not pass.

Why it is recommended:

- The implementation is small enough for six minutes.
- Set operations expose whether the candidate can select an appropriate data structure.
- The empty-source false pass, normalization boundary, and deletion semantics reveal
  production data judgment.
- Follow-up questions naturally cover observability, scale, and stale snapshots.

Repository inspiration:
[`../course-creation/compare_raw_to_view.py`](../course-creation/compare_raw_to_view.py).

### 2. Validate a configuration contract

Given variables declared in a configuration and placeholders referenced by templates,
return missing and unused variables. Ask the candidate which findings should block a
deployment and which should be warnings.

Senior signal: closed-world configuration design, error taxonomy, and safe rollout.

Repository inspiration:
[`../../.github/scripts/audit_configs.py`](../../.github/scripts/audit_configs.py).

### 3. Check producer-consumer coverage

Given upstream dataset names and downstream job names that follow a convention, report
upstream datasets with no consumer and jobs with no producer. Include one malformed job
name and ask whether it should be ignored, warned, or rejected.

Senior signal: pipeline completeness, naming contracts, and handling malformed inputs.


The complete multi-hop contextualization assignment replaces this idea when the desired
signal is whether every table row has valid business context rather than whether every
dataset has a processing job.

### 4. Calculate a safe deployment blast radius

Given changed package paths and tenant configurations that select packages, return the
tenants that must be tested. A change to shared configuration must trigger all tenants.

Senior signal: dependency reasoning, conservative fallbacks, and balancing safety with
CI cost.

### 5. Compare a declared contract with an implementation schema

Given a small API contract and implementation schema, report missing models, missing
required fields, and undocumented implementation fields. Ask the candidate to separate
errors from warnings and suggest close name matches.

Senior signal: governance, compatibility policy, and actionable diagnostics.

## Why the primary exercise is product-neutral

The exercise models a common boundary in data platforms: one system says which records
should exist, while another system exposes what was published. The same pattern applies
to databases, search indexes, caches, APIs, data lakes, and message consumers. It does
not depend on a vendor SDK or platform vocabulary.

## Files

Each complete assignment has:

- `candidate/PROMPT.md`: handout and commands.
- `candidate/*.py`: starter implementation and visible tests.

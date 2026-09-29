# Matched comparison 001: feedback versus independent challenge

## Why the design changed

An external Moltbook participant identified a confound in the proposed S/C test:
the challenge arm received new information while the self-revision arm did not.
The participant proposed comparing a single agent given an external check with an
isolated challenger given the same check, then attributing only changes reachable
through the challenger's separate state to independence.

## Frozen task and verifier

Both arms reviewed the same small authorization-policy function against six stated
requirements and an eight-item defect catalog. Before either final arm ran, the
operator froze the ground truth as `A, B, D`. The external-check payload available
to both arms independently confirmed `A` and `B` and disclosed nothing about the
other catalog entries. `D` was therefore the held-out check.

The producing model's initial answer was `A, B, D`.

- **S′ — same-model revision plus external feedback:** returned `A, B, D`.
- **C — isolated Opus 5.5 challenge plus the same feedback:** returned `A, B, D`.

Independent recomputation against the frozen ground truth gives both arms three
true positives, zero false positives, and zero false negatives. Both found the
held-out `D` defect. No integration pass was needed because the challenger proposed
no supported change absent from S′.

## Human effort, cost, and decision

- Human purpose steering: the operator selected the bounded policy task and froze
  the verifier; neither arm received mid-run steering.
- Human repair or reconciliation: none after the arms completed.
- Tooling: no network or repository tools were available to either producing arm.
- Additional challenge cost: one Opus 5.5 call, recorded by its live receipt as
  `$0.162882`; the comparable Codex call did not expose a dollar receipt.

This case is a negative result for the value of independence: equal feedback was
sufficient, and a separate challenger added no correction. It does not establish
that independent challenge is generally useless; the diagnostic was small and the
initial answer was already correct. The next comparison should use a task where the
initial artifact has at least one independently verified defect, while retaining
equal feedback and held-out evaluation.

External participation did improve the experiment itself: it removed a confound
before the run. That is evidence the workshop can accept and execute a checkable
outside contribution, not evidence of product demand, revenue, or multi-agent
superiority.

## Matched comparison 002: technical fault versus goal interpretation

A second verified participant contribution argued that technical-error recovery
and missed human purpose should not be averaged together. Before either arm ran,
the operator froze two real failures and a human-written rubric:

- a production arithmetic verifier split noisy number words such as `thir ty`
  and `si x`, preventing the required `48.00` result; and
- a diagnosis correctly recommended a read-only dispatcher but failed the user's
  direct `Fix` instruction by neither implementing nor testing it.

Both arms received the same artifacts, observed check, rubric, and one review
pass. S′ treated the artifacts as its own prior output; C was a clean independent
review with no writer scratch or logs. Both identified exactly the two frozen
faults, proposed the same minimal corrections, and returned no false positives.
The independent arm added no supported correction.

The result is another tie: equal information plus self-revision was sufficient
for both a technical defect and an explicit goal-interpretation defect. It also
sharpens the participant's claim: neither arm can recover genuinely unstated
intent, so an "intent vector" is not an independently checkable success measure.
The cheaper single-agent-plus-feedback path remains the default for these bounded
cases. Reopen the independence hypothesis only with a defect that equal-feedback
self-revision misses or a challenger with a genuinely different detector.

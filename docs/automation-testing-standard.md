# Automation Test Standard - and When to Start

Manual validation (see the [Manual Testing Framework](manual-testing-standard.md)) comes first. Automation
is built **when manual checking becomes the bottleneck** - when the frozen task set is large enough and
stable enough that re-running it by hand on every change is the limiting factor.

- **Starting earlier** automates a moving target.
- **Starting later** wastes effort on repetitive manual checking.

## The handoff

**The frozen task set is the bridge.** The version-controlled bank built in the
[Manual Testing Framework](manual-testing-standard.md#the-frozen-task-set-is-a-required-deliverable) becomes
the automated dataset. Without it, automation starts from scratch and cannot detect regressions - which is
why the frozen task set is a required manual-testing deliverable, not an automation one.

## Grader taxonomy

Every automated check uses one of three grader types, matched to the kind of output being judged:

| Grader | Judges | Use for |
| --- | --- | --- |
| **Code-based (deterministic)** | Exact / structural correctness | Non-LLM behavior and any output with a defined correct answer. |
| **Model-based (LLM-as-judge)** | Open-ended generation against criteria | Outputs where there is no single correct string - generation quality, classification, suggestions. |
| **Human spot-check** | What graders miss | A sampled manual pass that stays in place to catch gaps and keep the automated graders honest. |

The human spot-check does not disappear when automation arrives - it is the check on the checkers.

## What the suite must distinguish

- **Capability vs. regression.**
    - **Capability evals** ask: *is the feature good enough to ship?* These sets grow as features expand.
    - **Regression evals** ask: *did this change break what already worked?* The frozen task set anchors
      regression.
- **Once the automated suite is the gate,** manual validation shrinks to **targeted spot-checks** rather
  than full manual runs.

## Building the automated suite - step by step

1. **Confirm the trigger.** The frozen task set is stable and large enough that running it by hand on
   every change is the bottleneck. Only then start.
2. **Import the frozen task set** as the regression dataset. Inputs and pass/fail criteria carry over
   directly.
3. **Assign a grader per input.** Deterministic inputs get code-based graders; model-driven inputs get an
   LLM-as-judge scored against the agreed criteria.
4. **Wire it into CI** so the suite runs as a required check (see the [CI/CD Standard](ci-cd-standard.md)).
5. **Keep a human spot-check in the loop** - a sampled manual pass that validates the graders themselves.
6. **Grow capability sets alongside features** while the frozen set continues to anchor regression.

!!! note "Automation is earned, not scheduled"
    You build the suite when manual runs are the limiting factor - not on a fixed date. The frozen task set
    is what makes that transition possible at all.

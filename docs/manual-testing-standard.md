# Internal Manual Testing Framework

Manual validation is the **current operating gate on the development side**: structured manual validation
before a change is promoted between environments. It comes after the change is built and self-reviewed
(see the [Engineering Baseline](engineering-baseline-standard.md)) and before promotion (see the
[Branch Strategy](branching-standard.md)).

## Two categories that always travel together

| Category | What manual validation covers |
| --- | --- |
| **Non-LLM behavior** | Functional and end-to-end paths: integrations (e.g. GHL, Twilio), auth, data flows, the full user/lead journey. **Deterministic** — a defined input has a defined correct output. |
| **LLM + RAG behavior** | Model-driven features: generation quality, sentiment/classification, qualification or suggestion logic, and retrieval quality. Judged against **agreed criteria**, not a single correct string. |

Every feature is validated across both categories where both apply — you do not sign off deterministic
paths and skip the model-driven ones, or vice versa.

## Validation runs before promotion

- Validation runs **before promotion** between environments (dev → staging → production).
- A change is checked against the four self-review questions in the [Engineering Baseline](engineering-baseline-standard.md#human-self-review)
  **plus** the category checks above.
- **A change is not promoted on "looks fine."** It is checked against stated criteria.

## The frozen task set is a required deliverable

For any feature with LLM behavior, the team builds a **fixed bank of 20–40 real inputs with agreed
pass/fail criteria.** This is the load-bearing artifact of the framework:

- It makes manual judgment **repeatable** — the same inputs, the same criteria, every time.
- It is the **explicit handoff into automation** (see the [Automation Test Standard](automation-testing-standard.md)).
- It is **version-controlled** and **grows with the product** — it is not optional.

### Building the frozen task set — step by step

1. **Collect real inputs.** Pull 20–40 representative inputs from actual usage or realistic scenarios — not
   toy examples. Cover the common path, the edge cases, and the known failure modes.
2. **Write pass/fail criteria for each.** For deterministic inputs, the criterion is the exact/structural
   correct output. For model-driven inputs, the criterion is what a good answer must and must not do — the
   qualities that make it acceptable, since there is no single correct string.
3. **Freeze it.** Commit the input bank and its criteria to version control. This is the reference set.
4. **Run it before each promotion.** Record each input as pass / fail / risk against its criteria, with
   notes on any fix or deferral.
5. **Grow it.** When the product gains behavior or a new failure mode is found, add inputs and criteria.
   The set expands; it is never quietly shrunk.

!!! note "Why frozen"
    A fixed, version-controlled set is what turns subjective "it looked good" into a repeatable check —
    and it is exactly the dataset automation inherits when manual runs become the bottleneck.

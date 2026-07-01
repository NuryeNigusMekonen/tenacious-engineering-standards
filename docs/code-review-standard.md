# Code Review Standard

Review at Tenacious happens in two layers: the engineer's own **self-review and automated review** before a
PR opens (the merge gate), and **optional teammate review** that adds a second perspective. This standard
defines both and how they fit together.

## The two layers of review

1. **Self-review + automated review (the gate).** Before opening a PR, the engineer runs the
   [Engineering Baseline](engineering-baseline-standard.md): automated review (CodeRabbit or equivalent)
   plus the four-question human self-review. Automated review then runs again on the PR. **Passing
   automated review and required checks is the merge gate** (see the [Pull Request Standard](pull-request-standard.md)).
2. **Teammate review (optional).** A human approval is **not required** to merge. A teammate may still
   review and weigh in — and for higher-risk areas, should be asked to.

!!! note "The person merging owns the result"
    Automated review is the gate, not a guarantee. Whoever merges is accountable for the change in the
    environment it lands in.

## Automated review is addressed in full

- Automated review (e.g. CodeRabbit, Copilot) runs on every PR.
- The author addresses **every** comment it raises — fix it, or reply with the reason it doesn't apply.
- **Nothing is left unanswered.** An open automated-review comment is unfinished work.

## When to pull in a teammate

Even though human approval isn't gated, ask a teammate to look when the change touches:

- **Security, authentication, or authorization**
- **Payments or billing**
- **Shared utilities, data migrations, or infrastructure**
- **Personal data (PII)**, or **prompt changes that affect other agent flows**

Route these through **CODEOWNERS** so the right people are asked automatically.

### Reviews route through CODEOWNERS

Every repository has a `CODEOWNERS` file (provided by the template) mapping paths to the teams responsible
for them. Because access is managed through teams, ownership is too — assign ownership to **teams**, not
individuals, so a request never blocks on one person.

```
# Example CODEOWNERS
*                   @tenacious/tenacious-engineering
/billing/           @tenacious/billing-team
/infra/             @tenacious/platform-team
```

## What a reviewer checks

Whether it's automated review or a teammate, review looks at the same things:

- **Correctness** — does it do what it claims, including edge cases?
- **Requirement match** — does it solve the *stated* problem (see the [Engineering Baseline](engineering-baseline-standard.md#human-self-review))?
- **Readability** — will the next engineer understand this in six months?
- **Tests** — is the change covered, and do the tests actually prove the behavior (see the [Manual Testing Framework](manual-testing-standard.md))?
- **Security** — no injected vulnerabilities, no secrets, input is validated (see [Security](security-standard.md)).
- **Scope** — does the PR do one thing, or should it be split?

## How to give a good teammate review

- Be specific and kind. Critique the code, not the person.
- Distinguish **blocking** issues from **suggestions**. Prefix non-blocking comments with `nit:`.
- Explain *why*, and propose an alternative where you can.
- Review promptly — aim for a first pass within **one business day**; hotfixes get an **immediate** look.

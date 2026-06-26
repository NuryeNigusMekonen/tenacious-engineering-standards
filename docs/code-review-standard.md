# Code Review Standard

Code review protects quality and spreads knowledge across the team. This standard defines what authors
and reviewers are responsible for.

## Every change is reviewed

- At least **one approving review** is required before merging to `main`.
- Reviews are required by branch protection and cannot be bypassed (see the [Branching Standard](branching-standard.md)).
- Reviewers are routed automatically through **CODEOWNERS** so the right people are asked.

For higher-risk areas (security, payments, infrastructure), require review from the relevant code owners.

## Reviews route through CODEOWNERS

Every repository has a `CODEOWNERS` file (provided by the template) mapping paths to the teams
responsible for them. Because access is managed through teams, ownership is too - assign ownership to
**teams**, not individuals, so reviews don't block on one person.

```
# Example CODEOWNERS
*                   @tenacious/tenacious-engineering
/billing/           @tenacious/billing-team
/infra/             @tenacious/platform-team
```

## What reviewers check

- **Correctness** - does it do what it claims, including edge cases?
- **Readability** - will the next engineer understand this in six months?
- **Tests** - is the change covered, and do the tests actually test the behavior?
- **Security** - no injected vulnerabilities, no secrets, input is validated (see [Security](security-standard.md)).
- **Standards** - does it follow our branching, PR, and CI/CD standards?
- **Scope** - does the PR do one thing, or should it be split?

## How to give a good review

- Be specific and kind. Critique the code, not the person.
- Distinguish **blocking** issues from **suggestions**. Prefix non-blocking comments with `nit:`.
- Explain *why*, and propose an alternative where you can.
- Approve when the change is good enough to ship - not only when it is perfect.
- Review promptly. A PR waiting on review is blocked work.

## Author responsibilities

- Keep the PR small and well-described (see the [Pull Request Standard](pull-request-standard.md)).
- Respond to every comment; resolve it or explain your reasoning.
- Re-request review after addressing feedback.
- Don't merge with unresolved blocking comments.

## Review turnaround

- Aim to give a first review within **one business day**.
- Hotfixes get an **immediate** review (see the [Branching Standard](branching-standard.md)).

!!! note "Approving means you share ownership"
    When you approve a PR, you are vouching for it. Review as if you'll be on call for the result.

# Pull Request Standard

Every merge into a protected branch (`dev`, `staging`, `production`) arrives through a pull request (PR).
This standard defines how to open, describe, and merge them. The branch model and promotion rules live in
the [Branch Strategy & Pull Requests](branching-standard.md) standard.

## When to open a PR

- Open a PR for **every** change merged into a protected branch — features, fixes, docs, and chores alike.
- Open it early as a **draft** if you want CI feedback or early discussion before the work is finished.
- Mark it ready only when it is complete, self-reviewed (see the [Engineering Baseline](engineering-baseline-standard.md)),
  and CI is green.

## Keep PRs small

Small PRs are reviewed faster, more thoroughly, and merged sooner. A good PR does **one thing**.

- Aim for a few hundred changed lines or fewer.
- If a change is large, split it into a stack of focused PRs.
- Separate refactors from behavior changes so each can be reasoned about on its own.

## PR description

Every PR uses the repository's pull request template. The description is **what changed and why, in plain
language — not a restatement of the diff.** A good description includes:

- **What** - a short summary of the change.
- **Why** - the motivation or the ticket it resolves (link the issue, e.g. `Closes ACME-123`).
- **How** - notable implementation decisions or trade-offs.
- **Testing** - how the change was verified (see the [Manual Testing](manual-testing-standard.md) standard).
- **Screenshots / output** - for user-facing or behavioral changes.
- **Risk and rollback** - anything reviewers should watch for, and how to revert if needed.

```markdown
## What
Adds invoice export to CSV from the billing dashboard.

## Why
Closes ACME-123. Finance needs exports for monthly reconciliation.

## How
New `InvoiceExporter` service; streams rows to avoid loading all invoices in memory.

## Testing
Unit tests for the exporter; ran the frozen manual task set in staging (10k invoices).

## Risk / rollback
Read-only feature. Revert the PR to disable.
```

## The merge gate: automated review + required checks

A PR is gated on **automated review and required status checks**, not on a human approval.

- [ ] **Automated review has run** (e.g. CodeRabbit, Copilot) and every comment is addressed — fixed, or
      answered with the reason it doesn't apply. **Nothing is left unanswered.**
- [ ] **CI checks pass** — build, lint/format, tests, and secret scan (see the [CI/CD Standard](ci-cd-standard.md)).
- [ ] The branch is up to date with its target branch.
- [ ] No secrets or sensitive data are included (see [Key Management](secrets-management-standard.md)).

A teammate **may** review and weigh in, but a human approval is **not** required before merge.

!!! note "The person merging owns the result"
    Passing automated review is the gate, not a substitute for judgment. Whoever merges is accountable for
    the change in the environment it lands in.

## Merging

- **Squash and merge** is the default, producing one clean commit on the target branch.
- The squash commit message must be meaningful — it becomes the permanent history entry and feeds release notes.
- Delete the branch after merge.

## Authoring etiquette

- Address every automated-review comment; resolve it or explain why it doesn't apply.
- Complete your own [Engineering Baseline](engineering-baseline-standard.md) self-review before marking the PR ready.
- Re-run automated review after pushing changes in response to feedback.

!!! note "Draft PRs"
    Opening a draft PR early gives reviewers context and lets CI catch issues before the work is finished.

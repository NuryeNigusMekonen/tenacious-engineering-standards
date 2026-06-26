# Pull Request Standard

Every change to `main` arrives through a pull request (PR). This standard defines how to open, describe,
and merge them.

## When to open a PR

- Open a PR for **every** change merged into `main` — features, fixes, docs, and chores alike.
- Open it early as a **draft** if you want CI feedback or early discussion before the work is finished.
- Mark it ready for review only when it is complete and CI is green.

## Keep PRs small

Small PRs are reviewed faster, more thoroughly, and merged sooner. A good PR does **one thing**.

- Aim for a few hundred changed lines or fewer.
- If a change is large, split it into a stack of focused PRs.
- Separate refactors from behavior changes so reviewers can reason about each.

## PR description

Every PR uses the repository's pull request template. A good description includes:

- **What** — a short summary of the change.
- **Why** — the motivation or the ticket it resolves (link the issue, e.g. `Closes ACME-123`).
- **How** — notable implementation decisions or trade-offs.
- **Testing** — how the change was verified.
- **Screenshots / output** — for user-facing or behavioral changes.
- **Risk and rollback** — anything reviewers should watch for, and how to revert if needed.

```markdown
## What
Adds invoice export to CSV from the billing dashboard.

## Why
Closes ACME-123. Finance needs exports for monthly reconciliation.

## How
New `InvoiceExporter` service; streams rows to avoid loading all invoices in memory.

## Testing
Unit tests for the exporter; manually exported 10k invoices in staging.

## Risk / rollback
Read-only feature. Revert the PR to disable.
```

## Requirements before merging

A PR may only be merged when:

- [ ] CI checks pass (see the [CI/CD Standard](ci-cd-standard.md)).
- [ ] It has the required approving review(s) (see the [Code Review Standard](code-review-standard.md)).
- [ ] All review comments are resolved.
- [ ] The branch is up to date with `main`.
- [ ] No secrets or sensitive data are included (see [Secrets Management](secrets-management-standard.md)).

## Merging

- **Squash and merge** is the default, producing one clean commit on `main`.
- The squash commit message must be meaningful — it becomes the permanent history entry and feeds release notes.
- Delete the branch after merge.

## Authoring etiquette

- Respond to every review comment; resolve it or explain why not.
- Re-request review after pushing changes in response to feedback.
- Don't merge your own PR without the required approval, even if you have permission to.

!!! tip "Draft early, polish late"
    Opening a draft PR early gives reviewers context and lets CI catch issues before the work is "done".

# Branching Standard

This standard defines our branching model and naming conventions. A consistent branching model keeps
history readable and makes it obvious what every branch is for.

## The model

We use a **trunk-based** model with short-lived feature branches:

- `main` is the single long-lived branch. It is always releasable.
- All work happens on short-lived branches created from `main`.
- Branches are merged back into `main` through a pull request - never by direct push.

Keep branches small and short-lived. A branch that lives for weeks accumulates conflicts and risk.
Aim to merge within a few days.

## `main` is protected

`main` must have branch protection enabled (configured by the template). Required settings:

- Require a pull request before merging.
- Require at least one approving review (see the [Code Review Standard](code-review-standard.md)).
- Require status checks to pass (see the [CI/CD Standard](ci-cd-standard.md)).
- Require branches to be up to date before merging.
- Disallow force pushes and branch deletion on `main`.

!!! warning "No direct pushes to main"
    Nobody pushes directly to `main`, including maintainers. All changes go through a pull request.

## Branch naming

Use a `type/short-description` format in kebab-case. Where a ticket exists, include its ID.

```
<type>/<ticket-id>-<short-description>
```

| Type | Use for |
| --- | --- |
| `feature/` | New functionality |
| `fix/` | Bug fixes |
| `chore/` | Tooling, dependencies, non-functional maintenance |
| `docs/` | Documentation-only changes |
| `refactor/` | Restructuring without behavior change |
| `hotfix/` | Urgent production fixes |

Examples:

```
feature/ACME-123-add-invoice-export
fix/ACME-456-null-pointer-on-login
docs/update-onboarding-guide
hotfix/restore-payment-webhook
```

## Keeping branches current

- Regularly update your branch from `main` (rebase or merge) to avoid large conflicts at the end.
- Resolve conflicts on your branch, not in `main`.
- Branches must be up to date with `main` before they can be merged.

## After merging

- Delete the branch after the pull request is merged. The remote should not accumulate stale branches.
- Squash-merge is the default so that `main` history is one commit per change. Confirm the merge strategy
  with your team if a project differs.

## Hotfixes

Production-urgent fixes still go through a pull request, but with an expedited review:

1. Branch from `main` using `hotfix/`.
2. Make the minimal change required.
3. Open a pull request, request an immediate review, and ensure CI passes.
4. Merge and trigger a release per the [Release Management Standard](release-management-standard.md).

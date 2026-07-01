# Branch Strategy

This standard defines how code moves from a developer's machine into production. Protected branches map
one-to-one to environments and promote in one direction only: **dev → staging → production**. Code never
skips a stage and never flows backward.

## The branch model

Feature branches are cut from `dev` and merge back into `dev` via pull request. Each protected branch
deploys to exactly one environment.

| Branch | Deploys to | Merges from | Protection |
| --- | --- | --- | --- |
| `production` | Production | `staging` only | No direct push. PR required; promotion approved jointly by the Tech Lead and Project Owner. |
| `staging` | Staging | `dev` only | No direct push. PR required; the Tech Lead approves promotion. |
| `dev` | Development | feature branches | No direct push. PR required; merges once automated review and required checks pass. |
| `feature/*` | - (local / dev) | cut from `dev` | Short-lived; deleted after merge. |

### One-way promotion

- **Promotion is by merge, not cherry-pick.** What runs in production is exactly what was validated in
  staging. Merging (not cherry-picking) guarantees the promoted commit is identical to the validated one.
- **Hotfixes branch from `production`**, then merge back down into `staging` and `dev` so no fix is lost.
- **Code never flows backward.** A change reaches production only by climbing dev → staging → production.

### Projects without a staging environment

Projects that have no staging environment collapse to **dev → production**, with the Tech Lead owning the
combined promotion gate. The promotion discipline does not change - only the number of stages.

## `dev` and `staging` are protected

Every protected branch requires:

- A pull request before merging - **no direct pushes**, including by maintainers.
- Automated review and required status checks to pass (see the [CI/CD Standard](ci-cd-standard.md)).
- The branch to be up to date before merging.
- Force pushes and branch deletion disabled.

!!! warning "No direct pushes to protected branches"
    Nobody pushes directly to `dev`, `staging`, or `production`. Every change goes through a pull request.

## Branch naming

Use a `type/short-description` format in kebab-case. Where a ticket exists, include its ID. Branch
prefixes and the version scheme are set per project in its conventions record and applied consistently.

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
| `hotfix/` | Urgent production fixes (branched from `production`) |

Examples:

```
feature/ACME-123-add-invoice-export
fix/ACME-456-null-pointer-on-login
docs/update-onboarding-guide
hotfix/restore-payment-webhook
```

## Keeping branches current

- Keep branches small and short-lived. A branch that lives for weeks accumulates conflicts and risk.
- Regularly update your feature branch from `dev` (rebase or merge) to avoid large conflicts at the end.
- Resolve conflicts on your branch, never on a protected branch.
- Branches must be up to date before they can be merged.

## After merging

- Delete the feature branch after the pull request is merged. The remote should not accumulate stale branches.
- Squash-merge is the default so `dev` history is one commit per change. Confirm the merge strategy with
  your team if a project differs.

## Pull requests

Every merge into a protected branch goes through a pull request. PRs are gated on **automated review and
required checks**, not on a human approval.

- **Every PR includes a description:** what changed and why, in plain language - not a restatement of the
  diff. See the [Pull Request Standard](pull-request-standard.md) for the full description format.
- **Automated review runs on every PR** (e.g. CodeRabbit, Copilot). The author addresses every comment it
  raises - fix it, or reply with the reason it doesn't apply. Nothing is left unanswered.
- **Passing automated review and required checks is the merge gate.** A teammate may review and weigh in,
  but a human approval is not required before merge. **The person merging owns the result.**

## Hotfixes

Production-urgent fixes still go through a pull request, on an expedited path:

1. Branch from `production` using `hotfix/`.
2. Make the minimal change required.
3. Open a pull request, run automated review, and ensure CI passes.
4. Merge to `production`, then merge the fix back down into `staging` and `dev` so it is not lost.
5. Cut a release per the [Release Management Standard](release-management-standard.md).

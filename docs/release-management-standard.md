# Release Management

How a validated change becomes a production release. Releases promote **dev → staging → production** (see
the [Branch Strategy](branching-standard.md)).

> **Staging is the true release gate; production is execution only.**

By the time a change reaches production, every decision has already been made in staging. The production
step deploys what staging approved — it introduces no new approval.

## Approval chain

| Stage | Validated by | Approved by |
| --- | --- | --- |
| **Dev** | Engineer who built the change | Tech Lead (with DevOps if the role exists) |
| **Staging** | Tech Lead | Tech Lead and Project Owner, **jointly — the release gate** |
| **Production** | Deployment only — no new approval | — |

- **Projects without staging** fold the staging checks into dev, with the Tech Lead owning the combined gate.
- **Rollback plan per release.** Every release names how it will be rolled back. The mechanism is defined
  at the project level (typically redeploying the previous version). Keep the previous release deployable
  at all times.

## Release record and versioning

Maintain a **two-part record** in the release tracker:

1. **A per-release log** — what shipped, when, and by whom.
2. **A current-state environments view** — what version each environment is on.

**Credentials never appear in the tracker — a pointer only** (see [Key Management](secrets-management-standard.md)).

### Versioning

Use **semantic versioning** with four release types:

| Type | Meaning |
| --- | --- |
| **First Release** | The initial production release of the project. |
| **Major** | A significant, named release — the name is drawn from the project's codename pool. |
| **Minor** | New, backward-compatible functionality. |
| **Patch** | Backward-compatible bug fixes, including hotfixes. |

Branch prefixes and the exact version scheme are set per project in its conventions record.

## The release process

1. Confirm the change has passed manual validation (see the [Manual Testing Framework](manual-testing-standard.md))
   and, where it exists, the automated suite (see the [Automation Test Standard](automation-testing-standard.md)).
2. Promote `dev → staging` (Tech Lead approves).
3. Validate in staging against the stated criteria.
4. **Promote `staging → production` through the joint gate** (Tech Lead and Project Owner). This is the
   release gate.
5. Deploy to production — execution only, no new approval.

## Hotfix releases

For urgent production fixes (see the [Branch Strategy](branching-standard.md) hotfix flow):

1. Merge the reviewed `hotfix/` PR into `production`, then merge the fix back down into `staging` and `dev`.
2. Cut a **Patch** release.
3. Record it in the release log and update the environments view.

## After the release

1. **Update the environments view** to the new production version.
2. **Add the entry to the release log** (what shipped, when, by whom).
3. **Announce in the project channel** — what shipped and anything the team needs to know.

!!! note "Staging is the gate"
    A release reaching production always passes through the staging gate. No release skips staging (or, on
    projects without one, the combined dev gate the Tech Lead owns).

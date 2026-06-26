# Release Management Standard

A release is a deliberate, traceable act. This standard defines how we version, tag, and ship releases
so that we always know what is running and can roll back if needed.

## Versioning

We use [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`.

| Bump | When |
| --- | --- |
| **MAJOR** (`1.x.x` → `2.0.0`) | Backward-incompatible changes. |
| **MINOR** (`x.1.x` → `x.2.0`) | New, backward-compatible functionality. |
| **PATCH** (`x.x.1` → `x.x.2`) | Backward-compatible bug fixes. |

Pre-release work may use suffixes like `1.4.0-rc.1`.

## Releases are tagged

- Every release is a **git tag** in the form `vMAJOR.MINOR.PATCH` (e.g. `v1.4.0`) on a commit in `main`.
- Create a corresponding **GitHub Release** from the tag.
- A release maps to exactly one commit, so we always know precisely what shipped.

## Release notes

Every release has notes describing what changed, grouped by:

- **Added** - new features.
- **Changed** - changes to existing behavior.
- **Fixed** - bug fixes.
- **Security** - security-relevant changes.

Because we squash-merge PRs with meaningful messages (see the [Pull Request Standard](pull-request-standard.md)),
release notes can largely be assembled from merged PR titles. Maintain a `CHANGELOG.md` where the project warrants it.

## Release process

1. Confirm `main` is green: all CI checks pass (see the [CI/CD Standard](ci-cd-standard.md)).
2. Decide the version bump based on what changed since the last release.
3. Update the changelog / version metadata via a pull request.
4. Tag the release commit (`vX.Y.Z`) and create the GitHub Release with notes.
5. The tag triggers the deployment pipeline to **staging**.
6. Verify in staging.
7. **Promote to production through the approval gate** (see the [CI/CD Standard](ci-cd-standard.md)).

## Hotfix releases

For urgent production fixes (see the [Branching Standard](branching-standard.md)):

1. Merge the reviewed `hotfix/` PR into `main`.
2. Cut a **PATCH** release and tag it.
3. Promote through staging to production via the normal gate, expedited.

## Rollback

- Every release is tagged, so rollback means redeploying the previous tag.
- Keep the previous release deployable at all times.
- Prefer rolling **forward** with a fix when safe; roll **back** when a fix would take too long.

!!! note "Production deploys are gated"
    A release reaching production always passes through the approval gate. No release skips staging.

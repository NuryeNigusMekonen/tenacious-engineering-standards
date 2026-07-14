# Standards Summary

A one-page digest of the onboarding guide and 11 standards in [`docs/`](docs/) (everything except
the homepage, `docs/index.md`). The README and
[`docs/index.md`](docs/index.md) each summarize the repository as a whole; this file goes one
level deeper and gives the single core rule of every individual standard, so a reader can scan
the whole set in under a minute before opening the page they actually need.

| Standard | Core rule in one line |
| --- | --- |
| [Onboarding Guide](docs/onboarding-guide.md) | Get added to the right GitHub team, skim every standard once, then follow the same daily build loop (branch → self-check → PR → review → merge → test → promote) for every change, regardless of size. |
| [Repository Management](docs/repository-management-standard.md) | Every repository starts from the approved template (never built up by hand), is named `tenacious-<project>` or `<client>-<project>`, and grants access only through GitHub Teams, never to individuals. |
| [Engineering Baseline](docs/engineering-baseline-standard.md) | Before opening a PR, the engineer runs both automated review (CodeRabbit or equivalent) and a four-question human self-review — requirement match, risk outside scope, maintainability, and whether tests actually prove the behavior. |
| [Branch Strategy](docs/branching-standard.md) | Protected branches promote `dev → staging → production`, one direction only, by merge (not cherry-pick); nobody pushes directly to a protected branch; hotfixes branch from `production` and merge back down. |
| [Pull Requests](docs/pull-request-standard.md) | Every merge into a protected branch goes through a small, described PR (what/why/how/testing/risk); the merge gate is passing automated review and required checks, not a human approval. |
| [Code Review](docs/code-review-standard.md) | Self-review plus automated review is the mandatory gate; teammate review is optional in general but should be pulled in — via CODEOWNERS — for security, billing, shared infrastructure, PII, or agent-prompt changes. |
| [Key Management](docs/secrets-management-standard.md) | Every environment is isolated, every key is scoped and capped, and no credential ever lives in the repository; a pre-commit hook blocks new leaks and `make secret-scan` audits history; a suspected leak is rotated immediately, not just cleaned up. |
| [CI/CD](docs/ci-cd-standard.md) | The Makefile is the permanent local operating contract; CI runs the exact same targets (`build`, `lint`, `test`, `secret-scan`) on every pull request, and production deploys sit behind an approval gate. |
| [Manual Testing](docs/manual-testing-standard.md) | A tester validates the change against stated criteria — not "looks fine" — before promotion to staging and production, recording test cases, results, defects, and evidence, with a `go` / `hold` / `go with accepted risk` recommendation. |
| [Automation Testing](docs/automation-testing-standard.md) | `make test` is the mandatory CI entry point; automate stable, repeatable, high-value checks at the lowest reliable layer (unit before integration before end-to-end), starting from a manual check that's already understood. |
| [Release Management](docs/release-management-standard.md) | Staging is the true release gate — the Tech Lead and Project Owner jointly approve promotion to production — and production deployment itself introduces no new approval; every release has a named rollback plan. |
| [Security](docs/security-standard.md) | Security is built in from the first commit: `SECURITY.md`, dependency/code/secret scanning, least-privilege team-based access, parameterized queries, and immediate rotation the moment a secret is suspected of leaking. |

## The thread connecting all of them

Read top to bottom, the standards trace one change's path end to end: **Onboarding** gets you set
up, **Repository Management** gives the project its shape, **Engineering Baseline** is what you do
before anyone else sees your code, **Branch Strategy** and **Pull Requests** get it merged,
**Code Review** and **Key Management** are the checks riding along on every PR, **CI/CD** proves it
automatically, **Manual** and **Automation Testing** prove it works, **Release Management** ships
it, and **Security** is the constraint that applies to every step of the loop, not a separate one.

# CI/CD Standard

CI/CD is the infrastructure that makes environments safe. Automation is what lets us trust that a branch
is promotable to its next environment.

## The Makefile is the operating contract

**The Makefile is the permanent local operating contract on every project** — not scaffolding to be
replaced. It is the single command surface for build, run, lint, and test on a developer's machine and
stays for the life of the engagement.

CI/CD layers on top of it: **CI runs the same Makefile targets a developer runs locally**, so local and
pipeline behavior stay identical. If `make test` passes on your machine, it passes the same way in CI.

## When CI/CD is mandatory

- **Engagements expected to exceed three months** (guidance, not a firm rule) set up CI/CD, established in
  the back half of the early phase once the Makefile and environments are stable.
- **Shorter engagements** may run on the Makefile alone if the Tech Lead judges a pipeline isn't warranted.

## What must be automated on every pull request

CI runs on **every pull request** into a protected branch. At minimum it must run and pass:

- **Build / compile / render** — the project builds cleanly from a clean checkout.
- **Lint and format check** — fails on new warnings or unformatted code.
- **Tests** — the relevant test suite runs and must pass.
- **Secret scan** — the diff is scanned for committed credentials, running the same `make secret-scan`
  that backs the pre-commit hook, so CI is a second net behind it (see [Key Management](secrets-management-standard.md)).

These are the **required merge checks** behind the PR merge gate (see the [Pull Request Standard](pull-request-standard.md)).
A PR cannot merge until they pass.

```yaml
# Illustrative .github/workflows/ci.yml — CI calls the same Makefile targets you run locally
name: CI
on:
  pull_request:
  push:
    branches: [dev, staging, production]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: make build
      - name: Lint
        run: make lint
      - name: Test
        run: make test
      - name: Secret scan
        run: make secret-scan
```

## What is handled per project

- **Deployment automation** — auto-deploy on merge to an environment branch vs. a manual trigger — is a
  project decision based on maturity and client setup. Whatever the choice:
    - Promotion still follows the [Branch Strategy](branching-standard.md) (dev → staging → production).
    - Release gating still follows the [Release Management Standard](release-management-standard.md).
    - Automation speeds the mechanics; **it does not remove the approval gate.**

### Deployment principles

- Deployments are performed by **pipelines, not by hand**. No manual copying of artifacts to servers.
- Each environment is a separate, named target.
- **Production deploys require an approval gate** — use GitHub Environments with protection rules to
  enforce approvals and restrict who can deploy.
- Credentials come from the secret store, never from committed files. Workflows run with **minimal,
  scoped permissions** (see [Key Management](secrets-management-standard.md)).

## Pipeline principles

- **Fast** — keep CI under ~10 minutes so it doesn't slow down the loop. Cache dependencies; parallelize jobs.
- **Reliable** — a flaky pipeline trains people to ignore failures. Fix or quarantine flaky tests immediately.
- **Reproducible** — pin action and tool versions so a green build today is a green build tomorrow.

!!! warning "A red pipeline blocks merge"
    Do not merge by overriding failing checks. Fix the failure or fix the test.

# CI/CD Standard

Every repository has automated continuous integration (CI) and, where it deploys, continuous delivery (CD).
Automation is what lets us trust that `main` is always releasable.

## Continuous integration

CI runs on **every pull request** and on every push to `main`. The pipeline is provided by the template
and lives in `.github/workflows/`.

### Required checks

At minimum, CI must run and pass:

- **Build** - the project compiles / builds successfully.
- **Lint and format** - code style is enforced automatically, not by hand in review.
- **Tests** - the automated test suite runs and passes.
- **Security scanning** - dependency and code scanning (see the [Security Standard](security-standard.md)).
- **Secret scanning** - no secrets are present in the diff (see [Secrets Management](secrets-management-standard.md)).

These checks are **required status checks** in branch protection. A PR cannot merge until they pass.

```yaml
# Illustrative .github/workflows/ci.yml
name: CI
on:
  pull_request:
  push:
    branches: [main]
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
```

## Continuous delivery

For projects that deploy:

- Deployments are performed by **pipelines, not by hand**. No manual copying of artifacts to servers.
- Each environment (`staging`, `production`) is a separate, named target.
- Changes flow `main` → `staging` → `production`. Nothing reaches production without passing through staging.

### Deployment gates

- **Production deploys require an approval gate** - a human approves the promotion to production.
- Production deploys are tied to releases (see the [Release Management Standard](release-management-standard.md)).
- Use GitHub Environments with protection rules to enforce approvals and restrict who can deploy.

## Pipeline principles

- **Fast** - keep CI under ~10 minutes so it doesn't slow down review. Cache dependencies; parallelize jobs.
- **Reliable** - a flaky pipeline trains people to ignore failures. Fix or quarantine flaky tests immediately.
- **Reproducible** - pin action and tool versions so a green build today is a green build tomorrow.
- **Least privilege** - workflows use scoped, minimal permissions and pull credentials from the secret store,
  never from committed files (see [Secrets Management](secrets-management-standard.md)).

!!! warning "A red pipeline blocks merge"
    Do not merge by overriding failing checks. Fix the failure or fix the test.

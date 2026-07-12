# README Review

Three concrete improvements for `README.md`.

## 1. Add a badges row and a "view the live site" link

The repo builds and deploys to GitHub Pages via `.github/workflows/deploy-docs.yml`, and
`mkdocs.yml` already declares `site_url: https://nuryenigusmekonen.github.io/tenacious-engineering-standards/`.
None of this is surfaced in the README — a visitor can't tell at a glance whether the last
deploy succeeded, or find the published site without digging into `mkdocs.yml`.

**Suggested change**, right under the H1:

```markdown
# Tenacious Engineering Standards

[![Deploy Docs](https://github.com/NuryeNigusMekonen/tenacious-engineering-standards/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/NuryeNigusMekonen/tenacious-engineering-standards/actions/workflows/deploy-docs.yml)

**[View the published site →](https://nuryenigusmekonen.github.io/tenacious-engineering-standards/)**
```

## 2. Turn "Reading the standards" into a full index

The README links to only 3 of the 12 documents registered under `nav:` in `mkdocs.yml`
(the homepage, the Onboarding Guide, and the Repository Management Standard). A reader has
to open `mkdocs.yml` or browse `docs/` to discover the rest exist. Since the README's job is
to orient a new reader, it should mirror the nav as a scannable list.

**Suggested change**, expanding the "Reading the standards" section:

```markdown
## Reading the standards

The standards live in [`docs/`](docs/). Start with the [homepage](docs/index.md) and the
[Onboarding Guide](docs/onboarding-guide.md), then read the standard relevant to your task:

- [Repository Management](docs/repository-management-standard.md) - project init checklist
- [Engineering Baseline](docs/engineering-baseline-standard.md)
- [Branch Strategy](docs/branching-standard.md)
- [Pull Requests](docs/pull-request-standard.md)
- [Code Review](docs/code-review-standard.md)
- [Key Management](docs/secrets-management-standard.md)
- [CI/CD](docs/ci-cd-standard.md)
- [Manual Testing](docs/manual-testing-standard.md)
- [Automation Testing](docs/automation-testing-standard.md)
- [Release Management](docs/release-management-standard.md)
- [Security](docs/security-standard.md)
```

## 3. State the license/usage terms

`mkdocs.yml` sets `copyright: Copyright © Tenacious Intelligence Corporation - internal
reference, maintained as code`, but there is no `LICENSE` file and the README never states
that this is an internal/proprietary reference rather than an openly licensed project. An
external reader (or a fork) has no way to know the intended usage terms.

**Suggested change**, a short section near the bottom of the README:

```markdown
## License

This repository is an internal reference for Tenacious Intelligence Corporation and is not
licensed for external use or redistribution.
```

(or, if it should be open, add an actual `LICENSE` file and link to it here instead).

---

No existing files were modified for this review; this file only records suggestions.

# Tenacious Engineering Standards

The official reference for how engineering work moves from a developer's machine to a production release
at Tenacious. This repository documents the single development-side standard: repository setup, the
engineering baseline, branch strategy and pull requests, code review, key management, CI/CD, manual and
automation testing, and release management.

It is published as a documentation site using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
and deployed to GitHub Pages via GitHub Actions.

## Who this is for

- **Engineers** - the day-to-day rules for working in our repositories.
- **Engineering managers** - the reference for onboarding, access management, and project setup.
- **New team members** - start with the [Onboarding Guide](docs/onboarding-guide.md).

## Core rules at a glance

- Every new repository must start from the approved template.
- External client project repositories must include the client name and project name.
- All contributors are added through GitHub Teams - never as individual collaborators.
- Protected branches promote **dev → staging → production**, one direction only - code never skips a stage or flows backward.
- Passing automated review and required checks is the merge gate; the person merging owns the result.
- Every environment is isolated, every key is scoped and capped, and no credential ever lives in the repository.
- A change is validated against stated criteria before promotion - never on "looks fine."

## Reading the standards

The standards live in [`docs/`](docs/). Start with the [homepage](docs/index.md), then read the
standard relevant to your task. The [Repository Management Standard](docs/repository-management-standard.md)
includes the project initialization checklist used at the start of every project.

## Local development

```bash
# Install dependencies
pip install mkdocs-material

# Serve the site locally with live reload
mkdocs serve

# Build the static site
mkdocs build
```

Then open <http://127.0.0.1:8000>.

## How to contribute

1. Create a branch from `main` following the [Branching Standard](docs/branching-standard.md).
2. Edit or add Markdown files in `docs/`.
3. If you add a new page, register it under `nav:` in [`mkdocs.yml`](mkdocs.yml).
4. Open a pull request following the [Pull Request Standard](docs/pull-request-standard.md).

## Deployment

Pushing to `main` triggers the [GitHub Actions workflow](.github/workflows/deploy-docs.yml)
that builds the site and publishes it to GitHub Pages.

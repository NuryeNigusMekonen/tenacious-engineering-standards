# Tenacious Engineering Standards

The official reference for how we build and operate software at Tenacious. This repository
documents our standards for GitHub repository setup, project management, branching, pull
requests, code review, CI/CD, security, secrets management, and releases.

It is published as a documentation site using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
and deployed to GitHub Pages via GitHub Actions.

## Who this is for

- **Engineers** - the day-to-day rules for working in our repositories.
- **Engineering managers** - the reference for onboarding, access management, and project setup.
- **New team members** - start with the [Onboarding Guide](docs/onboarding-guide.md).

## Core rules at a glance

- Every new repository must start from the approved template.
- External client project repositories must include the client name and project name.
- Every external client project must have a GitHub team named after the client.
- All contributors must be added through GitHub Teams - never as individual collaborators.
- Internal projects must use the internal GitHub team.
- Access is managed through teams, not individuals.
- Every project must follow our branch, PR, review, CI/CD, security, secrets, and release standards.

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

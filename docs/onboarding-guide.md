# Onboarding Guide

Welcome to Tenacious. This guide gets you productive quickly and points you to the standards you'll
use every day. Read it first, then keep the standards bookmarked.

## For new engineers

### Day one

1. Make sure you've been added to the right **GitHub team** (your manager handles this). At Tenacious,
   access is granted through teams - you get repository access by being on the internal team or a client
   team, not by being added to repos individually.
2. Read the [Home page](index.md) to understand why we have standards.
3. Skim every standard once so you know what exists:
    - [Repository Management](repository-management-standard.md)
    - [Branching](branching-standard.md)
    - [Pull Requests](pull-request-standard.md)
    - [Code Review](code-review-standard.md)
    - [CI/CD](ci-cd-standard.md)
    - [Security](security-standard.md)
    - [Secrets Management](secrets-management-standard.md)
    - [Release Management](release-management-standard.md)

### Your first change

Follow this flow - it's the same one for every change you'll ever make here:

1. Create a branch from `main` following the [Branching Standard](branching-standard.md)
   (e.g. `feature/ACME-123-add-export`).
2. Make your change. Keep secrets out of the code (see [Secrets Management](secrets-management-standard.md)).
3. Push and open a pull request using the template, following the [Pull Request Standard](pull-request-standard.md).
4. Make sure CI passes (see the [CI/CD Standard](ci-cd-standard.md)).
5. Get an approving review (see the [Code Review Standard](code-review-standard.md)).
6. Squash-merge, and delete your branch.

That's it. If you can do this loop comfortably, you know how we work.

## For engineering managers

### Starting a new project

Use the [Repository Management Standard](repository-management-standard.md) and its
**project initialization checklist**. In short:

1. Apply the **approved template structure** using the integration command - it works for both new and
   existing repositories (see [Repository Management](repository-management-standard.md#integrating-the-template)).
2. Name it correctly:
    - Internal: `tenacious-<project>`.
    - Client: `<client>-<project>`, and put the **client name and project name** in the repo description.
3. Set up the team:
    - Client projects need a **GitHub team named after the client**; add all contributors through it.
    - Internal projects use the **internal GitHub team**.
4. Confirm access is granted to the **team**, not to individuals.
5. Walk the rest of the [initialization checklist](repository-management-standard.md#5-project-initialization-checklist)
   before development begins.

### Adding and removing people

- Add people to the relevant **team**; never add them as individual repository collaborators.
- Remove people from the team when they leave the project - this revokes their access everywhere at once.

## Editing these standards

This site is just Markdown. To propose a change:

1. Branch from `main`.
2. Edit or add a file in [`docs/`](https://github.com/NuryeNigusMekonen/tenacious-engineering-standards/tree/main/docs).
3. If you add a page, register it under `nav:` in `mkdocs.yml`.
4. Open a PR following the [Pull Request Standard](pull-request-standard.md).

Standards improve through the same review process as our code. If something here is wrong or outdated,
fixing it is a welcome contribution.

!!! tip "Run the site locally"
    ```bash
    pip install mkdocs-material
    mkdocs serve
    ```
    Then open <http://127.0.0.1:8000> to preview your changes with live reload.

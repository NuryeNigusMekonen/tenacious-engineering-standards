# Onboarding Guide

Welcome to Tenacious. This guide gets you productive quickly and points you to the standards you'll
use every day. Read it first, then keep the standards bookmarked.

## For new engineers

### Day one

1. Confirm you've been added to the right **GitHub team** (your manager handles this) - access comes from
   team membership, not from being added to repos individually.
2. Read the [Home page](index.md) to understand why we have standards.
3. Skim each standard once (links in the left sidebar) so you know what exists and where to find it later.

### Your first change

Follow this flow - it's the same daily build loop for every change you'll ever make here:

1. Create a feature branch from `dev` following the [Branch Strategy](branching-standard.md)
   (e.g. `feature/ACME-123-add-export`).
2. Make your change. Keep credentials out of the code (see [Key Management](secrets-management-standard.md)).
3. **Self-check your work** - run automated review and the four-question self-review in the
   [Engineering Baseline](engineering-baseline-standard.md) before anyone else sees it.
4. Push and open a pull request into `dev` using the template (see the [Pull Request Standard](pull-request-standard.md)).
5. Make sure automated review is addressed and CI passes - that's the merge gate (see [CI/CD](ci-cd-standard.md)).
6. Squash-merge into `dev`, and delete your branch.
7. Before promotion to staging, the change is validated against stated criteria (see [Manual Testing](manual-testing-standard.md)),
   then promoted `dev → staging → production` (see [Release Management](release-management-standard.md)).

Every change follows this loop, regardless of size.

## For engineering managers

### Starting a new project

The full process lives in the [Repository Management Standard](repository-management-standard.md). The essentials:

1. Apply the **approved template structure** with the integration command - it works for new and
   existing repos (see [Integrating the template](repository-management-standard.md#integrating-the-template)).
2. Name it by convention: `tenacious-<project>` internally, or `<client>-<project>` for client work
   (with the client and project name in the repo description).
3. Grant access to a **team, never to individuals**: a team named after the client for client work, or
   the internal team otherwise.

Then walk the full [initialization checklist](repository-management-standard.md#5-project-initialization-checklist)
before development begins.

### Adding and removing people

- Add people to the relevant **team**; never add them as individual repository collaborators.
- Remove people from the team when they leave the project - this revokes their access everywhere at once.

## Editing these standards

This site is just Markdown. To propose a change:

1. Branch from `dev`.
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

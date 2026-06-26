# Tenacious Engineering Standards

Welcome to the official reference for how we build and operate software at Tenacious.

These standards exist so that every repository, on every project, looks and behaves the same way.
When a new engineer joins a project, or a manager audits one, they should find the same structure,
the same branching model, the same review process, and the same release flow everywhere. Consistency
is what lets us move quickly without losing control.

## Why standards

- **Predictability** — anyone can move between projects and immediately know how things work.
- **Quality** — shared rules for reviews, CI/CD, and security raise the floor on everything we ship.
- **Onboarding** — new engineers ramp up against one documented way of working, not tribal knowledge.
- **Client trust** — external client projects are set up consistently, with clear ownership and access control.
- **Auditability** — access, secrets, and releases follow rules that can be checked and proven.

## The core rules

These apply to **every** project, internal or external:

- Every new repository **must start from the approved template**.
- External client project repositories **must include the client name and project name**.
- Every external client project **must have a GitHub team named after the client**.
- All contributors **must be added through GitHub Teams** — never as individual collaborators.
- Internal projects **must use the internal GitHub team**.
- Access is **managed through teams, not individuals**.
- Every project **must follow the branch, PR, review, CI/CD, security, secrets, and release standards** in this site.

## How this site is organized

| Section | What it covers |
| --- | --- |
| [Onboarding Guide](onboarding-guide.md) | Where new engineers and managers should start. |
| [Repository Management](repository-management-standard.md) | Creating repos, naming, teams, access, and the project initialization checklist. |
| [Branching](branching-standard.md) | The branching model and naming conventions. |
| [Pull Requests](pull-request-standard.md) | How to open, describe, and merge pull requests. |
| [Code Review](code-review-standard.md) | What reviewers and authors are responsible for. |
| [CI/CD](ci-cd-standard.md) | Required pipelines, checks, and deployment gates. |
| [Security](security-standard.md) | Baseline security requirements for every repo. |
| [Secrets Management](secrets-management-standard.md) | How secrets are stored, rotated, and never committed. |
| [Release Management](release-management-standard.md) | Versioning, tagging, and release process. |

## A standard is a contract

If you find a standard that no longer fits how we work, that is a signal to **update the standard**,
not to quietly ignore it. Open a pull request against this repository following the
[Pull Request Standard](pull-request-standard.md). Standards evolve through the same review process
as our code.

!!! tip "New here?"
    Start with the [Onboarding Guide](onboarding-guide.md), then read the
    [Repository Management Standard](repository-management-standard.md) before creating your first project.

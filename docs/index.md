---
hide:
  - navigation
  - toc
---

<div class="ten-hero" markdown="1">
  <img class="ten-hero-logo" src="assets/logo.svg" alt="Tenacious Intelligence logo" width="92" height="92">
  <p class="ten-eyebrow">Tenacious Intelligence</p>
  <h1>The standard for how we build software</h1>
  <p class="ten-sub">
    One consistent way to set up repositories, manage projects, and ship code —
    across every internal and client project. Predictable, secure, and auditable by default.
  </p>
  <div class="ten-cta">
    <a class="md-button md-button--primary" href="onboarding-guide/">Get started</a>
    <a class="md-button" href="repository-management-standard/">Read the standards</a>
    <a class="md-button" href="https://github.com/NuryeNigusMekonen/tenacious-engineering-standards">View on GitHub</a>
  </div>
</div>

## Why these standards exist

Every repository, on every project, should look and behave the same way. When a new engineer joins a
project — or a manager audits one — they find the same structure, branching model, review process, and
release flow everywhere. Consistency is what lets us move quickly without losing control.

- **Predictability** — anyone can move between projects and immediately know how things work.
- **Quality** — shared rules for reviews, CI/CD, and security raise the floor on everything we ship.
- **Onboarding** — new engineers ramp against one documented way of working, not tribal knowledge.
- **Client trust** — external projects are set up consistently, with clear ownership and access control.
- **Auditability** — access, secrets, and releases follow rules that can be checked and proven.

## Explore the standards

<div class="ten-cards">
<a class="ten-card" href="onboarding-guide/"><span class="ten-card-icon">🚀</span><h3>Onboarding Guide</h3><p>Where new engineers and managers start. The first-change loop, end to end.</p></a>
<a class="ten-card" href="repository-management-standard/"><span class="ten-card-icon">📦</span><h3>Repository Management</h3><p>Templates, naming, teams, access — plus the project initialization checklist.</p></a>
<a class="ten-card" href="branching-standard/"><span class="ten-card-icon">🌿</span><h3>Branching</h3><p>Our trunk-based model and branch naming conventions.</p></a>
<a class="ten-card" href="pull-request-standard/"><span class="ten-card-icon">🔀</span><h3>Pull Requests</h3><p>How to open, describe, and merge changes into <code>main</code>.</p></a>
<a class="ten-card" href="code-review-standard/"><span class="ten-card-icon">🔎</span><h3>Code Review</h3><p>What authors and reviewers are responsible for, routed via CODEOWNERS.</p></a>
<a class="ten-card" href="ci-cd-standard/"><span class="ten-card-icon">⚙️</span><h3>CI/CD</h3><p>Required pipelines, status checks, and production deployment gates.</p></a>
<a class="ten-card" href="security-standard/"><span class="ten-card-icon">🛡️</span><h3>Security</h3><p>Baseline security requirements for every repository.</p></a>
<a class="ten-card" href="secrets-management-standard/"><span class="ten-card-icon">🔐</span><h3>Secrets Management</h3><p>How secrets are stored, rotated, and never committed.</p></a>
<a class="ten-card" href="release-management-standard/"><span class="ten-card-icon">🏷️</span><h3>Release Management</h3><p>Versioning, tagging, release notes, and rollback.</p></a>
</div>

## The core rules

These apply to **every** project, internal or external:

- Every new repository **must start from the approved template**.
- External client project repositories **must include the client name and project name**.
- Every external client project **must have a GitHub team named after the client**.
- All contributors **must be added through GitHub Teams** — never as individual collaborators.
- Internal projects **must use the internal GitHub team**.
- Access is **managed through teams, not individuals**.
- Every project **must follow the branch, PR, review, CI/CD, security, secrets, and release standards** on this site.

## A standard is a contract

If you find a standard that no longer fits how we work, that is a signal to **update the standard**, not
to quietly ignore it. Open a pull request against this repository following the
[Pull Request Standard](pull-request-standard.md). Standards evolve through the same review process as
our code.

!!! tip "New here?"
    Start with the [Onboarding Guide](onboarding-guide.md), then read the
    [Repository Management Standard](repository-management-standard.md) before creating your first project.

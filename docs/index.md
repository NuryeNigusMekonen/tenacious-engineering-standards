---
hide:
  - navigation
  - toc
---

<div class="ten-hero" markdown="1">
  <span class="ten-hero-logo"><img src="assets/tenacious-logo-full.png" alt="Tenacious Intelligence Corporation"></span>
  <h1>The standard for how we build software</h1>
  <p class="ten-sub">
    One consistent way to set up repositories, manage projects, and ship code
    across every internal and client project. Predictable, secure, and auditable by default.
  </p>
  <div class="ten-cta">
    <a class="md-button md-button--primary" href="onboarding-guide/">Get started</a>
    <a class="md-button" href="repository-management-standard/">Read the standards</a>
    <a class="md-button" href="https://github.com/NuryeNigusMekonen/tenacious-engineering-standards">View on GitHub</a>
  </div>
</div>

## Why these standards exist

Every repository, on every project, should look and behave the same way. Consistency is what lets us
move quickly without losing control:

- **Predictability** - anyone can move between projects and immediately know how things work.
- **Quality** - shared rules for reviews, CI/CD, and security raise the floor on everything we ship.
- **Onboarding** - new engineers ramp against one documented way of working, not tribal knowledge.
- **Client trust** - external projects are set up consistently, with clear ownership and access control.
- **Auditability** - access, secrets, and releases follow rules that can be checked and proven.

## Explore the standards

<div class="ten-cards">
<a class="ten-card" href="onboarding-guide/"><h3>Onboarding Guide</h3><p>Where new engineers and managers start, including the first-change workflow.</p></a>
<a class="ten-card" href="repository-management-standard/"><h3>Repository Management</h3><p>Templates, naming, teams, access - plus the project initialization checklist.</p></a>
<a class="ten-card" href="branching-standard/"><h3>Branching</h3><p>Our trunk-based model and branch naming conventions.</p></a>
<a class="ten-card" href="pull-request-standard/"><h3>Pull Requests</h3><p>How to open, describe, and merge changes into <code>main</code>.</p></a>
<a class="ten-card" href="code-review-standard/"><h3>Code Review</h3><p>What authors and reviewers are responsible for, routed via CODEOWNERS.</p></a>
<a class="ten-card" href="ci-cd-standard/"><h3>CI/CD</h3><p>Required pipelines, status checks, and production deployment gates.</p></a>
<a class="ten-card" href="security-standard/"><h3>Security</h3><p>Baseline security requirements for every repository.</p></a>
<a class="ten-card" href="secrets-management-standard/"><h3>Secrets Management</h3><p>How secrets are stored, rotated, and never committed.</p></a>
<a class="ten-card" href="release-management-standard/"><h3>Release Management</h3><p>Versioning, tagging, release notes, and rollback.</p></a>
</div>

## The core rules

These apply to **every** project, internal or external:

- Every repository **must use the approved template structure** - apply it to new and existing repos with the integration command.
- Repositories are **named by convention**: `tenacious-<project>` internally, `<client>-<project>` for client work.
- Access is **managed through GitHub Teams, never individuals** - a client team for client work, the internal team otherwise.
- Every change **follows the branch, PR, review, CI/CD, security, secrets, and release standards** on this site.

## A standard is a contract

If you find a standard that no longer fits how we work, that is a signal to **update the standard**, not
to quietly ignore it. Open a pull request against this repository following the
[Pull Request Standard](pull-request-standard.md). Standards evolve through the same review process as
our code.

!!! note "Where to start"
    Read the [Onboarding Guide](onboarding-guide.md), then the
    [Repository Management Standard](repository-management-standard.md) before creating your first project.

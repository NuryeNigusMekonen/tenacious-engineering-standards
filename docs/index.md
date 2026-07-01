---
hide:
  - navigation
  - toc
---

<div class="ten-hero" markdown="1">
  <span class="ten-hero-logo"><img src="assets/tenacious-logo-full.png" alt="Tenacious Intelligence Corporation"></span>
  <h1>The standard for how we build software</h1>
  <p class="ten-sub">
    The single development-side standard for how engineering work moves from a developer's machine
    to a production release. One way to write, review, secure, test, and ship code across every engagement.
  </p>
  <div class="ten-cta">
    <a class="md-button md-button--primary" href="onboarding-guide/">Get started</a>
    <a class="md-button" href="repository-management-standard/">Read the standards</a>
    <a class="md-button" href="https://github.com/NuryeNigusMekonen/tenacious-engineering-standards">View on GitHub</a>
  </div>
</div>

<div class="ten-page" markdown="1">

## Why these standards exist

Any engineer should be able to execute from these standards alone. Every repository, on every engagement,
should look and behave the same way. Consistency is what lets us move quickly without losing control:

- **Predictability** - anyone can move between projects and immediately know how things work.
- **Quality** - shared rules for baseline checks, review, testing, and CI/CD raise the floor on everything we ship.
- **Onboarding** - new engineers ramp against one documented way of working, not tribal knowledge.
- **Client trust** - external projects are set up consistently, with clear ownership and access control.
- **Auditability** - access, keys, and releases follow rules that can be checked and proven.

## The daily build loop

The standards follow the path a change takes from a developer's machine to production:

1. **Write and self-check** — the [Engineering Baseline](engineering-baseline-standard/).
2. **Open a PR and merge into protected branches** — [Branch Strategy & Pull Requests](branching-standard/).
3. **The infrastructure that makes environments safe** — [Key Management](secrets-management-standard/) and [CI/CD](ci-cd-standard/).
4. **Prove the change works** — [Manual Testing](manual-testing-standard/) then [Automation Testing](automation-testing-standard/).
5. **Ship it** — [Release Management](release-management-standard/).

## Explore the standards

<div class="ten-cards">
<a class="ten-card" href="onboarding-guide/"><h3>Onboarding Guide</h3><p>Where new engineers and managers start, including the first-change workflow.</p></a>
<a class="ten-card" href="repository-management-standard/"><h3>Repository Management</h3><p>Templates, naming, teams, access - plus the project initialization checklist.</p></a>
<a class="ten-card" href="engineering-baseline-standard/"><h3>Engineering Baseline</h3><p>Automated review, AI-assistant rules, and the four-question self-review before any PR.</p></a>
<a class="ten-card" href="branching-standard/"><h3>Branch Strategy & PRs</h3><p>The dev → staging → production model and one-way promotion.</p></a>
<a class="ten-card" href="pull-request-standard/"><h3>Pull Requests</h3><p>How to open and describe a PR, merged on automated review, not human approval.</p></a>
<a class="ten-card" href="code-review-standard/"><h3>Code Review</h3><p>Self-review, automated review as the gate, and when to pull in a teammate.</p></a>
<a class="ten-card" href="secrets-management-standard/"><h3>Key Management</h3><p>Per-environment isolation, spend caps, AI keys, and pre-commit secret scanning.</p></a>
<a class="ten-card" href="ci-cd-standard/"><h3>CI/CD</h3><p>The Makefile contract, required PR checks, and production deployment gates.</p></a>
<a class="ten-card" href="manual-testing-standard/"><h3>Manual Testing</h3><p>Structured validation before promotion and the frozen task set.</p></a>
<a class="ten-card" href="automation-testing-standard/"><h3>Automation Testing</h3><p>Grader taxonomy, capability vs. regression, and when to start automating.</p></a>
<a class="ten-card" href="release-management-standard/"><h3>Release Management</h3><p>Staging as the release gate, the approval chain, and versioning.</p></a>
</div>

## The core rules

These apply to **every** project, internal or external:

- Every repository **must use the approved template structure** - apply it to new and existing repos with the integration command.
- Repositories are **named by convention**: `tenacious-<project>` internally, `<client>-<project>` for client work.
- Access is **managed through GitHub Teams, never individuals** - a client team for client work, the internal team otherwise.
- Protected branches promote **dev → staging → production, one direction only** - code never skips a stage or flows backward.
- **Passing automated review and required checks is the merge gate** - the person merging owns the result.
- **Every environment is isolated, every key is scoped and capped, and no credential ever lives in the repository.**
- **A change is validated against stated criteria before promotion** - never on "looks fine."

## A standard is a contract

If you find a standard that no longer fits how we work, that is a signal to **update the standard**, not
to quietly ignore it. Open a pull request against this repository following the
[Pull Request Standard](pull-request-standard.md). Standards evolve through the same review process as
our code.

!!! note "Where to start"
    Read the [Onboarding Guide](onboarding-guide.md), then the
    [Repository Management Standard](repository-management-standard.md) before creating your first project.

</div>

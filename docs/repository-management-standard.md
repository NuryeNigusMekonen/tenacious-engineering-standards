# Repository Management Standard

This standard defines how repositories are created, named, owned, and accessed at Tenacious.
It is the first standard to read before starting any project.

## 1. Every repository starts from the approved template

Every new repository **must** be created from the official Tenacious repository template. The template
provides the baseline structure that all other standards depend on:

- A starter `README.md` with the required sections.
- Pre-configured branch protection settings.
- The standard `.github/` directory: pull request template, issue templates, and CI/CD workflows.
- A baseline `.gitignore`, license, and security policy.
- The CODEOWNERS file.

Do not create empty repositories and add structure by hand. Starting from the template guarantees that
branching, PR, review, CI/CD, security, and release configuration is present from commit one.

!!! warning "No exceptions"
    A repository that was not created from the template is not considered a valid Tenacious repository.
    Recreate it from the template and migrate the code.

## 2. Repository naming

### Internal projects

Use a short, descriptive, kebab-case name:

```
tenacious-<project>
```

Examples: `tenacious-billing`, `tenacious-design-system`.

### External client projects

External client repositories **must include the client name and the project name** so ownership and
context are obvious at a glance:

```
<client>-<project>
```

Examples: `acme-mobile-app`, `globex-data-platform`.

The client name and project name must also be stated in the repository description and in the README.

## 3. Teams and access

Access at Tenacious is **managed through teams, not individuals**. We never add people as individual
repository collaborators.

### External client projects

- Every external client project **must have a GitHub team named after the client** (for example, the
  `acme` team for all Acme work).
- All contributors to the project **must be added through that client team**.
- The client team is granted access to the client's repositories; members get access by being on the team.

### Internal projects

- Internal projects **must use the internal GitHub team** (for example, the `tenacious-engineering` team).
- Contributors are added to the internal team, not to individual repositories.

### Why teams, not individuals

- Onboarding and offboarding happen in one place — add or remove a person from a team.
- Access is auditable: you can see who has access to what by looking at team membership.
- Permissions stay consistent across all of a client's or the company's repositories.

| Project type | Team requirement | Access granted to |
| --- | --- | --- |
| External client | A team named after the client | The client team |
| Internal | The internal engineering team | The internal team |

## 4. Required repository configuration

Every repository must have, from the template:

- **Branch protection** on `main` per the [Branching Standard](branching-standard.md).
- A **CODEOWNERS** file so reviews route to the right people per the [Code Review Standard](code-review-standard.md).
- **CI/CD workflows** per the [CI/CD Standard](ci-cd-standard.md).
- A **security policy** and scanning per the [Security Standard](security-standard.md).
- **No secrets in the repo**, per the [Secrets Management Standard](secrets-management-standard.md).

## 5. Project initialization checklist

Complete this checklist at the start of **every** project before writing feature code.

- [ ] Repository created from the **approved template**.
- [ ] Name follows the convention (`tenacious-<project>` for internal, `<client>-<project>` for client work).
- [ ] For client work: the repository name and description include the **client name and project name**.
- [ ] For client work: a **GitHub team named after the client** exists.
- [ ] For internal work: the **internal GitHub team** is used.
- [ ] All contributors are added **through the team**, not as individual collaborators.
- [ ] Team access level (read / write / maintain) is set correctly for the project.
- [ ] **Branch protection** on `main` is enabled (see [Branching](branching-standard.md)).
- [ ] **CODEOWNERS** file is filled in (see [Code Review](code-review-standard.md)).
- [ ] **Pull request template** is present (see [Pull Requests](pull-request-standard.md)).
- [ ] **CI/CD pipeline** runs on pull requests (see [CI/CD](ci-cd-standard.md)).
- [ ] **Security scanning** is enabled (see [Security](security-standard.md)).
- [ ] **Secrets** are configured in the secret store, not committed (see [Secrets Management](secrets-management-standard.md)).
- [ ] **Release process** is agreed and documented (see [Release Management](release-management-standard.md)).
- [ ] README describes the project, how to run it, and who owns it.

Once every box is checked, the project is ready for development.

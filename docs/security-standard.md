# Security Standard

Security is everyone's responsibility, and it is built in from the first commit — not bolted on later.
This standard defines the baseline security requirements for every Tenacious repository.

## Baseline requirements

Every repository must have, from the template:

- A **`SECURITY.md`** policy describing how to report a vulnerability.
- **Dependency scanning** enabled (e.g. Dependabot or equivalent) to flag vulnerable dependencies.
- **Code scanning** enabled (e.g. CodeQL or equivalent) running in CI.
- **Secret scanning** enabled to catch credentials before they are committed.
- **Branch protection** on `main` so unreviewed code cannot ship (see the [Branching Standard](branching-standard.md)).

## Access control

- Access is **managed through teams, not individuals** (see the [Repository Management Standard](repository-management-standard.md)).
- Grant the **least privilege** necessary: read by default, write only where needed, admin rarely.
- External client repositories are accessed only through the **client's team**.
- Review team membership and access regularly; remove access promptly when someone leaves a project.

## Dependencies

- Keep dependencies up to date; triage scanner alerts promptly.
- Prefer well-maintained, widely-used libraries over obscure ones.
- Pin versions and use lockfiles so builds are reproducible.
- Review new dependencies before adding them — every dependency is attack surface.

## Secure coding

- Validate and sanitize all external input.
- Use parameterized queries; never build SQL or shell commands by string concatenation.
- Encode output to prevent injection (XSS, command injection, etc.).
- Use vetted libraries for cryptography, authentication, and session management — do not roll your own.
- Apply least privilege to service accounts, tokens, and database users.

## Secrets

Secrets are covered in detail in the [Secrets Management Standard](secrets-management-standard.md).
The headline rule: **secrets never live in the repository.** Secret scanning enforces this in CI.

## Vulnerability response

- Report suspected vulnerabilities through the process in `SECURITY.md`.
- Triage by severity. Critical issues are treated as incidents and fixed with priority.
- Security fixes still go through a pull request and review, but on an expedited path
  (see the [Branching Standard](branching-standard.md) hotfix flow).
- After a fix, confirm scanners are clean and document what happened.

## CI/CD security

- Workflows run with **minimal, scoped permissions**.
- Credentials come from the secret store, never from committed files.
- Production deployments require an **approval gate** (see the [CI/CD Standard](ci-cd-standard.md)).

!!! danger "If you think a secret leaked"
    Treat it as compromised. Rotate it immediately and follow the
    [Secrets Management Standard](secrets-management-standard.md) — do not wait to confirm.

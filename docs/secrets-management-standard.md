# Secrets Management Standard

Secrets — passwords, API keys, tokens, certificates, connection strings — are among the most damaging
things to leak. This standard defines how we store, use, and rotate them.

## The one rule

**Secrets never live in the repository.** Not in code, not in config files, not in commit history,
not in comments, not in CI logs.

Secret scanning runs in CI (see the [Security Standard](security-standard.md)) to enforce this. A PR
containing a secret will be blocked.

## Where secrets live

- **Application/runtime secrets** live in a dedicated secret store (cloud secret manager or vault) and
  are injected at runtime as environment variables.
- **CI/CD secrets** live in GitHub Actions secrets / environment secrets, scoped to the environment
  that needs them.
- **Local development** uses a `.env` file that is **git-ignored** and never committed. Commit a
  `.env.example` with placeholder keys and no real values.

```bash
# .env.example  (committed — placeholders only)
DATABASE_URL=
STRIPE_API_KEY=
JWT_SECRET=

# .env          (git-ignored — real values, never committed)
```

Ensure `.env` is in `.gitignore` (the template includes it).

## Using secrets in code

- Read secrets from environment variables or the secret store at runtime.
- Never hard-code a secret, even temporarily "just to test".
- Never log secrets. Scrub them from error messages and debug output.
- Keep secrets out of URLs, query strings, and client-side code.

## Using secrets in CI/CD

- Store them as GitHub repository or environment secrets.
- Reference them with `${{ secrets.NAME }}`; never echo them.
- Scope production secrets to the production environment, behind the deployment approval gate
  (see the [CI/CD Standard](ci-cd-standard.md)).
- Grant workflows the minimum permissions they need.

## Rotation

- Rotate secrets on a regular schedule and whenever a person with access leaves a project.
- Rotate **immediately** on any suspected exposure.
- Prefer short-lived credentials and automatic rotation where the platform supports it.

## If a secret leaks

A leaked secret is **compromised the moment it is exposed**, even briefly. Removing it from a later
commit does not undo the leak.

1. **Rotate it immediately** — invalidate the old value and issue a new one.
2. Update the secret store and CI secrets with the new value.
3. Investigate where it leaked and what may have been accessed.
4. Purge it from history if feasible, but treat rotation — not cleanup — as the real fix.
5. Follow the vulnerability response process in the [Security Standard](security-standard.md).

!!! danger "Don't wait to be sure"
    If you *think* a secret may have leaked, rotate it. The cost of an unnecessary rotation is minutes;
    the cost of a real leak left active can be catastrophic.

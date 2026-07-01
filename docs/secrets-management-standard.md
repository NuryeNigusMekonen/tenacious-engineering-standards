# Key Management

This standard covers **all secrets** — AI/LLM provider keys, cloud credentials, third-party API keys, and
database and service tokens. The governing principle:

> **Every environment is isolated, every key is scoped and capped, and no credential ever lives in the repository.**

## Per-environment isolation

- **Separate keys per environment.** Development, staging, and production each have their own distinct
  keys for every provider. A dev key can never reach production data or production spend, and a leaked dev
  key cannot touch production.
- **AI keys are treated exactly like cloud keys.** LLM provider keys are segregated per environment and
  capped like any other paid resource — they are a direct cost line, not an exception.

## Caps and controls

- **Spend and rate limits per key.** Each key carries a maximum daily/monthly spend cap and a rate limit
  appropriate to its environment. Non-production keys are capped low, so a misbehaving job hits its cap
  instead of running up an unbounded bill.
- **Cost-intensive jobs are environment-gated.** Cron jobs, batch processes, backfills, and bulk
  generation (e.g. profile generation over large datasets) run **only in production** and are disabled by
  default in dev and staging. They never run automatically against a non-production key.

## Handling and storage

- **Credentials never enter the repo.** No keys, tokens, or secrets in source, in config committed to git,
  in diffs, in logs, or in the release tracker. The tracker and docs hold a **pointer** to where
  credentials live, never the credentials themselves.
- **Keys come from environment configuration / a secrets store,** injected at deploy time. Example config
  files list variable names with placeholder values only.

```bash
# .env.example  (committed - placeholders only)
DATABASE_URL=
OPENAI_API_KEY=
JWT_SECRET=

# .env          (git-ignored - real values, never committed)
```

Ensure `.env` is in `.gitignore` (the template includes it).

- **Rotation and revocation.** Keys are rotated on a defined cadence, and **immediately** on suspected
  exposure or when a team member with access leaves. Each environment can be revoked independently without
  affecting the others.
- **Embedded placements** use the client's secrets management and key policy; these principles are the
  floor, not a replacement.

## Using keys in code and CI

- Read secrets from environment variables or the secret store at runtime. Never hard-code a secret, even
  temporarily "just to test."
- Never log secrets. Scrub them from error messages and debug output. Keep them out of URLs, query
  strings, and client-side code.
- In CI, store secrets as GitHub environment secrets, reference them with `${{ secrets.NAME }}`, and never
  echo them. Scope production secrets to the production environment, behind the deployment approval gate
  (see the [CI/CD Standard](ci-cd-standard.md)).

## Pre-commit secret scanning

- **Every repo carries a pre-commit sanitization hook.** A robust, version-controlled pre-commit hook is
  injected into every project and **blocks a commit** when it detects a credential, token, or key in the
  staged diff — stopping secrets before they ever enter history. This is the standard mechanism behind the
  "no credentials in the repo" rule and is rolled out to all repos.
- **`make secret-scan`** runs a full scan of the repository, **including past history**, and surfaces
  existing and historical secret leaks — not just what is in the current diff. It is the audit complement
  to the pre-commit hook: the hook prevents new leaks, the scan finds what already landed. The same scan
  runs in CI as a second net (see the [CI/CD Standard](ci-cd-standard.md)).
- **Anything surfaced is remediated, not ignored.** A scan that finds nothing is the only acceptable pass.

## If a secret leaks

A leaked secret is **compromised the moment it is exposed**, even briefly. Removing it from a later commit
does not undo the leak.

1. **Rotate and revoke it immediately** — invalidate the old value and issue a new one.
2. Update the secret store and CI secrets with the new value.
3. Investigate where it leaked and what may have been accessed.
4. Clean it from history if feasible, but treat **rotation — not cleanup — as the real fix**.
5. Follow the vulnerability response process in the [Security Standard](security-standard.md).

!!! danger "Don't wait to be sure"
    If you *think* a secret may have leaked, rotate it. The cost of an unnecessary rotation is minutes; the
    cost of a real leak left active can be catastrophic.

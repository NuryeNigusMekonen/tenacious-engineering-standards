# PROOF

## Task

Review the repo's structure, README, and docs; identify 3 concrete, specific improvements; implement them.

## The 3 improvements found and fixed

1. **Broken local-dev setup instructions.** `README.md` and `docs/onboarding-guide.md` told a new
   contributor to run `pip install mkdocs-material` before `mkdocs serve`/`mkdocs build`. `mkdocs.yml`
   requires the `git-revision-date-localized` plugin, which that command does not install.
   Reproduced live in an isolated venv with only `mkdocs-material` installed:
   ```
   ERROR   -  Config value 'plugins': The "git-revision-date-localized" plugin is not installed
   Aborted with a configuration error!
   ```
   The CI workflow (`deploy-docs.yml`) already installs the correct package
   (`mkdocs-git-revision-date-localized-plugin`) - only the docs a contributor actually reads were wrong.
   **Fix:** updated the install command in both files to match what CI installs.

2. **Dead config referencing a file that doesn't exist.** `mkdocs.yml`'s `exclude_docs:` listed
   `STLC_Process_Standard.md`, and `.gitignore` separately ignored `/docs/STLC_Process_Standard.md` - but
   no such file exists anywhere in the repo (`find . -iname "*STLC*"` returns nothing). Two stale
   references to a document that no longer exists, left for the next person to trip over while editing nav
   or exclude config. **Fix:** removed both dead entries.

3. **This repo doesn't enforce its own standards on its own PRs.** The Repository Management Standard and
   CI/CD Standard require every repository to have a Makefile (`build`/`lint`/`test` targets) and CI that
   runs those targets on every pull request. This repo had neither a Makefile nor a PR-triggered workflow -
   `deploy-docs.yml` only runs on push to `main` / manual dispatch, so nothing validated a PR (a broken
   internal link, a `mkdocs build --strict` failure) before it merged to `main` and was live on Pages.
   **Fix:** added `Makefile` (`build`, `lint`, `test`), a stdlib-only internal link/anchor checker
   (`scripts/check_links.py`, no new dependencies) wired in as `make lint`, and
   `.github/workflows/ci.yml` running `make lint && make test` on every `pull_request`.

## Files changed

- `README.md` - fixed local-dev install command
- `docs/onboarding-guide.md` - fixed local-dev install command
- `mkdocs.yml` - removed dead `exclude_docs` entry
- `.gitignore` - removed dead ignore entry for the same nonexistent file
- `Makefile` - new: `build`, `lint`, `test` targets
- `scripts/check_links.py` - new: stdlib Markdown link/anchor checker
- `.github/workflows/ci.yml` - new: runs `make lint && make test` on every PR
- `WORKTREE.md` - task checklist

## Test results

No pre-existing Makefile/test suite existed in the repo before this change (part of finding #3), so there
was nothing to run beforehand. After adding the Makefile, both targets were verified in an isolated venv
with the two documented dependencies (`mkdocs-material`, `mkdocs-git-revision-date-localized-plugin`)
installed, mirroring exactly what the new CI workflow installs:

```
$ make lint
python3 scripts/check_links.py
All local Markdown links and anchors resolve.

$ make test
mkdocs build --strict
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: .../site
INFO    -  Documentation built in 0.47 seconds
```

The link checker was also sanity-checked against intentionally-broken links (missing file, missing
anchor in another file, missing same-file anchor) in a scratch fixture outside the repo to confirm it
actually catches breakage and isn't trivially passing:

```
Broken local links found:
  - .../docs/a.md: links to missing file 'b-does-not-exist.md'
  - .../docs/a.md: links to 'c.md#nope', but no heading in c.md slugifies to 'nope'
  - .../docs/a.md: broken anchor '#zzz' (same file)
exit:1
```

## Walkthrough

- The install-instructions bug and the dead STLC references are pure content/config fixes - no
  behavior change to the published site.
- The Makefile's `build` and `test` targets both run `mkdocs build --strict`: for a static docs site,
  a strict build (which fails on missing files, broken nav, and warnings) is the meaningful "test."
  `lint` is a separate, fast, dependency-free pass that only checks Markdown link/anchor integrity, so it
  can run even before the mkdocs toolchain is installed.
- `site/` (the local build artifact from verification) was removed before committing; it was already
  covered by `.gitignore`.

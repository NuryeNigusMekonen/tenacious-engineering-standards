# Task: Review this repository's structure, README, and any docs present. Identify 3 concrete, specific improvements (not generic advice) that would make these engineering standards clearer or more complete. 
- **Branch**: review/improvements-suggestions
- **Repo**: NuryeNigusMekonen/tenacious-engineering-standards
- **Parent**: /home/nurye/tenai-projects/NuryeNigusMekonen/tenacious-engineering-standards

## Instructions
1. Read this file to understand your task scope
2. Break this task into 3-7 concrete subtasks and add them as a checklist
3. Implement each subtask in order, checking them off
4. Run lint and test commands (check Makefile: `make lint && make test`)
5. Create `PROOF.md` with: test results, files changed, brief walkthrough
6. Commit and push: `git add -A && git commit -m 'feat: <summary>' && git push -u origin review/improvements-suggestions`
7. Create a PR: `gh pr create --base main --fill 2>/dev/null || true`
8. Exit when complete

## Do not
- Install system packages or tools (no apt, brew, npm -g, pip install)
- Modify files outside this task's scope
- Commit .env files
- Merge from other branches (let CI handle it)

## Findings: 3 concrete improvements

1. **Broken local-dev setup instructions.** `README.md` and `docs/onboarding-guide.md` tell a new
   contributor to run `pip install mkdocs-material` then `mkdocs serve`/`mkdocs build`. `mkdocs.yml`
   requires the `git-revision-date-localized` plugin, which that command does not install. Reproduced live:
   `mkdocs build` aborts with `ERROR - Config value 'plugins': The "git-revision-date-localized" plugin is
   not installed`. The CI workflow installs the right package (`mkdocs-git-revision-date-localized-plugin`)
   but the docs contributors actually read do not.
2. **Dead config in `mkdocs.yml`.** `exclude_docs:` lists `STLC_Process_Standard.md`, a file that does not
   exist anywhere in the repo (`find . -iname "*STLC*"` returns nothing). Stale reference that will confuse
   the next person editing nav/exclude config.
3. **This repo doesn't enforce its own standards on its own PRs.** The Repository Management Standard and
   CI/CD Standard require every repo to have a Makefile (`build`/`lint`/`test` targets) and CI that runs
   those targets on every pull request. This repo has no Makefile and its only workflow
   (`deploy-docs.yml`) triggers on push to `main` / manual dispatch only - nothing validates a PR (e.g. a
   `mkdocs build --strict` failure or a broken internal link) before it merges.

## Subtasks

- [x] Fix the local-dev install instructions in `README.md` and `docs/onboarding-guide.md` to include the
      git-revision-date-localized plugin package
- [x] Remove the dead `exclude_docs: STLC_Process_Standard.md` entry from `mkdocs.yml` (and the matching
      dead entry found in `.gitignore` for the same nonexistent file)
- [x] Add a stdlib internal-link/anchor checker script (`scripts/check_links.py`), no new dependencies
- [x] Add a `Makefile` with `build`, `lint`, `test` targets per the CI/CD Standard's Makefile contract
- [x] Add a pull-request-triggered CI workflow that runs `make lint && make test` on every PR
- [x] Run `make lint && make test` locally, confirm green, write `PROOF.md`
- [x] Commit, push branch, open PR

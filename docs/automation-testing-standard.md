# Automation Testing

Automation testing means software checks are run by code or tools instead of being repeated manually.
Automated tests are part of the engineering gate: they run locally, in CI, or against deployed environments
and produce repeatable pass/fail evidence.

Manual validation still comes first for new behavior. Automation is added when the behavior is understood,
stable, and worth checking repeatedly.

## What counts as automation

| Test type | What it checks | Typical owner |
| --- | --- | --- |
| **Unit test** | One small function, class, module, or component in isolation. | Developer |
| **Integration test** | Multiple parts working together, such as service + database or API + queue. | Developer / QA |
| **API test** | Request/response behavior, contracts, auth, errors, and data shape. | Developer / QA |
| **End-to-end test** | A full user journey through the app, often in a browser. | QA / Developer |
| **Smoke test** | A small critical-path check that proves a build is testable. | QA / Developer |
| **Regression test** | Previously working behavior that must not break. | QA / Developer |
| **LLM / eval test** | Model output scored against a golden set, rubric, or deterministic expectation. | QA / AI owner |

Unit, integration, API, and end-to-end tests are all automation tests when they are run by a tool and produce
an objective result.

## Standard tools

Each project may adapt to its stack, but the tool choices must follow the categories below. The Tech Lead
records project-specific choices during setup.

| Category | Standard expectation |
| --- | --- |
| **Command surface** | All automated tests must be runnable through the project `Makefile`. `make test` is the required CI entry point. |
| **CI runner** | GitHub Actions is the default. AWS CodePipeline or a client-approved runner may be used when the engagement requires it. |
| **Unit test framework** | Use the standard test runner for the language or framework, such as Jest/Vitest, pytest, JUnit, Go test, or the platform equivalent. |
| **API / integration testing** | Prefer code-based tests in the project test suite. Postman may be used for exploratory or client-shared collections. |
| **Browser / end-to-end testing** | Playwright is the default for web UI automation unless the project has an established equivalent. |
| **LLM / RAG evaluation** | Use a versioned eval harness or dataset that can run from CI and produce reviewable results. |
| **Reports** | Use native CI output by default. Add Allure or another report tool only when the project needs richer release evidence. |

If a project uses different tools, the reason must be recorded in the repository README or project
conventions file.

## When to automate

Automate a test when most of these are true:

- the behavior is stable enough that the test will not be rewritten every sprint;
- the same check must run repeatedly;
- the expected result can be asserted by code, a rubric, or a reliable evaluator;
- the path is business-critical or high-risk;
- automation will save more time than it costs to build and maintain.

Keep the test manual when the feature is still changing, the check is one-off, the result requires nuanced
human judgment, or the automation would be fragile.

## Test layer guidance

Use the lowest reliable layer for the behavior being checked.

| Layer | Use it for | Guardrail |
| --- | --- | --- |
| **Unit** | Business rules, calculations, parsing, transformations, component logic. | Fast and numerous; should not need external services. |
| **Integration / API** | Service boundaries, database behavior, auth, contracts, and data flow. | Prefer these over UI tests when the UI is not the point. |
| **End-to-end** | Critical user journeys that prove the system works as a user experiences it. | Keep small and high-value; avoid a slow UI-heavy suite. |
| **LLM evals** | AI behavior where output quality matters over exact string matching. | Use versioned datasets, rubrics, thresholds, and human spot-checks. |

## Required commands

`make test` is mandatory for every project with automated tests. It must run the test set that is required
for pull requests.

Projects may add more specific targets when useful:

| Command | Use |
| --- | --- |
| `make test` | Required PR gate; runs the relevant automated suite for the project. |
| `make test-unit` | Fast unit tests. |
| `make test-integration` | Service, database, API, and integration tests. |
| `make test-e2e` | Browser or full-journey tests. |
| `make test-eval` | LLM/RAG evaluation suite. |

CI must call the same commands developers run locally (see the [CI/CD Standard](ci-cd-standard.md)).

## How to build automated coverage

1. **Start from a real manual check.** The expected behavior must already be understood and written down.
2. **Choose the right layer.** Prefer unit or API coverage unless the user interface itself must be proven.
3. **Make the test deterministic where possible.** Control data, mocks, time, random values, and environment
   dependencies.
4. **Assert outcomes, not implementation details.** The test should fail when user-visible or contract-level
   behavior breaks.
5. **Run it locally and in CI.** Required automated gates belong in the project command surface and pipeline
   (see the [CI/CD Standard](ci-cd-standard.md)).
6. **Publish useful failure output.** A failing test should tell the owner what broke and where to start.
7. **Maintain it like production code.** Review it, refactor it, and remove or quarantine flaky checks.

## Test ownership and naming

Every automated test must have a clear reason to exist. It should cover a requirement, defect, user journey,
integration contract, or frozen task set item.

| Rule | Standard |
| --- | --- |
| **Naming** | Test names describe the behavior, not the implementation. |
| **Location** | Tests live with the code or in the project-approved test directory. |
| **Data** | Test data is repeatable, safe, and does not depend on uncontrolled production state. |
| **Owner** | The team that owns the feature owns the automated tests for it. |
| **Failure** | A failing required test blocks merge or promotion until fixed, removed with justification, or explicitly risk-accepted. |

## LLM automation handoff

For LLM and RAG features, the handoff from manual to automation is the frozen task set from the
[Manual Testing](manual-testing-standard.md#llm-and-rag-checks) standard.

Automated LLM checks must define:

- the input dataset or golden set;
- the expected answer, rubric, or scoring criteria;
- the grader type: code-based, model-based, or human spot-check;
- the pass threshold for release;
- how failures are reviewed and accepted.

Human spot-checks remain part of the process. They verify that automated graders are still judging the
right thing.

## CI and release gates

An automated test can block promotion only when it is trusted.

To be trusted, it must:

- run consistently in the same command used by CI;
- fail for real product risk, not environment noise;
- have an owner who fixes or removes it when it breaks;
- publish results that can be reviewed during a release decision.

Do not override a failing required check without fixing the failure or recording explicit risk acceptance.

## Exit criteria

Automation work is complete only when:

- the test covers a named requirement, defect, risk, or frozen task set item;
- the test runs successfully in the expected local or CI command;
- the failure message is useful enough for triage;
- test data and setup are repeatable;
- the check is documented or discoverable by future maintainers;
- flaky behavior has been fixed, not normalized.

!!! note "Automation is earned"
    Automation is not a goal by itself. The goal is a trusted signal that catches real regressions faster
    than manual checking can.

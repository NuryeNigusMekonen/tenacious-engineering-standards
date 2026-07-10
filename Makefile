.PHONY: build lint test

# Render the site the same way the deploy workflow does; --strict turns
# warnings (missing nav entries, broken references) into failures.
build:
	mkdocs build --strict

# Fast, dependency-free check that local Markdown links and heading
# anchors across the repo actually resolve.
lint:
	python3 scripts/check_links.py

test: build

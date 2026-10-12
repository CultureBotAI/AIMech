set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

install:
    uv sync --locked --extra dev

check:
    uv run --locked --extra dev python scripts/check.py

fetch-review-bases:
    uv run --locked python scripts/fetch_review_bases.py

test:
    uv run --locked --extra dev pytest -q

lint:
    uv run --locked --extra dev ruff check src tests scripts

vendored-check:
    bash scripts/check_vendored_sync.sh

[positional-arguments]
validate *args:
    uv run --locked aimech validate "$@"

check-source:
    uv run --locked aimech check-source

[positional-arguments]
seed *args:
    uv run --locked aimech seed "$@"

[positional-arguments]
new-history *args:
    uv run --locked aimech new-history "$@"

[positional-arguments]
validate-history *args:
    uv run --locked aimech validate-history "$@"

[positional-arguments]
check-reviews *args:
    uv run --locked python scripts/record_review.py check "$@"

[positional-arguments]
review-check *args:
    uv run --locked python scripts/record_review.py check "$@"

render:
    uv run --locked python scripts/render_pages.py

render-check:
    uv run --locked python scripts/render_pages.py --check

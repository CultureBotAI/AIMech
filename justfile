set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

install:
    uv sync --locked --extra dev

check:
    uv run --locked --extra dev python scripts/check.py

test:
    uv run --locked --extra dev pytest -q

lint:
    uv run --locked --extra dev ruff check src tests scripts

vendored-check:
    bash scripts/check_vendored_sync.sh

validate *args:
    uv run --locked aimech validate {{args}}

check-source:
    uv run --locked aimech check-source

seed *args:
    uv run --locked aimech seed {{args}}

new-history *args:
    uv run --locked aimech new-history {{args}}

validate-history *args:
    uv run --locked aimech validate-history {{args}}

check-reviews *args:
    uv run --locked python scripts/record_review.py check {{args}}

review-check *args:
    uv run --locked python scripts/record_review.py check {{args}}

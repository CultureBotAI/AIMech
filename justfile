set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

install:
    uv sync --locked --extra dev

check:
    uv run --locked --extra dev python scripts/check.py

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

"""Starter code for the published-record reconciliation exercise."""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class ReconciliationResult:
    expected_count: int
    actual_count: int
    matched: tuple[str, ...]
    missing: tuple[str, ...]
    extra: tuple[str, ...]
    ok: bool


def normalize_id(value: str | None) -> str | None:
    """Return a canonical identifier, or None for a missing or blank value."""
    raise NotImplementedError


def reconcile(
    source_records: Sequence[Mapping[str, str | None]],
    published_ids: Sequence[str | None],
) -> ReconciliationResult:
    """Compare active source identifiers with published identifiers."""
    raise NotImplementedError

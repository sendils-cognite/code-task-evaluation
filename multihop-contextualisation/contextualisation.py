"""Starter code for the multi-hop contextualization exercise."""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

Record = Mapping[str, str | None]


@dataclass(frozen=True)
class ContextualizationResult:
    total_rows: int
    contextualized: tuple[str, ...]
    missing_equipment: tuple[str, ...]
    ambiguous_equipment: tuple[str, ...]
    missing_location: tuple[str, ...]
    ambiguous_location: tuple[str, ...]
    ok: bool


def normalize_id(value: str | None) -> str | None:
    """Return a canonical identifier, or None for a missing or blank value."""
    if value is None:
        return None
    normalized = value.strip().casefold()
    return normalized or None


def build_active_index(
    records: Sequence[Record],
    key_field: str,
) -> tuple[dict[str, Record], set[str]]:
    """Return uniquely keyed active records and ambiguous active identifiers."""
    raise NotImplementedError


def validate_contextualization(
    source_rows: Sequence[Record],
    equipment_records: Sequence[Record],
    location_records: Sequence[Record],
) -> ContextualizationResult:
    """Validate source-row resolution through equipment to location."""
    raise NotImplementedError

 Multi-hop Contextualization Coverage

A source table contains records that reference equipment. Equipment references a
location. A source row is contextualized only when both links resolve to exactly one
active reference record:

`source row → equipment → location`

Complete `build_active_index()` and `validate_contextualization()` in
`contextualization.py`. You may use any resources available to you. Python 3.11 or
newer is required.

## Requirements

1. Identifiers are normalized with the supplied `normalize_id()` function.
2. Only reference records whose `status` is `active` are eligible.
3. `build_active_index()` returns:
   - identifiers with exactly one active record, mapped to that record; and
   - identifiers with more than one active record, marked ambiguous.
4. For each source row:
   - a missing, blank, or inactive equipment reference is `missing_equipment`;
   - multiple active equipment records are `ambiguous_equipment`;
   - after unique equipment resolution, a missing, blank, or inactive location is
     `missing_location`;
   - multiple active locations are `ambiguous_location`;
   - only a unique active resolution at both hops is `contextualized`.
5. Do not continue to the location hop when equipment resolution failed.
6. Return source `row_id` values as sorted tuples. Assume they are non-blank and unique.
7. `ok` is true only when the source contains at least one row and every row is
   contextualized.

Do not change `ContextualizationResult`, `normalize_id()`, or the visible tests.

## Run

From this directory:

```bash
uv run python -m unittest -v test_contextualization.py
```

When the tests pass, be ready to explain:

- why checking only for non-null foreign keys is insufficient;
- the complexity of your solution;
- how you would validate a snapshot containing millions of rows.

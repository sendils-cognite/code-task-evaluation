# Published Record Reconciliation

You are checking whether records from a source system reached a published API.

Complete `normalize_id()` and `reconcile()` in `reconcile.py`. You may use any
resources available to you. Python 3.11 or newer is required.

## Requirements

1. An identifier is normalized by trimming leading/trailing whitespace and comparing
   without case sensitivity. Blank or missing identifiers are ignored. Do not remove
   whitespace inside an identifier.
2. Only source records whose `status` is `active`, compared without case sensitivity
   and after trimming, are expected in the published API.
3. Duplicate identifiers count once.
4. Return sorted tuples for `matched`, `missing`, and `extra` so output is deterministic.
5. Published extras are reported but do not make the result fail.
6. `ok` is true only when the expected set is non-empty and no expected identifier is
   missing. An empty expected set must fail because it may indicate a bad source query.

Do not change `ReconciliationResult` or the visible tests.

## Run

From this directory:

```bash
uv run python -m unittest -v test_reconcile.py
```

When the tests pass, be ready to explain:

- assumptions or risks you noticed;
- the time and space complexity;
- what you would monitor if this ran in production.

The exercise and discussion together are limited to ten minutes.

# Configuration Contract Validation

A deployment configuration declares variable names, while templates reference variables
using `{{ variable_name }}` placeholders.

Complete `extract_placeholders()` and `validate_contract()` in `config_contract.py`.
You may use any resources available to you. Python 3.11 or newer is required.

## Requirements

1. Placeholder names are case-sensitive and match `[A-Za-z_][A-Za-z0-9_]*`.
2. Allow whitespace immediately inside the braces, for example
   `{{ database_name }}` and `{{database_name}}`.
3. Ignore malformed placeholders rather than partially matching them.
4. `referenced` contains every unique placeholder used by any template.
5. `missing` contains names that are referenced or required but not declared.
6. `unused` contains declared names that are neither referenced nor required.
7. All result tuples must be sorted.
8. Missing names fail validation; unused names are warnings and do not fail it.

Do not change `ContractValidationResult` or the visible tests.

## Run

From this directory:

```bash
uv run python -m unittest -v test_config_contract.py
```

When the tests pass, be ready to explain:

- which findings should block deployment;
- how malformed templates should be handled in production;
- how this validator should evolve when variable scopes are introduced.

The exercise and discussion together are limited to ten minutes.

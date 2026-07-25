"""Visible tests for the configuration-contract validation exercise."""

import unittest

from config_contract import (
    ContractValidationResult,
    extract_placeholders,
    validate_contract,
)


class ExtractPlaceholdersTest(unittest.TestCase):
    def test_extracts_valid_unique_names_and_ignores_malformed_values(self) -> None:
        template = """
        host={{ database_host }}
        database={{database_name}}
        again={{ database_host }}
        malformed={{ 9invalid }} and {{ database-name }}
        """

        self.assertEqual(
            extract_placeholders(template),
            {"database_host", "database_name"},
        )


class ValidateContractTest(unittest.TestCase):
    def test_reports_missing_and_unused_variables(self) -> None:
        result = validate_contract(
            declared=["database_host", "legacy_timeout", "region"],
            required=["region"],
            templates=[
                "host={{ database_host }}",
                "name={{ database_name }} in {{region}}",
            ],
        )

        self.assertEqual(
            result,
            ContractValidationResult(
                referenced=("database_host", "database_name", "region"),
                missing=("database_name",),
                unused=("legacy_timeout",),
                ok=False,
            ),
        )

    def test_required_but_unreferenced_variables_are_not_unused(self) -> None:
        result = validate_contract(
            declared=["region", "optional_timeout"],
            required=["region"],
            templates=[],
        )

        self.assertEqual(result.referenced, ())
        self.assertEqual(result.missing, ())
        self.assertEqual(result.unused, ("optional_timeout",))
        self.assertTrue(result.ok)


if __name__ == "__main__":
    unittest.main()

"""
Foreclosure Lead Analyzer

This script cleans and filters foreclosure lead data from a CSV file.

The goal is to simulate a real-world data processing workflow where raw
property records are reviewed, validated, and prepared for further analysis.
"""

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


UNIT_PATTERNS = [
    r"\bAPT\b",
    r"\bAPARTMENT\b",
    r"\bUNIT\b",
    r"\bSUITE\b",
    r"#\d+",
    r"\bBLDG\b",
    r"\bFLOOR\b",
]

EXCLUDED_OWNER_KEYWORDS = [
    "CONDOMINIUM",
    "CONDO",
    "ASSOCIATION",
    "HOA",
    "HOMEOWNERS",
    "PROPERTY OWNERS",
    "COMMUNITY ASSOC",
]


@dataclass
class LeadReviewResult:
    """Stores the result of reviewing a foreclosure lead."""

    keep: bool
    reason: str


def get_value(row: Dict, column_name: str) -> str:
    """Safely reads a value from a CSV row."""

    target = column_name.strip().lower()

    for key, value in row.items():
        if key.strip().lower() == target:
            return str(value).strip()

    return ""


def has_valid_address(row: Dict) -> bool:
    """Checks whether a lead has the minimum required address fields."""

    address = get_value(row, "Address")
    city = get_value(row, "City")
    zip_code = get_value(row, "Zip")

    return bool(address and city and zip_code)


def looks_like_apartment_or_condo(address: str, owner_name: str) -> bool:
    """Detects apartment, condo, or HOA-related leads."""

    address_upper = address.upper()
    owner_upper = owner_name.upper()

    for pattern in UNIT_PATTERNS:
        if re.search(pattern, address_upper):
            return True

    for keyword in EXCLUDED_OWNER_KEYWORDS:
        if keyword in owner_upper:
            return True

    return False


def review_lead(row: Dict) -> LeadReviewResult:
    """Applies filtering rules to a single foreclosure lead."""

    address = get_value(row, "Address")
    owner_name = get_value(row, "Certificate Holder Name")

    if not has_valid_address(row):
        return LeadReviewResult(False, "Missing address information")

    if looks_like_apartment_or_condo(address, owner_name):
        return LeadReviewResult(False, "Likely apartment, condo, or HOA property")

    return LeadReviewResult(True, "Qualified lead")


def read_csv(file_path: Path) -> Tuple[List[Dict], List[str]]:
    """Reads a CSV file and returns rows plus headers."""

    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        headers = reader.fieldnames or []

    return rows, headers


def write_csv(file_path: Path, rows: List[Dict], headers: List[str]) -> None:
    """Writes filtered lead records to a new CSV file."""

    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def filter_leads(rows: List[Dict]) -> Tuple[List[Dict], Dict]:
    """Filters foreclosure leads and returns cleaned rows plus summary stats."""

    filtered_rows = []

    summary = {
        "total": len(rows),
        "kept": 0,
        "missing_address": 0,
        "apartment_or_condo": 0,
    }

    for row in rows:
        result = review_lead(row)

        if result.keep:
            filtered_rows.append(row)
            summary["kept"] += 1
        elif result.reason == "Missing address information":
            summary["missing_address"] += 1
        else:
            summary["apartment_or_condo"] += 1

    return filtered_rows, summary


def print_summary(summary: Dict, output_file: Path) -> None:
    """Displays a clean processing summary."""

    print("\nLead Filtering Summary")
    print("-" * 30)
    print(f"Total records reviewed: {summary['total']}")
    print(f"Qualified leads kept:   {summary['kept']}")
    print(f"Missing address:        {summary['missing_address']}")
    print(f"Apartment/condo leads:  {summary['apartment_or_condo']}")
    print(f"Output file:            {output_file}")


def main() -> None:
    """Runs the lead filtering workflow from the command line."""

    input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sample_leads.csv")
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("filtered_leads.csv")

    if not input_file.exists():
        print(f"Error: input file not found: {input_file}")
        sys.exit(1)

    rows, headers = read_csv(input_file)
    filtered_rows, summary = filter_leads(rows)

    write_csv(output_file, filtered_rows, headers)
    print_summary(summary, output_file)


# Entry point for command-line execution
if __name__ == "__main__":
    main()
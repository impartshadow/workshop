"""Check vina's fabricated-citation fixture; no network or model calls."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions/collaboration/vina-citation-integrity"
FAKE_DOI = "https://doi.org/10.5555/workshop-hallucinated-2026"


def one_row(name):
    with (BASE / name).open(newline="") as source:
        rows = list(csv.DictReader(source))
    assert len(rows) == 1, f"{name} must contain exactly one row"
    return rows[0]


def main():
    fixture = one_row("fixture.csv")
    result = one_row("result.csv")
    assert fixture["discovery_lead"] == FAKE_DOI
    assert result["primary_source"] == "INVALID_INPUT"
    assert result["public_inputs"] == "NOT_USED"
    assert "404" in result["verification"] and "do not infer" in result["verification"]
    assert "does not" in result["limitations"]
    assert FAKE_DOI not in result["primary_source"]
    print("PASS: fabricated lead is rejected, no source or public input is invented, and the limit is explicit.")


if __name__ == "__main__":
    main()

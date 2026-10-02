"""Inspect the frozen public workbook locally, without spreadsheet dependencies.

Print every populated cell for human review; do not infer scientific meaning
from column names or execute formulas. The publisher file is not redistributed.
"""
import argparse
import csv
import hashlib
from pathlib import Path
import posixpath
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

EXPECTED_SHA256 = "db17997b99a449df965c9e6e45ecc91314575d1d944c9e6b12933f09dee8abe3"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def inspect(path, summary=False):
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"Source hash mismatch: {digest}; this is not the frozen workbook")
    print(f"Source verified: {len(payload)} bytes; SHA-256 {digest}", file=sys.stderr)
    writer = csv.writer(sys.stdout)
    writer.writerow(["sheet", "populated_rows", "populated_cells", "header_cells"] if summary
                    else ["sheet", "cell", "value", "formula_not_executed"])
    with ZipFile(path) as archive:
        strings = ET.fromstring(archive.read("xl/sharedStrings.xml"))
        shared = ["".join(node.itertext()) for node in strings.findall("s:si", NS)]
        relations = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        targets = {rel.attrib["Id"]: rel.attrib["Target"] for rel in relations}
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheets = workbook.findall("s:sheets/s:sheet", NS)
        for sheet in sheets:
            target = targets[sheet.attrib[RID]]
            member = (target.lstrip("/") if target.startswith("/") else
                      posixpath.normpath(posixpath.join("xl", target)))
            document = ET.fromstring(archive.read(member))
            rows = []
            for row in document.findall("s:sheetData/s:row", NS):
                cells = []
                for cell in row.findall("s:c", NS):
                    value = cell.findtext("s:v", default="", namespaces=NS)
                    kind = cell.get("t")
                    if kind == "s":
                        value = shared[int(value)]
                    elif kind == "inlineStr":
                        value = "".join(cell.find("s:is", NS).itertext())
                    formula = cell.findtext("s:f", default="", namespaces=NS)
                    if value or formula:
                        cells.append((cell.attrib["r"], value, formula))
                if cells:
                    rows.append(cells)
            if summary:
                writer.writerow([sheet.attrib["name"], len(rows), sum(map(len, rows)),
                                 "; ".join(f"{ref}={value}" for ref, value, _ in rows[0]) if rows else ""])
            else:
                for row in rows:
                    for ref, value, formula in row:
                        writer.writerow([sheet.attrib["name"], ref, value, formula])
        print(f"Inspected {len(sheets)} sheets. Values are workbook contents, not a scientific verdict.", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--summary", action="store_true", help="Print sheet counts and headers instead of every cell")
    args = parser.parse_args()
    try:
        inspect(args.workbook, args.summary)
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))

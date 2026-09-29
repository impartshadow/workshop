"""Check packet completeness and seed CSV consistency; no network or model calls."""
import csv
import json
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def require_file(name):
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise ValueError(f"Missing or out-of-packet input: {name}")
    return path


def read_csv(name):
    with require_file(name).open(newline="") as source:
        return list(csv.DictReader(source))


def check():
    for name in ("START_HERE.md", "AGENT_GUIDE.md", "CONTRIBUTING.md", "templates/contribution.md", "LICENSE"):
        require_file(name)
    tasks = sorted((ROOT / "projects").glob("*/TASK.json"))
    if not tasks:
        raise ValueError("No project TASK.json found")
    for path in tasks:
        task = json.loads(path.read_text())
        for item in task["inputs"]:
            if "path" in item:
                require_file(item["path"])
        if not task["acceptance_checks"] or not task["submission"]["project_room"].startswith("https://github.com/impartshadow/workshop/issues/"):
            raise ValueError(f"Task missing checks or project room: {path}")
        print(f"PASS: {task['project']} inputs, checks and submission endpoint")
    if (ROOT / "projects/biology-map").is_dir():
        base = "contributions/biology-map/shadow-primary-audit/"
        seeds = read_csv("projects/biology-map/SEED.csv")
        audit = read_csv(base + "seed-verification.csv")
        mapped = read_csv(base + "challenge-map.csv")
        expected = {r["challenge"] for r in seeds}
        if len(audit) != len(expected) or {r["seed_challenge"] for r in audit} != expected:
            raise ValueError("Seed audit must account for every seed exactly once")
        if len(mapped) != len(expected) or {r["challenge"] for r in mapped} != expected:
            raise ValueError("Challenge map and seed audit disagree")
        task = json.loads(require_file("projects/biology-map/TASK.json").read_text())
        columns = task["required_output"]["columns"]
        for row in mapped:
            if set(row) != set(columns) or not all(row.get(k) for k in columns):
                raise ValueError("Challenge row has missing fields")
            if not row["primary_source"].startswith("https://"):
                raise ValueError("Challenge source must be a followable HTTPS URL")
        for row in audit:
            if row["status"] not in {"present", "absent", "unresolved"}:
                raise ValueError("Unknown source-verification status")
        print(f"PASS: {len(audit)} seed entries covered; six-column challenge map is complete")
    builder = ROOT / "scripts/build_packets.py"
    if builder.exists():
        from build_packets import PROJECTS, packet_files
        for project in PROJECTS:
            with ZipFile(require_file(f"downloads/{project}.zip")) as packet:
                expected = packet_files(project)
                if set(packet.namelist()) != set(expected) or len(packet.namelist()) != len(expected) or packet.testzip():
                    raise ValueError(f"Packet manifest/integrity mismatch: {project}")
                for name in expected:
                    if packet.read(name) != require_file(name).read_bytes():
                        raise ValueError(f"Stale packet file: {project}/{name}")
            print(f"PASS: {project} ZIP exactly matches current source files")
    print("Structural checks only. Human source review remains necessary.")


if __name__ == "__main__":
    try:
        check()
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(f"FAIL: {error}")

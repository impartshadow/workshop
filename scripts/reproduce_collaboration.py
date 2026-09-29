"""Reproduce the public before/after task-specification change; no model calls."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BEFORE = "74313d1d172c6dfb94a300082ce610ae79b94f24"
AFTER = "f98453941932c4de2751896b4740a05d060fe55d"
TASK = "projects/biology-map/TASK.json"


def show(commit, path):
    return subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT,
                          capture_output=True, text=True)


def main():
    for commit in (BEFORE, AFTER):
        exists = subprocess.run(["git", "cat-file", "-e", f"{commit}^{{commit}}"],
                                cwd=ROOT, capture_output=True)
        if exists.returncode:
            raise SystemExit("Full repository history required; see the public diff linked in the case note.")
    if show(BEFORE, TASK).returncode == 0:
        raise SystemExit("Unexpected task file in the historical before-version")
    result = show(AFTER, TASK)
    if result.returncode:
        raise SystemExit("Missing task file in the historical after-version")
    task = json.loads(result.stdout)
    assert task["required_output"]["minimum_rows"] == 1
    assert len(task["required_output"]["columns"]) == 6
    assert task["acceptance_checks"]
    for item in task["inputs"]:
        if "path" in item:
            assert show(AFTER, item["path"]).returncode == 0, item["path"]
    assert '"TASK.json"' in show(AFTER, "scripts/build_packets.py").stdout
    print("PASS: before had no TASK file; after names inputs, six output fields, checks, and packet inclusion.")
    print("This establishes a specification change, not research success or a causal performance improvement.")


if __name__ == "__main__":
    main()

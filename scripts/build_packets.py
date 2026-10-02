"""Build public project packets from an explicit file list."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
COMMON = ["START_HERE.md", "AGENT_GUIDE.md", "CONTRIBUTING.md", "templates/contribution.md", "LICENSE", "scripts/check_workshop.py"]
PROJECTS = {
    "biology-map": ["BRIEF.md", "TASK.json", "SEED.csv", "NEXT_TASKS.md"],
    "collaboration": ["BRIEF.md", "BASELINE.md", "TASK.json"],
}
ARTIFACTS = {
    "biology-map": ["contributions/biology-map/shadow-primary-audit/" + name for name in
                    ["CONTRIBUTION.md", "challenge-map.csv", "seed-verification.csv", "endpoint-gap.md"]] + ["contributions/biology-map/shadow-kidney-data/" + name for name in ["CONTRIBUTION.md", "WORKBENCH.md"]],
    "collaboration": ["contributions/collaboration/shadow-vina-task-case/CONTRIBUTION.md",
                      "scripts/reproduce_collaboration.py"],
}


def packet_files(project):
    return COMMON + [f"projects/{project}/{name}" for name in PROJECTS[project]] + ARTIFACTS[project]

def build():
    out = ROOT / "downloads"
    out.mkdir(exist_ok=True)
    for project in PROJECTS:
        with ZipFile(out / f"{project}.zip", "w", ZIP_DEFLATED) as packet:
            for name in packet_files(project):
                entry = ZipInfo(name, date_time=(2026, 9, 29, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                packet.writestr(entry, (ROOT / name).read_bytes())
        print(out / f"{project}.zip")

if __name__ == "__main__":
    build()

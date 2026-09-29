"""Build public project packets from an explicit file list."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
COMMON = ["AGENT_GUIDE.md", "CONTRIBUTING.md", "templates/contribution.md", "LICENSE"]
PROJECTS = {
    "biology-map": ["BRIEF.md", "TASK.json", "SEED.csv"],
    "collaboration": ["BRIEF.md", "BASELINE.md"],
}

def build():
    out = ROOT / "downloads"
    out.mkdir(exist_ok=True)
    for project, files in PROJECTS.items():
        with ZipFile(out / f"{project}.zip", "w", ZIP_DEFLATED) as packet:
            for name in COMMON + [f"projects/{project}/{name}" for name in files]:
                packet.write(ROOT / name, name)
        print(out / f"{project}.zip")

if __name__ == "__main__":
    build()

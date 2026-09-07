"""Generate or verify active repository and component SHA-256 inventories."""

import argparse
import hashlib
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
COMPONENTS = ("schemas", "conformance", "reference-implementation", "audit")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repository_files():
    output = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    ).decode("utf-8")
    return sorted({path.replace("\\", "/") for path in output.split("\0") if path})


def content(paths, prefix=""):
    offset = len(prefix) + 1 if prefix else 0
    return "".join(f"{digest(ROOT / path)}  {path[offset:]}\n" for path in paths)


def apply(path, expected, check):
    target = ROOT / path
    if check:
        actual = target.read_text(encoding="utf-8") if target.exists() else ""
        if actual != expected:
            raise SystemExit(f"Checksum inventory stale: {path}")
    else:
        target.write_text(expected, encoding="utf-8", newline="\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail instead of writing when an inventory is stale")
    args = parser.parse_args()
    files = repository_files()
    for component in COMPONENTS:
        selected = [path for path in files if path.startswith(f"{component}/") and path != f"{component}/SHA256SUMS.txt"]
        apply(f"{component}/SHA256SUMS.txt", content(selected, component), args.check)
    # Component inventories are part of the root inventory and may have just changed.
    apply("SHA256SUMS.txt", content([path for path in files if path != "SHA256SUMS.txt"]), args.check)
    action = "verified" if args.check else "updated"
    print(f"PASS: checksum inventories {action}; {len(files) - 1} root entries")


if __name__ == "__main__":
    main()

"""Validate current release metadata and checksums; historical evidence is separate."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
COMPONENTS = ("schemas", "conformance", "reference-implementation", "audit")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_checksums(path):
    entries = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        target = (path.parent / relative).resolve()
        require(target.is_relative_to(path.parent.resolve()), f"Unsafe path: {relative}")
        require(relative not in entries, f"Duplicate checksum: {relative}")
        require(target != path.resolve(), f"Self checksum: {path}")
        require(target.is_file(), f"Missing artifact: {target}")
        require(digest(target) == expected, f"Checksum mismatch: {target}")
        entries.add(relative)
    require(entries, f"Empty checksum inventory: {path}")
    return entries


def compare_baseline(manifest, specification):
    baseline = manifest["original_baseline"]["repository_commit"]
    relative = manifest["normative_specification"]["path"]
    original = subprocess.check_output(["git", "show", f"{baseline}:{relative}"], cwd=ROOT)
    require(hashlib.sha256(original).hexdigest() == manifest["original_baseline"]["specification_sha256"],
            "Original baseline specification hash mismatch")
    # Reverse only the declared editorial operations, then require byte identity.
    restored = specification.replace("## Framework Specification v1.0 LTS", "## Framework Specification v1.0", 1)
    restored = restored.replace(
        "**Status:** RELEASED\n**Version:** v1.0 LTS\n**Release date:** 2026-09-05\n**Editorial revision:** LTS-Editorial-1",
        "**Status:** Release Candidate — Public-Readiness Hardened / Semantic Freeze Candidate\n"
        "Freeze Hold **Version:** 1.0 RC-Final-Public-Readiness-Hardening", 1)
    restored = re.sub(r"^> \*\*Status rilis saat ini:.*\n\n", "", restored, count=1, flags=re.M)
    restored = re.sub(r"^> \*\*Catatan historis — bukan status rilis saat ini\.\*\*.*\n", "", restored, flags=re.M)
    # Each appended historical banner introduced one additional blank line.
    restored = re.sub(r"(# Appendix [P-W] --- [^\n]+\n)\n\n", r"\1\n", restored)
    require(restored.encode("utf-8") == original, "Specification changed beyond declared editorial operations")
    archive = ROOT / "release/provenance/original-v1.0-LTS"
    for path in archive.rglob("*"):
        if not path.is_file() or path == archive / "README.md":
            continue
        relative = path.relative_to(archive).as_posix()
        expected = subprocess.check_output(["git", "show", f"{baseline}:{relative}"], cwd=ROOT)
        require(path.read_bytes() == expected, f"Historical archive changed: {relative}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compare-baseline", action="store_true", help="Also verify editorial-only changes against Git baseline history")
    args = parser.parse_args()
    manifest = load("release/AOF-v1.0-LTS-Release-Manifest.json")
    require((manifest["release"], manifest["status"], manifest["release_date"]) ==
            ("v1.0 LTS", "RELEASED", "2026-09-05"), "Inconsistent release identity")
    current = manifest["normative_specification"]
    require(digest(ROOT / current["path"]) == current["sha256"], "Active specification hash mismatch")
    specification = (ROOT / current["path"]).read_text(encoding="utf-8")
    require("**Status:** RELEASED" in specification[:500], "Stale specification header")
    for relative in ("README.md", "schemas/README.md", "schemas/RELEASE-NOTES.md",
                     "conformance/README.md", "conformance/RELEASE-NOTES.md",
                     "reference-implementation/README.md", "audit/README.md",
                     "release/AOF-v1.0-LTS-Declaration.md", "release/RELEASE-NOTES.md"):
        document = (ROOT / relative).read_text(encoding="utf-8")
        require("RELEASED" in document[:500], f"Missing active release status: {relative}")
        require(not re.search(r"(?:\*\*Status:\*\*|Status:).*RELEASE.CANDIDATE", document),
                f"Stale active status: {relative}")
    for appendix in "PQRSTUVW":
        require(re.search(rf"# Appendix {appendix} --- [^\n]+\n\n> \*\*Catatan historis", specification),
                f"Missing historical context: Appendix {appendix}")
    for path in ("schemas/catalog.json", "conformance/release/manifest.json", "reference-implementation/release/manifest.json"):
        component = load(path)
        require((component["release"], component["release_status"], component["release_date"]) ==
                (manifest["release"], manifest["status"], manifest["release_date"]), f"Stale component: {path}")
        require(component["current_specification"]["sha256"] == current["sha256"], f"Stale specification reference: {path}")
    require(load("conformance/release/manifest.json")["lts_audit_result"] == "PASS", "Incorrect A4 result")
    require(load("reference-implementation/release/manifest.json")["lts_audit_result"] ==
            "PASS_WITH_RELEASE_CLAIM_CONSTRAINT", "Incorrect A5 result")
    entries = validate_checksums(ROOT / "SHA256SUMS.txt")
    for component in COMPONENTS:
        component_entries = validate_checksums(ROOT / component / "SHA256SUMS.txt")
        require(all(f"{component}/{p}" in entries for p in component_entries), "Incomplete root checksum inventory")
    for relative in entries:
        path = ROOT / relative
        if path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8"))
        if path.suffix == ".md" and not relative.startswith("release/provenance/"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                local = target.split("#", 1)[0]
                require((path.parent / local).exists(), f"Broken local link in {relative}: {target}")
    if args.compare_baseline:
        compare_baseline(manifest, specification)
    print(f"PASS: release metadata, JSON, local links, and {len(entries)} root checksums; 4 component inventories")
    if args.compare_baseline:
        print("PASS: specification changes are editorial only; original metadata archive is byte-identical")


if __name__ == "__main__":
    main()

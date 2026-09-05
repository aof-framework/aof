from copy import deepcopy
from datetime import datetime, timezone

class EvidenceStore:
    def __init__(self):
        self._items = {}

    def add(self, evidence):
        eid = evidence["id"]
        if eid in self._items:
            raise ValueError("EVIDENCE_ALREADY_EXISTS")
        item = deepcopy(evidence)
        item.setdefault("created_at", datetime.now(timezone.utc).isoformat())
        item.setdefault("admissible", True)
        self._items[eid] = item
        return deepcopy(item)

    def get(self, evidence_id):
        item = self._items.get(evidence_id)
        return deepcopy(item) if item else None

    def collect_for_subject(self, subject_ref, subject_version=None):
        out=[]
        for item in self._items.values():
            if item.get("subject_ref") != subject_ref:
                continue
            if subject_version is not None and str(item.get("subject_version")) != str(subject_version):
                continue
            out.append(deepcopy(item))
        return out

def evidence_is_admissible(evidence, subject_ref, subject_version):
    if evidence is None:
        return False, "EVIDENCE_MISSING"
    if evidence.get("admissible") is False:
        return False, "EVIDENCE_INADMISSIBLE"
    if evidence.get("subject_ref") != subject_ref:
        return False, "EVIDENCE_SUBJECT_MISMATCH"
    if str(evidence.get("subject_version")) != str(subject_version):
        return False, "EVIDENCE_VERSION_MISMATCH"
    if not evidence.get("provenance"):
        return False, "EVIDENCE_PROVENANCE_MISSING"
    if evidence.get("stale") is True:
        return False, "EVIDENCE_STALE"
    return True, "EVIDENCE_ADMISSIBLE"

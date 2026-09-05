from copy import deepcopy

class InMemoryStateStore:
    def __init__(self):
        self._states = {}

    def put(self, subject_ref, state, version):
        self._states[subject_ref] = {"state": deepcopy(state), "version": str(version)}
        return self.get(subject_ref)

    def get(self, subject_ref):
        rec = self._states.get(subject_ref)
        if rec is None:
            return None
        return {"state": deepcopy(rec["state"]), "version": rec["version"]}

    def compare_version(self, subject_ref, expected_version):
        rec = self._states.get(subject_ref)
        return rec is not None and rec["version"] == str(expected_version)

    def transition(self, subject_ref, expected_version, new_state, new_version):
        if not self.compare_version(subject_ref, expected_version):
            raise ValueError("STATE_VERSION_MISMATCH")
        self._states[subject_ref] = {"state": deepcopy(new_state), "version": str(new_version)}
        return self.get(subject_ref)

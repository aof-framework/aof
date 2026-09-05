from copy import deepcopy

class ExecutionContractRegistry:
    def __init__(self):
        self._contracts = {}

    def register(self, contract):
        cid = contract["id"]
        if cid in self._contracts:
            raise ValueError("EXECUTION_CONTRACT_ALREADY_REGISTERED")
        rec = deepcopy(contract)
        rec.setdefault("single_use", True)
        rec["consumed"] = False
        self._contracts[cid] = rec
        return deepcopy(rec)

    def get(self, contract_id):
        rec = self._contracts.get(contract_id)
        return deepcopy(rec) if rec else None

    def mark_consumed(self, contract_id):
        rec = self._contracts.get(contract_id)
        if rec is None:
            raise ValueError("EXECUTION_CONTRACT_NOT_FOUND")
        if rec.get("single_use", True) and rec.get("consumed", False):
            raise ValueError("EXECUTION_CONTRACT_REPLAY")
        rec["consumed"] = True
        return deepcopy(rec)

    def validate_replay(self, contract_id):
        rec = self._contracts.get(contract_id)
        if rec is None:
            return False, "EXECUTION_CONTRACT_NOT_FOUND"
        if rec.get("single_use", True) and rec.get("consumed", False):
            return False, "EXECUTION_CONTRACT_REPLAY"
        return True, "EXECUTION_CONTRACT_AVAILABLE"

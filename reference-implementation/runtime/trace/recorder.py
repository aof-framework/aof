from copy import deepcopy

class InMemoryTraceRecorder:
    def __init__(self):
        self._events = []
        self._counter = 0

    def append(self, event):
        self._counter += 1
        event = deepcopy(event)
        event.setdefault("trace_id", f"trace:{self._counter}")
        self._events.append(event)
        return event["trace_id"]

    def all(self):
        return deepcopy(self._events)

    def find_by_execution(self, execution_ref):
        return [e for e in self.all() if e.get("execution_ref") == execution_ref]

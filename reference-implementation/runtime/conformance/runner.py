from datetime import datetime, timezone
from runtime.conformance.engine import aggregate_requirement, aggregate_conformance

class ConformanceRunner:
    def run(self, manifest):
        requirements=[]
        for req in manifest.get("requirements",[]):
            r=dict(req)
            r["requirement_result"]=aggregate_requirement(r)
            requirements.append(r)

        claim=dict(manifest)
        claim["requirements"]=requirements
        final=aggregate_conformance(claim)

        return {
            "id":manifest.get("report_id","conformance-report:reference"),
            "manifest_ref":manifest.get("id"),
            "subject":manifest.get("subject"),
            "subject_version":manifest.get("subject_version"),
            "profile":manifest.get("profile"),
            "scope":manifest.get("scope"),
            "requirements":requirements,
            "exceptions":manifest.get("exceptions",[]),
            "limitations":manifest.get("limitations",[]),
            "final_result":final,
            "timestamp":datetime.now(timezone.utc).isoformat()
        }

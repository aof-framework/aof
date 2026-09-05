from runtime.assurance.verification import VerificationEngine
from runtime.conformance.runner import ConformanceRunner

class AssuranceConformanceFacade:
    def __init__(self, verification_engine=None, conformance_runner=None):
        self.verification_engine=verification_engine or VerificationEngine()
        self.conformance_runner=conformance_runner or ConformanceRunner()

    def verify(self, **kwargs):
        return self.verification_engine.verify(**kwargs)

    def run_conformance(self, manifest):
        return self.conformance_runner.run(manifest)

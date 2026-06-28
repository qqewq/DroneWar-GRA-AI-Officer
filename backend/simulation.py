from .orchestration import Orchestrator
from .models import SwarmState
import threading
import time

class Simulation:
    def __init__(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator
        self.running = False
        self.jamming = 0.0
        self._thread = None

    def start(self, drones: int, jamming: float):
        self.orchestrator.create_swarm(drones)
        self.jamming = jamming
        self.running = True
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def _run(self):
        while self.running:
            self.orchestrator.apply_nullification(self.jamming)
            time.sleep(0.1)

    def get_state(self) -> SwarmState:
        return self.orchestrator.get_state()

    def metrics(self):
        state = self.get_state()
        return {"success_prob": state.hierarchy_stability, "resonance": state.overall_resonance}

from backend.simulation import Simulation
from backend.orchestration import Orchestrator
from backend.nullification import Nullifier

def test_simulation_run():
    orch = Orchestrator(Nullifier())
    sim = Simulation(orch)
    sim.start(drones=10, jamming=0.2)
    import time; time.sleep(0.5)
    state = sim.get_state()
    assert state.overall_resonance > 0.5
    sim.running = False

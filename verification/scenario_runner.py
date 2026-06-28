import numpy as np
from backend.simulation import Simulation
from backend.orchestration import Orchestrator
from backend.nullification import Nullifier

def run_scenario(n_drones, jamming_level, steps=100):
    orch = Orchestrator(Nullifier())
    sim = Simulation(orch)
    sim.start(n_drones, jamming_level)
    resonances = []
    for _ in range(steps):
        state = sim.get_state()
        resonances.append(state.overall_resonance)
        import time; time.sleep(0.01)
    sim.running = False
    return np.mean(resonances), np.std(resonances)

if __name__ == "__main__":
    for jam in [0.0, 0.2, 0.5, 0.8]:
        m, s = run_scenario(20, jam)
        print(f"Jamming={jam:.1f} -> Resonance mean={m:.3f} std={s:.3f}")

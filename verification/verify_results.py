import numpy as np
from scenario_runner import run_scenario

def test_hard_jamming_success():
    m, s = run_scenario(30, 0.9, steps=50)
    assert m > 0.6, f"Resonance too low: {m}"

if __name__ == "__main__":
    test_hard_jamming_success()
    print("Verification passed: GRA nullification maintains swarm coherence under 90% jamming.")

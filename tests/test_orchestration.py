from backend.orchestration import Orchestrator
from backend.nullification import Nullifier

def test_swarm_creation():
    orch = Orchestrator(Nullifier())
    orch.create_swarm(10)
    assert len(orch.drones) == 10
    assert all(d.nullification_active for d in orch.drones)

def test_nullification_preserves_count():
    orch = Orchestrator(Nullifier())
    orch.create_swarm(5)
    orch.apply_nullification(0.5)
    assert len(orch.drones) == 5

from .models import SwarmState, Drone, DroneRole
from .nullification import Nullifier
import numpy as np
import random

class Orchestrator:
    def __init__(self, nullifier: Nullifier):
        self.nullifier = nullifier
        self.drones = []
        self.hierarchy = {}

    def create_swarm(self, n):
        roles = list(DroneRole)
        for i in range(n):
            role = random.choice(roles)
            pos = np.random.uniform(-1, 1, 3).tolist()
            self.drones.append(Drone(id=i, role=role, position=pos, resonance=1.0))
        self._build_hierarchy()

    def _build_hierarchy(self):
        # officer at top, then role-based sub-swarms
        self.hierarchy = {"officer": {"recon": [], "ew": [], "strike": []}}
        for d in self.drones:
            if d.role in (DroneRole.RECON,):
                self.hierarchy["officer"]["recon"].append(d.id)
            elif d.role == DroneRole.EW:
                self.hierarchy["officer"]["ew"].append(d.id)
            else:
                self.hierarchy["officer"]["strike"].append(d.id)

    def apply_nullification(self, jamming):
        for d in self.drones:
            pos = np.array(d.position)
            noise = np.random.normal(0, jamming, 3)
            new_pos = self.nullifier.nullify(pos, noise)
            d.position = new_pos.tolist()
            d.resonance = np.exp(-jamming)  # simplified metric

    def get_state(self) -> SwarmState:
        avg_res = np.mean([d.resonance for d in self.drones])
        return SwarmState(
            drones=self.drones,
            overall_resonance=avg_res,
            nullification_level=1.0 - avg_res,
            hierarchy_stability=1.0 if avg_res > 0.8 else 0.5
        )

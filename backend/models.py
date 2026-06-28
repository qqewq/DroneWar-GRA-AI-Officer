from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class DroneRole(str, Enum):
    RECON = "recon"
    EW = "ew"
    MIDSTRIKE = "midstrike"
    DEEPSTRIKE = "deepstrike"
    CLOSE = "close"

class Drone(BaseModel):
    id: int
    role: DroneRole
    position: List[float]
    resonance: float
    nullification_active: bool = True

class SwarmState(BaseModel):
    drones: List[Drone]
    overall_resonance: float
    nullification_level: float
    hierarchy_stability: float

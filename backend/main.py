from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import SwarmState, Drone
from .nullification import Nullifier
from .orchestration import Orchestrator
from .simulation import Simulation
from .config import settings

app = FastAPI(title="GRA Drone Officer")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

nullifier = Nullifier()
orchestrator = Orchestrator(nullifier)
sim = Simulation(orchestrator)

@app.get("/state", response_model=SwarmState)
async def get_state():
    return sim.get_state()

@app.post("/mission/start")
async def start_mission(drones: int = 10, jamming: float = 0.0):
    sim.start(drones, jamming)
    return {"status": "started"}

@app.get("/metrics")
async def metrics():
    return sim.metrics()

from fastapi import FastAPI
from environment import GrievanceEnv
from models import Action

app = FastAPI()

# sample complaints
complaints = [
    {"text": "Road broken", "category": "road", "priority": "high", "department": "infrastructure"},
    {"text": "Street light not working", "category": "electricity", "priority": "medium", "department": "power"},
    {"text": "No water supply", "category": "water", "priority": "high", "department": "water_board"},
]

env = GrievanceEnv(complaints)

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"complaint": obs.complaint}

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    env.step(act)
    return {"state": env.state()}
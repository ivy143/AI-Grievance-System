from fastapi import FastAPI
from environment import GrievanceEnv
from models import Action
import uvicorn

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
    
    return {
        "complaint": obs.complaint,
        "status": obs.status,
        "history": obs.history
    }

@app.post("/step")
def step(action_data: dict):
    
    act = Action(
        action_type=action_data.get("action_type"),
        value=action_data.get("value")
    )
    obs, reward, done, info = env.step(act)
    
    return {
        "observation": {
            "complaint": obs.complaint,
            "category": obs.category,
            "priority": obs.priority,
            "department": obs.department,
            "status": obs.status,
            "delay": obs.delay
        },
        "reward": reward.score,
        "done": done,
        "info": info
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
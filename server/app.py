import os
import sys
from fastapi import FastAPI
import uvicorn
from openai import OpenAI


client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"), 
    api_key=os.environ.get("API_KEY")


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from environment import GrievanceEnv

app = FastAPI()


complaints = [
    {"text": "Road broken", "category": "road", "priority": "high", "department": "infrastructure"},
    {"text": "Street light not working", "category": "electricity", "priority": "medium", "department": "power"},
    {"text": "No water supply", "category": "water", "priority": "high", "department": "water_board"},
]


env = GrievanceEnv(complaints)

@app.get("/")
def home():
    return {"message": "RCOS Intelligence Server is Running"}

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
    
    from models import Action
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
        "reward": float(reward.score), 
        "done": done,
        "info": info
    }

def main():
    port = int(os.environ.get("PORT", 7860))
    print(f"Starting RCOS Server on port {port}...")
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
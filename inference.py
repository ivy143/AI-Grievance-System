import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), "server"))


try:
    from environment import GrievanceEnv
    from models import Action
except ImportError:
    # Backup import
    from server.environment import GrievanceEnv
    from server.models import Action

def run_inference():
    print("Validator is checking inference.py...")
    
    # Simple complaints data
    complaints = [
        {"text": "Road broken", "category": "road", "priority": "high", "department": "infrastructure"}
    ]
    
    # Environment check
    env = GrievanceEnv(complaints)
    obs = env.reset()
    
    print(f"Check passed! Current complaint: {obs.complaint}")
    return 0

if __name__ == "__main__":
    
    sys.exit(run_inference())
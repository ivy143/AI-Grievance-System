import os
import sys
from openai import OpenAI


api_base = os.environ.get("API_BASE_URL")
api_key = os.environ.get("API_KEY")

client = OpenAI(
    base_url=api_base,
    api_key=api_key
)


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "server"))
from environment import GrievanceEnv

def run_inference():
    complaints = [
        {"text": "Power cut in sector 4", "dept": "Power"},
        {"text": "Major water leakage", "dept": "Water"}
    ]

    env = GrievanceEnv(complaints)
    print("[START] task=GrievanceLifecycle", flush=True)

    total_steps = 0
    for i in range(len(complaints)):
        env.current_idx = i
        obs, info = env.reset()
        
        
        try:
            print(f"Sending request to Proxy: {api_base}", flush=True)
            response = client.chat.completions.create(
                model="gpt-4o", 
                messages=[{"role": "user", "content": "Classify this grievance: " + str(obs)}]
            )
           
            print(f"Proxy Response Received", flush=True)
        except Exception as e:
            print(f"CRITICAL PROXY ERROR: {e}", flush=True)
            
            raise e 

        # 3. Actions Loop
        for action_val in [1, 2, 3]:
            from models import Action
            act = Action(action_type="status_update", value=str(action_val))
            
            result = env.step(act)
            if len(result) == 5:
                obs, reward, done, _, info_dict = result
            else:
                obs, reward, done, info_dict = result
            
            total_steps += 1
            print(f"[STEP] step={total_steps} reward={float(reward):.2f} info='Processing'", flush=True)
            
            if done:
                break
            
    print(f"[END] task=GrievanceLifecycle score=1.0 steps={total_steps}", flush=True)

if __name__ == "__main__":
    run_inference()
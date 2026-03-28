from models import Observation, Action, Reward
import random

class GrievanceEnv:

    def __init__(self, complaints):
        self.complaints = complaints
        self.current = None
        self.done = False

    def reset(self):
        # 1. Pick random complaint from your list
        self.current = random.choice(self.complaints)

        # 2. Initialize observation matching your models.py
        self.state_data = Observation(
            complaint=self.current["text"],
            category=None,
            priority=None,
            department=None,
            status="pending",
            delay=0,
            history=list()
        )

        self.done = False
        return self.state_data

    def state(self):
        return self.state_data

    def step(self, action: Action):
        reward = 0.0
        reason = ""

        # 🔹 1. Classify
        if action.action_type == "classify":
            self.state_data.category = action.value
            if action.value == self.current["category"]:
                reward += 0.5
                reason = "Correct classification"
            else:
                reward -= 0.3
                reason = "Wrong classification"

        # 🔹 2. Priority
        elif action.action_type == "set_priority":
            self.state_data.priority = action.value
            if action.value == self.current["priority"]:
                reward += 0.5
                reason = "Correct priority"
            else:
                reward -= 0.3
                reason = "Wrong priority"

        # 🔹 3. Department
        elif action.action_type == "assign_department":
            self.state_data.department = action.value
            if action.value == self.current["department"]:
                reward += 1.0
                reason = "Correct department"
            else:
                reward -= 0.5
                reason = "Wrong department"

        # 🔹 4. Status Update
        elif action.action_type == "update_status":
            self.state_data.status = action.value
            if action.value in ["in_progress", "resolved"]:
                reward += 0.5
                reason = "Valid status update"
            else:
                reward -= 0.5
                reason = "Invalid status"

        # 🔹 5. Response System
        elif action.action_type == "respond":
            if action.value and len(action.value) > 5:
                reward += 1.0
                reason = "Good response"
            else:
                reward -= 0.5
                reason = "Poor response"

        # 🔹 6. Escalation
        elif action.action_type == "escalate":
            if self.state_data.delay > 2:
                reward += 1.0
                reason = "Correct escalation"
            else:
                reward -= 0.5
                reason = "Unnecessary escalation"

        # 🟡 IMPROVEMENT 1: Invalid Action Safety
        else:
            reward -= 0.2
            reason = "Invalid action type"

        # 🔹 Update delay
        self.state_data.delay += 1
        
        # ⏱️ Delay Penalty
        reward -= 0.1

        # 🔹 Save history
        self.state_data.history.append(action.action_type)

        
        
        if self.state_data.status == "resolved" and self.state_data.department:
            self.done = True

        return self.state_data, Reward(score=reward, reason=reason), self.done, {}

# --- TESTING BLOCK ---
if __name__ == "__main__":
   
    complaints_list = [
        {"text": "Road broken", "category": "road", "priority": "high", "department": "infrastructure"},
        {"text": "Street light off", "category": "electricity", "priority": "medium", "department": "power"},
        {"text": "No water supply", "category": "water", "priority": "high", "department": "water_board"},
    ]

    env = GrievanceEnv(complaints_list)
    obs = env.reset()
    print(f"--- Episode Start ---")
    print(f"Complaint: {obs.complaint}")

    # Step 1: Assign Department
    action1 = Action(action_type="assign_department", value="infrastructure")
    obs, rew, done, _ = env.step(action1)
    print(f"Action: {action1.action_type} | Reward: {rew.score} | Reason: {rew.reason}")

    # Step 2: Resolve
    action2 = Action(action_type="update_status", value="resolved")
    obs, rew, done, _ = env.step(action2)
    print(f"Action: {action2.action_type} | Reward: {rew.score} | Reason: {rew.reason}")
    print(f"Is Finalized?: {done}")
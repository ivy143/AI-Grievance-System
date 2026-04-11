import gymnasium as gym
from gymnasium import spaces
import numpy as np

class GrievanceEnv(gym.Env):
    def __init__(self, complaints_data):
        super(GrievanceEnv, self).__init__()
        self.complaints = complaints_data
        self.current_idx = 0
        self.steps_taken = 0
        self.current_status = 0  # 0:Pending, 1:In_Prog, 2:Escalated, 3:Resolved
        
        # Simple Discrete Action Space
        self.action_space = spaces.Discrete(4)
        
        # Box Observation Space (Fail-proof)
        self.observation_space = spaces.Box(low=0, high=100, shape=(2,), dtype=np.int32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.steps_taken = 0
        self.current_status = 0
        
        # Return observation and empty info dict
        obs = np.array([self.current_status, self.steps_taken], dtype=np.int32)
        return obs, {}

    def step(self, action):
        self.steps_taken += 1
        reward = -0.05  # Efficiency penalty
        
        # Lifecycle Logic: Pending -> In Progress -> Escalated -> Resolved
        if action == 3: 
            self.current_status = 3
            reward += 1.0
        elif action == 2:
            self.current_status = 2
            reward += 0.3
        elif action == 1:
            self.current_status = 1
            reward += 0.1
            
        terminated = bool(self.current_status == 3)
        truncated = False
        obs = np.array([self.current_status, self.steps_taken], dtype=np.int32)
        
        return obs, float(reward), terminated, truncated, {}
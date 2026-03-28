class GrievanceEnv:
    def __init__(self, complaints):
        self.complaints = complaints
        self.current_idx = 0
        
    def reset(self):
        self.current_idx = 0
       
        return self._get_obs()
        
    def _get_obs(self):
        
        comp = self.complaints[self.current_idx]
        class Observation:
            def __init__(self, d):
                self.complaint = d["text"]
                self.category = d.get("category", "")
                self.priority = d.get("priority", "")
                self.department = d.get("department", "")
                self.status = "pending"
                self.delay = 0
                self.history = []
        return Observation(comp)

    def step(self, action):
       
        reward = type('Reward', (), {'score': 1.0})()
        done = False
        info = {}
        obs = self._get_obs()
        return obs, reward, done, info
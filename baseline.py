from analytics import AnalyticsTracker
from environment import GrievanceEnv
from models import Action
from grader import grade_easy, grade_medium, grade_hard

# sample complaints
complaints = [
    {"text": "Road broken", "category": "road", "priority": "high", "department": "infrastructure"},
    {"text": "Street light not working", "category": "electricity", "priority": "medium", "department": "power"},
    {"text": "No water supply", "category": "water", "priority": "high", "department": "water_board"},
]

env = GrievanceEnv(complaints)


tracker = AnalyticsTracker()


def run_episode():
    obs = env.reset()

    # 🔹  CLASSIFICATION LOGIC
    if "light" in obs.complaint.lower():
        category = "electricity"
        department = "power"
        priority = "medium"

    elif "water" in obs.complaint.lower():
        category = "water"
        department = "water_board"
        priority = "high"

    elif "road" in obs.complaint.lower():
        category = "road"
        department = "infrastructure"
        priority = "high"

    else:
        category = "road"
        department = "infrastructure"
        priority = "medium"

    # 🔹 Actions
    env.step(Action(action_type="classify", value=category))
    env.step(Action(action_type="set_priority", value=priority))
    env.step(Action(action_type="assign_department", value=department))
    env.step(Action(action_type="update_status", value="resolved"))

    return env.state(), env.current



for i in range(3):
    state, expected = run_episode()

    # 🎯 Grading
    easy_score = grade_easy(state, expected)
    medium_score = grade_medium(state, expected)
    hard_score = grade_hard(state, expected)

    # 📊  Analytics
    tracker.update(state)

    print(f"\nRun {i+1}")
    print("Easy Score:", easy_score)
    print("Medium Score:", medium_score)
    print("Hard Score:", hard_score)

# 📈 Final Analytics Report
tracker.report()
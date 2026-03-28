from typing import Dict


# 🟢 TASK 1 — EASY (Classification)
def grade_easy(state, expected: Dict):
    score = 0.0

    if state.category == expected["category"]:
        score = 1.0

    return score


# 🟡 TASK 2 — MEDIUM (Routing + Priority)
def grade_medium(state, expected: Dict):
    score = 0.0

    if state.category == expected["category"]:
        score += 0.33

    if state.priority == expected["priority"]:
        score += 0.33

    if state.department == expected["department"]:
        score += 0.34

    return round(score, 2)


# 🔴 TASK 3 — HARD (Full Lifecycle)
def grade_hard(state, expected: Dict):
    score = 0.0

    # classification
    if state.category == expected["category"]:
        score += 0.2

    # priority
    if state.priority == expected["priority"]:
        score += 0.2

    # department
    if state.department == expected["department"]:
        score += 0.2

    # status resolved
    if state.status == "resolved":
        score += 0.2

    # response given
    if len(state.history) > 0:
        score += 0.1

    # escalation logic
    if state.delay > 2:
        score += 0.1

    return round(score, 2)
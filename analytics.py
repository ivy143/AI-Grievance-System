class AnalyticsTracker:

    def __init__(self):
        self.total = 0
        self.resolved = 0
        self.pending = 0
        self.departments = {}

    def update(self, state):
        self.total += 1

        # status tracking
        if state.status == "resolved":
            self.resolved += 1
        else:
            self.pending += 1

        # department tracking
        dept = state.department
        if dept:
            if dept not in self.departments:
                self.departments[dept] = {"total": 0, "resolved": 0}

            self.departments[dept]["total"] += 1

            if state.status == "resolved":
                self.departments[dept]["resolved"] += 1

    def report(self):
        print("\n📊 Complaint Analytics")
        print(f"Total: {self.total}")
        print(f"Resolved: {self.resolved}")
        print(f"Pending: {self.pending}")

        print("\n📈 Department Performance")
        for dept, data in self.departments.items():
            rate = data["resolved"] / data["total"]
            print(f"{dept}: {round(rate,2)} resolution rate")

        print("\n🧾 Transparency Metrics")
        if self.total > 0:
            print(f"Overall Resolution Rate: {round(self.resolved/self.total,2)}")
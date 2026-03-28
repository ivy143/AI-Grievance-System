---
title: Grievance Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---
# 🚀 AI-Powered Public Grievance Redressal Environment (OpenEnv)

---

## 🧠 Problem Statement

Public grievance systems are critical for governance, yet in reality:

* ❌ Complaints are misclassified or ignored
* ❌ No proper tracking of resolution progress
* ❌ Delays are not monitored effectively
* ❌ Citizens lack transparency and accountability

This leads to inefficiency, poor governance, and reduced public trust.

---

## 🎯 Objective

To build a **real-world OpenEnv environment** where AI agents can:

* Understand citizen complaints
* Make decisions like a government system
* Track progress and delays
* Ensure accountability through measurable outcomes

---

## 💡 Solution Overview

This project simulates a **complete grievance lifecycle system**, where an AI agent performs:

1. Complaint classification
2. Priority assignment
3. Department routing
4. Status updates (pending → in_progress → resolved)
5. Response generation
6. Escalation of delayed cases

👉 The system is designed to mimic **real administrative workflows**

---

## 🏗️ Environment Architecture

### 🔄 Core API

* `reset()` → initializes a new complaint
* `step(action)` → processes an action and updates state
* `state()` → returns current environment state

---

## 📊 Observation Space

| Field      | Description                             |
| ---------- | --------------------------------------- |
| complaint  | Raw complaint text                      |
| category   | road / water / electricity / sanitation |
| priority   | low / medium / high                     |
| department | assigned authority                      |
| status     | pending / in_progress / resolved        |
| delay      | steps taken (time simulation)           |
| history    | list of actions taken                   |

---

## 🎮 Action Space

* `classify`
* `set_priority`
* `assign_department`
* `update_status`
* `respond`
* `escalate`

---

## 🧪 Tasks & Evaluation

### 🟢 Easy — Classification

* Correctly classify complaint

### 🟡 Medium — Routing

* Classification + priority + department assignment

### 🔴 Hard — Full Lifecycle

* End-to-end handling including:

  * classification
  * routing
  * response
  * escalation
  * resolution

---

## 🏆 Reward Design

* ✅ Correct decisions → positive reward
* ❌ Wrong actions → penalties
* ⏱️ Delay → continuous penalty
* 🚨 Escalation → rewarded only when justified

👉 This creates a **dense reward signal for learning realistic behavior**

---

## 📊 Tracking & Accountability System 

The environment includes a built-in tracking mechanism:

* **Status Tracking** → monitors complaint progress
* **Delay Tracking** → measures time inefficiency
* **Action History** → logs full decision sequence

👉 This ensures **transparency and auditability**

---

## 📈 Analytics & Transparency Layer 

Beyond simulation, the system provides **governance insights**:

### 📊 Complaint Analytics

* Total complaints
* Resolved vs pending

### 📈 Department Performance

* Resolution rate per department

### 🧾 Transparency Metrics

* Overall system efficiency
* Accountability measurement

👉 This transforms the environment into a **decision-support system**

---

## 🤖 Baseline Agent

A rule-based agent is provided to:

* Demonstrate environment interaction
* Produce reproducible baseline scores

👉 More advanced agents can be evaluated on this environment.

---

## 📦 Sample Complaints

* Road broken
* Street light not working
* Water supply issues
* Garbage overflow
* Drain blockage
* Traffic signal malfunction

---

## ⚙️ Setup & Usage

```bash
pip install -r requirements.txt
python baseline.py
```

---

## 🐳 Docker Support

```bash
docker build -t grievance-env .
docker run grievance-env
```

---

## 📌 Real-World Impact

This environment can be used to:

* Train AI for public service automation
* Benchmark decision-making agents
* Improve governance transparency
* Analyze system performance

---

## 🚀 Future Scope

* Integration with real complaint systems
* Multi-agent coordination
* Live dashboards for monitoring
* NLP-based complaint understanding

---

## 💯 Conclusion

This project goes beyond a simulation and introduces a **structured, measurable, and accountable grievance handling system**, making it highly relevant for real-world AI deployment in governance.

---

## 🏁 Final Note

> This environment is designed not just to solve complaints, but to **evaluate how well AI systems manage real-world responsibilities with accountability and transparency**.

---

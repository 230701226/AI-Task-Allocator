# 🤖 AI-Driven Task Allocation for Cross-Functional Product Teams

A smart optimization system that assigns tasks to the most suitable team members by:
- ✅ Matching required skills
- 🎯 Respecting task priority
- ⏳ Limiting individual workload (max hours)
- 📊 Balancing team effort

> 💼 Perfect for showcasing your logic, modeling, and visual communication skills — great for resumes, demos, and interviews.

---

## 🚀 Key Features

- 🧠 Uses **Linear Programming (LP)** via PuLP
- ✅ Guarantees each task is assigned to a qualified member
- ⏳ Ensures members don’t exceed working hour limits
- 🔁 Drops tasks automatically if team capacity is exceeded
- 📈 Visualizes both **member workload** and **task priorities**

---

## 🛠️ Technologies Used

| Tool          | Role                               |
|---------------|------------------------------------|
| Python 🐍     | Core language                      |
| pandas 📊     | Task/member dataset handling       |
| PuLP 📦       | Optimization model (LP)            |
| matplotlib 📈 | Visualizations & bar charts        |

---

## 🧾 Sample Output

```bash
🧩 REST API Development → Riya (Backend Dev)
🧩 UI Component Setup → Amit (Frontend Dev)
🧩 SQL Report Generation → Neha (Data Analyst)
🧩 Feature Planning → Priya (Product Manager)

🎯 Total Priority Score: 24

import streamlit as st
import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD, GLPK_CMD
import os

# 💡 Install CBC on Streamlit Cloud runtime (safe fallback)
os.system("apt-get install -y coinor-cbc")
# 🎯 Page Config
st.set_page_config(page_title="AI Task Allocator", layout="centered")
st.title("🤖 AI Task Allocator for Product Teams")
st.markdown("Match tasks to team members based on skills, workload, and priorities using smart optimization. 🚀")

# 📤 Upload Section
st.sidebar.header("📄 Upload Inputs")
task_file = st.sidebar.file_uploader("📋 Upload Task CSV", type=["csv"])
member_file = st.sidebar.file_uploader("👥 Upload Team Skills CSV", type=["csv"])

if task_file and member_file:
    tasks = pd.read_csv(task_file)
    skills_df = pd.read_csv(member_file)

    st.subheader("📋 Task List")
    st.dataframe(tasks)

    st.subheader("👥 Team Members & Skills")
    st.dataframe(skills_df)

    # 🔄 Map members and skills
    skills = skills_df.groupby("Member")["Skill"].apply(list).to_dict()
    members = list(skills.keys())

    # 🧠 Define LP model
    model = LpProblem("TaskAssignment", LpMaximize)

    # 📌 Decision Variables
    x = LpVariable.dicts("assign", ((t, m) for t in tasks['Task'] for m in members), cat="Binary")

    # 🎯 Objective: Maximize total priority
    model += lpSum(
        x[t, m] * tasks.loc[tasks['Task'] == t, 'Priority'].values[0]
        for t in tasks['Task'] for m in members
        if tasks.loc[tasks['Task'] == t, 'Required_Skill'].values[0] in skills[m]
    )

    # 📏 Constraint: Each task to at most one qualified member
    for t in tasks['Task']:
        required_skill = tasks.loc[tasks['Task'] == t, 'Required_Skill'].values[0]
        model += lpSum(x[t, m] for m in members if required_skill in skills[m]) <= 1

    # ⏱️ Constraint: Member workload ≤ 12 hours
    for m in members:
        model += lpSum(
            x[t, m] * tasks.loc[tasks['Task'] == t, 'Estimated_Hours'].values[0]
            for t in tasks['Task'] if tasks.loc[tasks['Task'] == t, 'Required_Skill'].values[0] in skills[m]
        ) <= 12

    # ⚙️ Use GLPK Solver (Stable for Streamlit Cloud)
    result = model.solve(GLPK_CMD(msg=0))


    # 📦 Show output
    st.subheader("🧩 Task Assignments")
    if result == 1:
        assigned = []
        for t in tasks['Task']:
            for m in members:
                if (t, m) in x and x[t, m].varValue == 1:
                    assigned.append([t, m])
        df_assigned = pd.DataFrame(assigned, columns=["Task", "Assigned To"])
        st.success("✅ Optimization Complete!")
        st.dataframe(df_assigned)
    else:
        st.error("❌ Infeasible allocation — team may lack skills or be overloaded.")
else:
    st.warning("📥 Please upload both task and skill CSV files to begin.")

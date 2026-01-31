# app.py

from agent.syllabus_loader import fetch_syllabus, save_syllabus_to_file
from agent.memory import create_vector_db, load_vector_db
from agent.planner_agent import generate_study_plan

if __name__ == "__main__":

    # 1️⃣ User input
    subject = input("Enter subject name: ")
    days = int(input("Enter number of days till exam: "))

    # 2️⃣ Fetch syllabus
    syllabus = fetch_syllabus(subject)
    save_syllabus_to_file(syllabus)

    # 3️⃣ Store syllabus in vector DB
    create_vector_db(syllabus)

    # 4️⃣ Load vector DB
    collection = load_vector_db()

    # 5️⃣ Generate study plan
    plan = generate_study_plan(collection, days)

    # 6️⃣ Print study plan
    print("\n📘 Generated Study Plan:\n")

    for day, topics in plan.items():
        if day == "_reasoning":
            continue
        print(f"{day}:")
        for t in topics:
            print(f" - {t}")

    # 7️⃣ Print agent reasoning
    print("\n🧠 Agent Reasoning:")
    for k, v in plan["_reasoning"].items():
        print(f"• {k}: {v}")

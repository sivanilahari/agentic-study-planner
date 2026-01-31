# agent/planner_agent.py

def generate_study_plan(collection, days: int):
    """
    Generates a day-wise study plan from stored syllabus data
    with agent reasoning included.
    """

    # 1️⃣ Fetch documents from vector DB
    results = collection.get(include=["documents"])
    documents = results.get("documents", [])

    if not documents:
        return {}

    # 2️⃣ Flatten documents (Chroma may return list[list[str]])
    if isinstance(documents[0], list):
        topics = [d for sub in documents for d in sub if d.strip()]
    else:
        topics = [d for d in documents if d.strip()]

    # 3️⃣ Importance heuristic (longer topic = more complex)
    def topic_score(topic):
        return len(topic.split())

    # 4️⃣ Sort topics by importance
    topics.sort(key=topic_score, reverse=True)

    # 5️⃣ Heavy-first scheduling
    plan = {}
    index = 0

    for day in range(1, days + 1):
        if day <= 2:  # first 2 days are heavy
            plan[f"Day {day}"] = topics[index:index + 2]
            index += 2
        else:
            if index < len(topics):
                plan[f"Day {day}"] = [topics[index]]
                index += 1
            else:
                plan[f"Day {day}"] = []

    # 6️⃣ Agent reasoning (exam gold)
    plan["_reasoning"] = {
        "strategy": "Heavy-first scheduling",
        "logic": "Complex topics are prioritized earlier when focus is high",
        "total_topics": len(topics),
        "days_allocated": days
    }

    return plan


def explain_topic(collection, topic_name: str):
    """
    Retrieves the most relevant syllabus content for a given topic
    using vector similarity search.
    """

    result = collection.query(
        query_texts=[topic_name],
        n_results=1
    )

    return result["documents"][0][0]

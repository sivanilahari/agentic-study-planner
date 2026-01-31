# agent/syllabus_loader.py

def fetch_syllabus(subject: str) -> str:
    """
    Simulates fetching syllabus content from Endee.
    In real usage, this can be replaced with Endee API calls.
    """

    syllabus_map = {
        "data structures": """
Unit 1: Arrays, Strings, Linked Lists
Unit 2: Stacks and Queues
Unit 3: Trees (BST, AVL, Heaps)
Unit 4: Graphs (BFS, DFS, Shortest Path)
Unit 5: Sorting and Searching Algorithms
        """,

        "python": """
Unit 1: Python Basics and Syntax
Unit 2: Control Structures and Functions
Unit 3: OOP in Python
Unit 4: File Handling and Exceptions
Unit 5: Libraries (NumPy, Pandas, Matplotlib)
        """
    }

    return syllabus_map.get(subject.lower(), "Syllabus not found.")


def save_syllabus_to_file(syllabus_text: str, path: str = "data/syllabus.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(syllabus_text)

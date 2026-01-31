Agentic AI Study Planner using Endee
Project Overview

Students often find it difficult to make effective study plans. This is because of poor prioritization of topics, unstructured study plans, and poor utilization of available study time. Traditional study planners are static in nature and do not account for the complexity and interdependencies of topics in the syllabus.
This project introduces an Agentic AI Study Planner that helps students make a day-wise study plan. The study planner uses vector-based memory and reasoning to understand the syllabus topics at a semantic level and structure them in an intelligent manner.
Endee is employed as the vector database to store the syllabus concepts and retrieve them using semantic search. This helps the AI agent reason about the syllabus and make a realistic study plan.

Problem Statement

The traditional study planners have the following drawbacks:
They consider all topics of equal importance
They do not account for topic difficulty and learning dependencies
They lack memory, reasoning, and adaptability
Because of these drawbacks, students feel overwhelmed or spend time on less important topics while neglecting more important topics.                     Solution Approach

The Agentic AI Study Planner overcomes these issues by integrating agent-based reasoning with vector search as follows:
It interprets syllabus topics based on their meaning, not just keywords
It identifies difficult and important topics using semantic similarity
It dynamically changes the study plan based on time constraints and learning objectives
It provides a simple and understandable day-wise study plan
The solution ensures that the student studies the right topics at the right time.

System Design and Technical Approach
Architecture Flow

Syllabus Input
The student enters the syllabus topics and the number of days available for studying. This input is the point of departure for the study planning process.

Vector Storage using Endee
The system represents each syllabus topic as a vector embedding and stores it in Endee, which is the vector-based knowledge storage.

Semantic Retrieval
The system retrieves relevant topics from Endee using vector similarity search, allowing the system to identify related concepts and dependencies.

Agentic Reasoning
An AI agent evaluates topic difficulty, importance, and the available study time to determine the best order of study.

Study Plan Generation
The system provides a personalized day-wise study plan that is logically organized, easy to understand, and effective for exam preparation.
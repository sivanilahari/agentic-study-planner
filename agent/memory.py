# agent/memory.py

from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import re

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_db(syllabus_text: str):
    client = Client(
        Settings(
            persist_directory="vector_store",
            anonymized_telemetry=False,
            chroma_db_impl="duckdb+parquet"   # 🔥 THIS IS THE FIX
        )
    )

    collection = client.get_or_create_collection(name="syllabus_memory")

    # Better splitting
    lines = [l.strip() for l in re.split(r"[.\n]", syllabus_text) if l.strip()]

    embeddings = model.encode(lines).tolist()

    for i, text in enumerate(lines):
        collection.add(
            documents=[text],
            embeddings=[embeddings[i]],
            ids=[str(i)]
        )

    client.persist()  # ✅ Now this WORKS


def load_vector_db():
    client = Client(
        Settings(
            persist_directory="vector_store",
            anonymized_telemetry=False,
            chroma_db_impl="duckdb+parquet"
        )
    )

    return client.get_or_create_collection(name="syllabus_memory")

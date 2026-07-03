"""Example entry point for HR document search.

This file can be used as a beginner-friendly starting point for running
queries against the indexed HR documents.
"""

from qdrant_client import QdrantClient

from embeddings import create_embedding


def query_hr_documents(question: str, limit: int = 3):
    """Query the HR documents collection for a question."""
    client = QdrantClient(path="./qdrant_data")

    query_vector = create_embedding(question)

    results = client.query_points(
        collection_name="hr_docs",
        query=query_vector,
        limit=limit,
    )

    return results


if __name__ == "__main__":
    user_question = "How many leave days do employees get?"
    print("Query:", user_question)
    response = query_hr_documents(user_question)

    for point in response.points:
        print("Score:", point.score)
        print("Text:", point.payload["text"])
        print("---------")

"""Simple example to query the indexed HR documents.

This module demonstrates how to:
- create an embedding for a question,
- query the local Qdrant collection,
- and print matching HR policy text.
"""

from typing import Any, List

from qdrant_client import QdrantClient

from embeddings import create_embedding


def create_qdrant_client(path: str = "./qdrant_data") -> QdrantClient:
    """Create a Qdrant client connected to the local database folder.

    Args:
        path: Path to the local Qdrant storage folder.

    Returns:
        A QdrantClient instance connected to the given path.
    """
    return QdrantClient(path=path)


def search_hr_documents(client: QdrantClient, question: str, limit: int = 3) -> List[Any]:
    """Search the `hr_docs` collection for the most relevant chunks.

    Args:
        client: A Qdrant client instance.
        question: The natural-language question to search for.
        limit: The maximum number of results to return.

    Returns:
        A list of scored points returned by Qdrant.
    """
    query_vector = create_embedding(question)
    results = client.query_points(
        collection_name="hr_docs",
        query=query_vector,
        limit=limit,
    )
    return results.points

# In Python, None means:
# No value or Nothing. It is often used as a default value for function arguments or to indicate the absence of a return value.
def print_search_results(points: List[Any]) -> None:
    """Print the search results in a readable format.

    Args:
        points: List of Qdrant points returned from the search.
    """
    if not points:
        print("No results found.")
        return

    for point in points:
        print(point.score)
        print(point.payload["text"])
        print("---------")

# In Python, None means:
# No value or Nothing. It is often used as a default value for function arguments or to indicate the absence of a return value.
def main() -> None:
    """Run a query against the local HR document index using user input."""
    client = create_qdrant_client()
    # question = "How many leave days do employees get?"
    # Prompt the user for a question
    question = input("Enter your HR question: ").strip()
    if not question:
        print("No question entered. Exiting.")
        client.close()
        return

    results = search_hr_documents(client, question)
    print_search_results(results)
    client.close()


if __name__ == "__main__":
    main()
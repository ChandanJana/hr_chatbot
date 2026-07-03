"""Simple inspector to list points stored in the `hr_docs` Qdrant collection.

This script prints point id, source file, and a short preview of the stored text.
"""

from qdrant_client import QdrantClient


# In Python, None means:
# No value or Nothing. It is often used as a default value for function arguments or to indicate the absence of a return value.
def inspect_collection(limit: int = 50) -> None:
    """Inspect the `hr_docs` Qdrant collection and print stored points.

    Args:
        limit: Maximum number of points to retrieve from Qdrant.

    Returns:
        None. The function prints a summary line for each point found.
    """
    client = QdrantClient(path="./qdrant_data")

    try:
        # Use scroll to retrieve stored points (with payloads)
        resp = client.scroll(collection_name="hr_docs", limit=limit, with_payload=True)
    except Exception as e:
        print("Error reading collection:", e)
        return

    points = resp[0] if resp else []
    if not points:
        print("No points found in collection or collection does not exist.")
        return

    for p in points:
        pid = getattr(p, "id", None)
        payload = getattr(p, "payload", {}) or {}
        text = payload.get("text", "")
        file = payload.get("file", "")
        print(f"- id: {pid} | file: {file} | text preview: {text[:120]!r}")


# ------------------------------------------------------------------
# Test Section
# ------------------------------------------------------------------
# The code inside this block executes only when this file is run
# directly from the command line.
#
# Example:
#     python3 app/inspect_qdrant.py
#
# In this case:
#     __name__ == "__main__"  → True
#
# Therefore, the test code below will execute.
#
# However, when this file is imported into another module:
#
#     from inspect_qdrant import inspect_collection
#
# Then:
#     __name__ == "inspect_qdrant"   → False
#
# As a result, the test code is skipped and only the functions
# defined in this file are imported.
#
# This is a standard Python practice used to:
#   • Keep reusable functions separate from test code
#   • Prevent test code from running during imports
#   • Allow the file to be executed independently for debugging
# ------------------------------------------------------------------

if __name__ == "__main__":
    inspect_collection(limit=100)

"""Initialize the Qdrant collection for the HR chatbot.

This module creates or recreates the `hr_docs` collection with the correct
vector configuration for OpenAI embeddings.
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


# In Python, None means:
# No value or Nothing. It is often used as a default value for function arguments or to indicate the absence of a return value.
def create_hr_docs_collection(path: str = "./qdrant_data") -> None:
    """Create or recreate the `hr_docs` Qdrant collection.

    Args:
        path: Local folder where Qdrant stores its data.

    Returns:
        None. The function creates the collection and prints a status message.
    """
    client = QdrantClient(path=path)
    client.recreate_collection(
        collection_name="hr_docs",
        vectors_config=VectorParams(
            size=1536,
            distance=Distance.COSINE,
        ),
    )
    print("Collection created")
    client.close()

# ------------------------------------------------------------------
# Test Section
# ------------------------------------------------------------------
# The code inside this block executes only when this file is run
# directly from the command line.
#
# Example:
#     python3 app/qdrant_service.py
#
# In this case:
#     __name__ == "__main__"  → True
#
# Therefore, the test code below will execute.
#
# However, when this file is imported into another module:
#
#     from qdrant_service import create_hr_docs_collection
#
# Then:
#     __name__ == "qdrant_service"   → False
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
    create_hr_docs_collection()

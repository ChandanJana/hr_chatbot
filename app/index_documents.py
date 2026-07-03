"""Index HR documents into Qdrant using OpenAI embeddings.

This module loads documents from the `documents/` folder, converts each
supported file into text, chunks the text, creates OpenAI embeddings for
each chunk, and stores the result in a local Qdrant collection.
"""

import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from embeddings import create_embedding
from chunker import chunk_text
from extract_pdf import read_all_documents


client = QdrantClient(path="./qdrant_data")

# In Python, None means:
# No value or Nothing. It is often used as a default value for function arguments or to indicate the absence of a return value.
def index_all_documents(folder: str = "documents") -> None:
    """Index all supported documents in the given folder.

    The function reads every supported document in `folder`, generates text
    chunks, converts each chunk into an embedding, and stores the chunks in
    the `hr_docs` Qdrant collection.

    Supported document types:
    - .txt
    - .pdf

    Args:
        folder: Path to the folder containing documents to index.

    Returns:
        None. The function writes points into Qdrant and prints a summary.
    """
    documents = read_all_documents(folder)
    if not documents:
        print(f"No supported documents found in {folder}")
        return

    points = []
    # enumerate(sorted(documents.items()))
    # This function returns an iterator that yields pairs of (index, (key, value)) for each item in the sorted dictionary.
    # The sorted() function sorts the dictionary items  alphabetically by key (filename) in ascending order.
    # The enumerate() function adds an index to each item, starting from 0.
    # This expression combines three Python concepts:
    # documents.items() → Get key-value pairs from a dictionary.
    # sorted(...) → Sort those pairs by key.
    # enumerate(...) → Add an index to each item.
    # Step 1: documents.items()
    # documents.items()

    # Returns:

    # dict_items([
    #     ("leave_policy.pdf", "Leave policy text"),
    #     ("attendance.pdf", "Attendance text"),
    #     ("employee_handbook.pdf", "Handbook text")
    # ])
    # Step 2: sorted(documents.items())

    # Sorts the dictionary items alphabetically by key:

    # sorted(documents.items())

    # Returns:

    # [
    #     ("attendance.pdf", "Attendance text"),
    #     ("employee_handbook.pdf", "Handbook text"),
    #     ("leave_policy.pdf", "Leave policy text")
    # ]
    # Step 3: enumerate(sorted(documents.items()))

    # Adds an index to each tuple:

    # enumerate(sorted(documents.items()))

    # Produces:

    # [
    #     (0, ("attendance.pdf", "Attendance text")),
    #     (1, ("employee_handbook.pdf", "Handbook text")),
    #     (2, ("leave_policy.pdf", "Leave policy text"))
    # ]
    for file_idx, (filename, text) in enumerate(sorted(documents.items())):
        if not text.strip():
            print(f"Skipping empty document: {filename}")
            continue

        chunks = chunk_text(text)
        for chunk_idx, chunk in enumerate(chunks):
            vector = create_embedding(chunk)
            source_id = f"{file_idx}_{chunk_idx}"
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={
                        "text": chunk,
                        "file": filename,
                        "source_id": source_id,
                    },
                )
            )

    if not points:
        print("No chunks were indexed because no document text was available.")
        return

    client.upsert(collection_name="hr_docs", points=points)
    print(f"Indexed {len(points)} points from {len(documents)} document(s)")


# ------------------------------------------------------------------
# Test Section
# ------------------------------------------------------------------
# The code inside this block executes only when this file is run
# directly from the command line.
#
# Example:
#     python3 app/index_documents.py
#
# In this case:
#     __name__ == "__main__"  → True
#
# Therefore, the test code below will execute.
#
# However, when this file is imported into another module:
#
#     from index_documents import index_all_documents
#
# Then:
#     __name__ == "index_documents"   → False
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
    index_all_documents()

client.close()
"""Simple helper to split long text into smaller pieces.

This helper is useful because embeddings work better when text is not too large.
"""

from email.mime import text
from fileinput import filename
from typing import Dict
from unittest import result


def chunk_text(text: str, size: int = 1000, overlap: int = 200) -> list[str]:
    """Split text into overlapping chunks.

    Args:
        text: Full string to split into chunks.
        size: Maximum number of characters in each chunk.
        overlap: Number of shared characters between consecutive chunks.

    Returns:
        A list of text chunks. If the text is shorter than `size`, the result
        contains a single chunk equal to the input text.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    return chunks


def chunk_documents(documents: Dict[str, str], size: int = 1000) -> Dict[str, list[str]]:
    """Chunk all loaded documents.

    Args:
        documents: Mapping of file name to document text.
        size: Maximum number of characters in each chunk.

    Returns:
        A dictionary where each key is a file name and each value is a list of
        chunked text segments for that document.
    """
    result = {}

    for filename, text in documents.items():
        result[filename] = chunk_text(text, size=size)
    return result

    #is equivalent to:
    # return {
    #     filename: chunk_text(text, size=size) 
    #     for filename, text in documents.items()
    # }

# ------------------------------------------------------------------
# Test Section
# ------------------------------------------------------------------
# The code inside this block executes only when this file is run
# directly from the command line.
#
# Example:
#     python3 app/chunker.py
#
# In this case:
#     __name__ == "__main__"  → True
#
# Therefore, the test code below will execute.
#
# However, when this file is imported into another module:
#
#     from chunker import chunk_text
#
# Then:
#     __name__ == "chunker"   → False
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
    from extract_pdf import read_all_documents

    all_docs = read_all_documents()
    """
    if not all_docs:
    
    This means:
    No PDFs found, or
    Loading failed and returned an empty collection

    In Python, every object has a truth value. When an object is used in 
    conditions like if, while, or with and/or, Python automatically
    treats it as either Truthy (True) or Falsy (False).

    Truthy vs Falsy

    These values are considered False in Python:

    None
    False
    0
    ""
    []
    {}
    set()

    Equivalent code 
    if len(all_docs) == 0:

    If no documents are found, print a message and exit.
    Otherwise, chunk the documents and print information about the chunks.
    
    Comparison Table
    Value	     Truth Value
    []	           False
    [1, 2]	       True
    {}	           False
    {"a": 1}	   True
    ""	           False
    "abc"	       True
    0	           False
    10	           True
    None	       False
    False	       False
    True	       True
    """
    if not all_docs:
        print("No supported documents found in the documents/ folder.")
    else:
        all_chunks = chunk_documents(all_docs, size=1000)
        
        #This loops through each key-value pair in the dictionary all_chunks
        for filename, chunks in all_chunks.items():
            print(f"✓ Document: {filename}")
            print(f"✓ Total length: {len(all_docs[filename])} characters")
            print(f"✓ Created: {len(chunks)} chunks")
            if chunks:
                print(f"\nFirst chunk:\n{chunks[0]}\n")
                if len(chunks) > 1:
                    print(f"Second chunk:\n{chunks[1]}")
            print("---")


# if __name__=="__main__":

#     text="""
# Employees receive 20 leave days annually.

# Unused leave up to 5 days can be carried forward.

# Employees may work remotely.
# """

#     chunks=chunk_text(text)

#     print(chunks)
"""OpenAI embedding helper for the HR chatbot.

This module loads the API key from `.env` and provides a function
that converts text into a numeric vector.
"""

import os
from typing import Sequence

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sequence[float] is a type hint in Python. It means:
# "A sequence (ordered collection) whose elements are of type float."
# Why use Sequence instead of list?
# 1. Flexibility: Sequence is more general than list. It can represent
#    any ordered collection, not just lists. This allows the function to
#    accept a wider range of input types, such as tuples or custom sequence
#    classes, as long as they behave like a sequence.
# 2. Readability: Using Sequence makes it clear that the function is
#    designed to work with any ordered collection, not just lists. This can
#    improve code readability and understanding for other developers.
# 3. Type Safety: By specifying Sequence[float], you indicate that the
#    function expects a sequence of floating-point numbers. This can help
#    catch type-related errors during development and improve code quality.
# Using Sequence
# Accepts:
# list[float]
# tuple[float, ...]
# Other sequence-like objects
# This makes the function more flexible.
def create_embedding(text: str) -> Sequence[float]:
    """Create an embedding vector for the given text.

    Args:
        text: The input text to convert into a vector.

    Returns:
        A numeric embedding vector returned by the OpenAI embeddings API.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding


# ------------------------------------------------------------------
# Test Section
# ------------------------------------------------------------------
# The code inside this block executes only when this file is run
# directly from the command line.
#
# Example:
#     python3 app/embedding.py
#
# In this case:
#     __name__ == "__main__"  → True
#
# Therefore, the test code below will execute.
#
# However, when this file is imported into another module:
#
#     from embedding import create_embedding
#
# Then:
#     __name__ == "embedding"   → False
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
    vector = create_embedding("Employees receive 20 leave days.")
    print(len(vector))
    print(vector[:10])
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_entities(question: str) -> dict:
    """Extract structured entities from a user question.

    Args:
        question: The natural-language question to analyze.

    Returns:
        A dictionary containing the extracted entities in the format
        expected by the downstream prompt pipeline.
    """

    from llm.prompt_builder import ENTITY_EXTRACTION_SYSTEM_PROMPT

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": ENTITY_EXTRACTION_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    import json

    return json.loads(
        response.choices[0].message.content
    )
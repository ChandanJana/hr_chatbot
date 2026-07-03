import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

from llm.prompt_builder import FINAL_ANSWER_SYSTEM_PROMPT, build_final_answer_prompt

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_final_answer(
    question: str,
    document_context: str,
    database_rows: list[Any]
) -> str:
    """
    Generate the final answer using both document context and
    database query results.

    Args:
        question:
            User's natural-language question.

        document_context:
            Context retrieved from the vector database.
            Empty string if no document search was performed.

        database_rows:
            Rows returned from the SQL query.
            Empty list if no database search was performed.

    Returns:
        A concise natural-language answer.
    """

    prompt = build_final_answer_prompt(
        question=question,
        document_context=document_context,
        database_rows=database_rows
    )

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content": FINAL_ANSWER_SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": prompt
            }

        ]

    )

    return response.choices[0].message.content.strip()
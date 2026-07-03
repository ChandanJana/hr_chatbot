import os

from search import answer_document_question
from text_to_sql import answer_database_question

from search import (
    answer_document_question
)

from dotenv import load_dotenv
from openai import OpenAI

from text_to_sql import (
    answer_database_question
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def hybrid_search(question: str):

    document_answer, sources = answer_document_question(question)

    database_answer = answer_database_question(question)

    return (
        document_answer,
        sources,
        database_answer
    )

def combine_answers(
    question,
    document_answer,
    database_answer
):
    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role":"system",

                "content":
                """
                You are an HR assistant.

                Combine the information from both sources.

                Rules:

                1. If only one answer contains useful information,
                    return that answer.

                2. If both answers contain useful information,
                    merge them naturally.

                3. Do not repeat information.

                4. If neither contains useful information,
                    say:

                Sorry, I couldn't find the requested information.
                """
            },

            {
                "role":"user",

                "content":
                f"""
                Question:

                {question}

                Document Answer:

                {document_answer}

                Database Answer:

                {database_answer}
                """
            }

        ]
    )

    return response.choices[0].message.content

def answer_hybrid(question):

    document_answer, sources = answer_document_question(
        question
    )

    database_answer = answer_database_question(
        question
    )

    answer = combine_answers(

        question,

        document_answer,

        database_answer
    )

    return answer, sources
import os

from dotenv import load_dotenv
from openai import OpenAI

from ConfirmationRequired import ConfirmationRequired
from search import answer_document_question, retrieve_document_context
from text_to_sql import answer_database_question
from llm.answer_generator import generate_final_answer
from llm.prompt_builder import CLASSIFIER_SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def classify_question(question: str) -> str:
    """
    Decide whether the question should be answered
    from the SQL database or document index.
    """

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",

                "content": CLASSIFIER_SYSTEM_PROMPT
                # """
                # Classify the user's question.

                # Return ONLY:

                # DATABASE

                # or

                # DOCUMENT

                # DATABASE:
                # - employee details
                # - employee salary
                # - leave balance
                # - attendance
                # - department information
                # - records stored in tables

                # DOCUMENT:
                # - company policy
                # - handbook
                # - leave policy
                # - reimbursement policy
                # - uploaded files
                # - HR documents
                # """
            },

            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content.strip().upper()


def main():

    print("HR Assistant Started")
    print("Type 'exit' to quit")

    pending_confirmation = None

    while True:

        user_input = input("\nAsk a question (or type exit): ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        #
        # Handle confirmation
        #

        if pending_confirmation:

            if user_input.lower() in ("yes", "y"):

                question = pending_confirmation["question"].replace(
                    pending_confirmation["original"],
                    pending_confirmation["corrected"]
                )

                print(f"\nUsing corrected question: {question}")

                pending_confirmation = None

            elif user_input.lower() in ("no", "n"):

                print("Okay. Please type your question again.")

                pending_confirmation = None
                continue

            else:

                print("Please answer yes or no.")
                continue

        else:

            question = user_input

        document_context = ""
        database_rows = []
        sources = []

        try:

            intent = classify_question(question)

            print(f"\nClassified Intent: {intent}")

            if intent == "DOCUMENT":

                document_context, sources = answer_document_question(question)

            elif intent == "DATABASE":

                database_rows = answer_database_question(question)

            else: #HYBRID

                document_context, sources = retrieve_document_context(question)

                database_rows = answer_database_question(question)

                # context, sources = answer_document_question(question)

                # rows = answer_database_question(question)

            answer = generate_final_answer(

                question,

                document_context,

                database_rows
            )

            print("\nAnswer:\n")
            print(answer)

            if sources:

                print("\nSources:")

                for source in sources:

                    print(f"- {source}")

        except ConfirmationRequired as e:

                pending_confirmation = {
                    "question": question,
                    "original": e.original,
                    "corrected": e.corrected
                }

                print(f"\nDid you mean '{e.corrected}'? (yes/no)")

                continue

        except Exception as e:

            print("\nError:")
            print(e)


if __name__ == "__main__":
    main()
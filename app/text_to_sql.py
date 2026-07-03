import os

from openai import OpenAI
from dotenv import load_dotenv

from query_preprocessor import correct_question

from sql_search import execute_query

from text_normalizer import normalize_question

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_sql(question: str) -> str:

    from llm.prompt_builder import SQL_GENERATION_SYSTEM_PROMPT
    from sql_search import (get_database_schema)

    schema = get_database_schema()

    system_prompt = f"""
    You are an expert SQLite query generator.

    Convert the user's question into a valid SQLite SELECT query.

    Database Schema:

    {schema}

    IMPORTANT RULES:

    1. Return ONLY the SQL query.
    2. Do NOT use markdown.
    3. Generate ONLY SELECT statements.
    4. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE.
    5. Use only columns that exist in the schema.

    TEXT SEARCH RULES:

    1. Text comparisons must be case-insensitive.

    2. Exact match:

    LOWER(column_name) = LOWER('value')

    3. Partial match:

    LOWER(column_name) LIKE LOWER('%value%')
    """

    print("Original:", question)

    question = normalize_question(question)

    print("Corrected:", question)

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",

                "content": SQL_GENERATION_SYSTEM_PROMPT
                # """
                # Convert the user's question into SQLite SQL.

                # Table:

                # employees(
                #     id INTEGER,
                #     name TEXT,
                #     department TEXT,
                #     salary INTEGER,
                #     leave_balance INTEGER
                # )

                # IMPORTANT RULES:

                # 1. Return ONLY the SQL query.
                # 2. Do NOT use ```sql or ``` markdown.
                # 3. Do NOT explain anything.
                # 4. Generate ONLY SELECT statements.
                # """
            },

            {
                "role": "user",
                "content": question
            }
        ]
    )

    sql = response.choices[0].message.content.strip()

    # Remove markdown if model still returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql

def generate_answer(question: str,rows: list) -> str:

    from llm.prompt_builder import SQL_SYSTEM_PROMPT, build_sql_prompt
    
    prompt = build_sql_prompt(
    question,
    rows
    )

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",

                "content": SQL_SYSTEM_PROMPT
                # """
                # You are a helpful HR assistant.

                # Answer the user's question using ONLY the database result.

                # Rules:
                # 1. Give a concise and accurate answer.
                # 2. Do not mention SQL queries.
                # 3. Do not mention databases.
                # 4. If the result is empty, say:
                #    No matching records were found.
                # """
            },

            {
                "role": "user",

                "content": prompt
                # f"""
                # Question:
                # {question}

                # Database Result:
                # {rows}
                # """
            }
        ]
    )

    return response.choices[0].message.content

def answer_database_question(question: str) -> list:

    # corrected_question = correct_question(question)

    # print("\nCorrected Question:")
    # print(corrected_question)

    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)

    rows = execute_query(sql)

    print("\nRows:")
    print(rows)

    return rows

def main():

    while True:

        question = input("\nAsk: ").strip()

        if question.lower() == "exit":
            break

        try:

            corrected_question = correct_question(question)
            sql = generate_sql(corrected_question)

            print("\nGenerated SQL:")
            print(sql)

            rows = execute_query(sql)

            if not rows:

                print("\nAnswer:")
                print("No matching records were found.")
                continue

            answer = generate_answer(
                corrected_question,
                rows
            )

            print("\nAnswer:")
            print(answer)

        except Exception as e:

            print("\nError:")
            print(e)


if __name__ == "__main__":

    main()
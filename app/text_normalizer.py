
import re

from rapidfuzz import process, fuzz

from ConfirmationRequired import ConfirmationRequired
from keyword_corrector import correct_keywords
from sql_search import execute_query

from llm.entity_extractor import extract_entities
from query_preprocessor import (correct_name, correct_department, find_best_match, find_department_match, find_name_match)


def get_column_values(
    table: str,
    column: str
) -> list[str]:

    rows = execute_query(
        f"SELECT DISTINCT {column} FROM {table}"
    )

    return [
        row[column]
        for row in rows
        if row.get(column) is not None
    ]


def normalize_question(
    question: str
) -> str:
    """
    Replace misspelled employee names and departments
    with the closest values from the database.
    """

    entities = extract_entities(question)
    print("Extracted Entities:", entities)

    if entities["employee_name"]:

        match, status = find_name_match(
            entities["employee_name"],
            get_column_values("employees", "name")
        )

        if status == "AUTO":

            question = question.replace(
                entities["employee_name"],
                match
            )

        elif status == "CONFIRM":

            raise ConfirmationRequired(
                original=entities["employee_name"],
                corrected=match,
                entity_type="employee"
            )

        elif status == "UNKNOWN":

            raise ValueError(
                "Unknown employee."
            )

        # match = find_best_match(
        #     entities["employee_name"],
        #     get_column_values("employees", "name")
        # )

        # if match:
        #     question = question.replace(
        #         entities["employee_name"],
        #         match
        #     )

    if entities["department"]:

        # match = find_best_match(
        #     entities["department"],
        #     get_column_values("employees", "department")
        # )

        # if match:
        #     question = question.replace(
        #         entities["department"],
        #         match
        #     )

        match, status = find_department_match(
            entities["department"],
            get_column_values("employees", "department")
        )

        if status == "AUTO":
            question = question.replace(
                entities["department"],
                match
            )

        elif status == "CONFIRM":
            #print(">>> Raising ConfirmationRequired")
            raise ConfirmationRequired(
                original=entities["department"],
                corrected=match,
                entity_type="department"
            )
            # raise ValueError(
            #     f"Did you mean department '{match}'?"
            # )

        elif status == "UNKNOWN":
            raise ValueError(
                "Unknown department."
            )
    
        #question = correct_keywords(question)

        #question = correct_name(question)

        #question = correct_department(question)

    return question

    # names = get_column_values(
    #     "employees",
    #     "name"
    # )

    # departments = get_column_values(
    #     "employees",
    #     "department"
    # )

    # question = replace_from_candidates(
    #     question,
    #     names
    # )

    # question = replace_from_candidates(
    #     question,
    #     departments
    # )

    # return question


def replace_from_candidates(
    text: str,
    candidates: list[str],
    cutoff: int = 50
) -> str:

    words = re.findall(r"\w+", text)

    corrected = text

    for word in words:

        # Ignore very short/common words
        # if len(word) < 3:
        #     continue

        result = process.extractOne(
            word,
            candidates,
            scorer=fuzz.WRatio
        )

        if result is None:
            continue

        match, score, _ = result

        if score >= cutoff:

            corrected = re.sub(
                rf"\b{re.escape(word)}\b",
                match,
                corrected,
                flags=re.IGNORECASE
            )

    return corrected
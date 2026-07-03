from difflib import get_close_matches
from rapidfuzz import process, fuzz

from sql_search import execute_query

import re

def find_best_match(
    value: str,
    candidates: list[str],
    cutoff: int = 85
) -> str | None:
    """Find the closest candidate match for a value using fuzzy matching.

    Args:
        value: The input string to match.
        candidates: Candidate strings to compare against.
        cutoff: Minimum similarity score required to accept a match.

    Returns:
        The best matching candidate string, or None if no match meets the cutoff.
    """

    if not value:
        return None

    value = value.strip()

    # Map lowercase -> original value
    candidate_map = {
        candidate.lower(): candidate.strip()
        for candidate in candidates
    }

    result = process.extractOne(
        value.lower(),
        list(candidate_map.keys()),
        scorer=fuzz.WRatio
    )

    if result is None:
        return None

    match, score, _ = result

    print(f"Searching: {value}")
    print(f"Matched: {candidate_map[match]} ({score:.1f})")

    if score >= cutoff:
        return candidate_map[match]

    return None

def get_column_values(
    table: str,
    column: str
) -> list[str]:
    """Return distinct values from a database column.

    Args:
        table: The database table to query.
        column: The column whose distinct values should be fetched.

    Returns:
        A list of distinct non-empty values from the specified column.
    """

    rows = execute_query(
        f"SELECT DISTINCT {column} FROM {table}"
    )

    return [
        row[0]
        for row in rows
        if row[0]
    ]


# def find_best_match(
#     value: str,
#     candidates: list[str],
#     cutoff: float = 0.7
# ) -> str | None:
#     """
#     Find the closest matching string.
#     """

#     matches = get_close_matches(
#         value,
#         candidates,
#         n=1,
#         cutoff=cutoff
#     )

#     if matches:
#         return matches[0]

#     return None


def correct_question(
    question: str
) -> str:
    """Correct likely employee names and departments in a question.

    Args:
        question: The original user question to normalize.

    Returns:
        A corrected question string with better-matching employee names and departments.
    """

    corrected = question

    names = get_column_values("employees", "name")
    departments = get_column_values("employees", "department")
    print(names)
    print(departments)
    words = re.findall(r"[A-Za-z]+", question)

    for word in words:

        match = find_best_match(word, names)

        print(word, "->", match)

        if match and match.lower() != word.lower():

            corrected = re.sub(
                rf"\b{re.escape(word)}\b",
                match,
                corrected,
                flags=re.IGNORECASE
            )

    words = re.findall(r"[A-Za-z]+", corrected)

    for word in words:

        match = find_best_match(word, departments)

        print(word, "->", match)

        if match and match.lower() != word.lower():

            corrected = re.sub(
                rf"\b{re.escape(word)}\b",
                match,
                corrected,
                flags=re.IGNORECASE
            )

    return corrected

def correct_name(name):
    """Return the closest employee name match for a possibly misspelled input.

    Args:
        name: The user-provided employee name.

    Returns:
        The best matching employee name from the database, or the original name if no confident match is found.
    """

    if not name:
        return None

    names = get_column_values(
        "employees",
        "name"
    )

    result = process.extractOne(
        name,
        names
    )

    if result is None:
        return name

    match, score, _ = result

    if score >= 55:
        return match

    return name

def correct_department(department):
    """Return the closest department match for a possibly misspelled input.

    Args:
        department: The user-provided department name.

    Returns:
        The best matching department from the database, or the original value if no confident match is found.
    """

    if not department:
        return None

    departments = get_column_values(
        "employees",
        "department"
    )

    result = process.extractOne(
        department,
        departments
    )

    if result is None:
        return department

    match, score, _ = result

    if score >= 60:
        return match

    return department

def find_department_match(
    value: str,
    departments: list[str]
) -> str | None:
    """Find the best department match for a value using fuzzy matching.

    Args:
        value: The department value to match.
        departments: Candidate department names.

    Returns:
        The best matching department name, or None if no suitable match is found.
    """

    if not value:
        return None

    #value = value.strip().lower()
    value = value.strip().upper()
    departments = [d.upper() for d in departments]

    # Exact match
    for dept in departments:
        if dept == value:
            return dept

    # Use ratio for very short abbreviations
    scorer = fuzz.ratio if len(value) <= 2 else fuzz.WRatio
    

    result = process.extractOne(
        value,
        departments,
        scorer=scorer
    )

    if result is None:
        return None, "UNKNOWN"

    match, score, _ = result

    print(f"Department: {value}")
    print(f"Matched: {match} ({score:.1f})")

    # cutoff = 50 if len(value) <= 2 else 85
    # if score >= cutoff:
    #     return match
    # return None
    
    if len(value) <= 2:

        if score >= 50:
            return match, "AUTO"

        elif score >= 30:
            return match, "CONFIRM"

        return None, "UNKNOWN"
    else:

        if score >= 85:
            return match, "AUTO"

        elif score >= 50:
            return match, "CONFIRM"

        return None, "UNKNOWN"
    
def find_name_match(
    value: str,
    candidates: list[str]
) -> tuple[str | None, str]:

    if not value:
        return None, "UNKNOWN"

    result = process.extractOne(
        value.strip(),
        candidates,
        scorer=fuzz.WRatio
    )

    if result is None:
        return None, "UNKNOWN"

    match, score, _ = result

    print(f"Employee: {value}")
    print(f"Matched: {match} ({score:.1f})")

    if score >= 85:
        return match, "AUTO"

    elif score >= 50:
        return match, "CONFIRM"

    return None, "UNKNOWN"
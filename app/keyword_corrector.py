from rapidfuzz import process, fuzz

HR_KEYWORDS = [
    "leave",
    "salary",
    "department",
    "attendance",
    "employee",
    "employees",
    "policy",
    "reimbursement",
    "balance",
    "manager",
    "designation",
    "holiday",
    "holidays",
    "working",
    "work",
]

import re

def find_keyword_match(
    word: str,
    cutoff: int = 85
) -> str | None:

    result = process.extractOne(
        word.lower(),
        HR_KEYWORDS,
        scorer=fuzz.WRatio
    )

    if result is None:
        return None

    match, score, _ = result

    if score >= cutoff:
        return match

    return None

def correct_keywords(question: str) -> str:

    words = re.findall(r"\w+|\W+", question)

    corrected = []

    for token in words:

        if not token.isalpha():
            corrected.append(token)
            continue

        match = find_keyword_match(token)

        if match:

            print(f"Keyword: {token} -> {match}")

            corrected.append(match)

        else:

            corrected.append(token)

    return "".join(corrected)
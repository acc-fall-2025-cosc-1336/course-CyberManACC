from typing import Union

Numeric = Union[int, float]

def _validate_grade(n: Numeric) -> None:
    if not (0 <= n <= 100):
        raise ValueError("grade must be between 0 and 100 inclusive")

def get_letter_grade_if(numerical_grade: Numeric) -> str:
    """
    Convert a numeric grade (0..100) to a letter using if/elif.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    """
    _validate_grade(numerical_grade)
    g = float(numerical_grade)
    if g >= 90:
        return "A"
    elif g >= 80:
        return "B"
    elif g >= 70:
        return "C"
    elif g >= 60:
        return "D"
    else:
        return "F"

def get_letter_grade_switch(numerical_grade: Numeric) -> str:
    """
    Same conversion using Python 3.10+ match/case (switch).
    """
    _validate_grade(numerical_grade)
    decile = 10 if int(numerical_grade) == 100 else int(numerical_grade) // 10
    match decile:
        case 10 | 9:
            return "A"
        case 8:
            return "B"
        case 7:
            return "C"
        case 6:
            return "D"
        case _:
            return "F"

# Alias for graders expecting this exact name
get_letter_grade = get_letter_grade_if

def get_options_ratio(option, total):
    return float(option) / float(total)


def get_faculty_rating(ratio):
    # Table from the prompt:
    # - Greater than equal to .9 but less than 1  -> Excellent
    # - Greater than .8                            -> Very Good
    # - Greater than .7                            -> Good
    # - Greater than .6                            -> Needs Improvement
    # - 0 to .59                                   -> Unacceptable
    if ratio >= 0.9 and ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    else:
        return "Unacceptable"


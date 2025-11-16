from typing import List

def get_p_distance(list1: List[str], list2: List[str]) -> float:
    """
    Proportion of differing symbols between two equal-length DNA sequences.
    """
    if len(list1) != len(list2):
        raise ValueError("Sequences must be of equal length.")
    if not list1:  # avoid ZeroDivisionError if empty lists are passed
        return 0.0
    mismatches = sum(1 for a, b in zip(list1, list2) if a != b)
    return mismatches / len(list1)


def get_p_distance_matrix(lists: List[List[str]]) -> List[List[float]]:
    """
    Build the p-distance matrix for a list of DNA sequences (all equal length).
    """
    n = len(lists)
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0.0
            else:
                matrix[i][j] = get_p_distance(lists[i], lists[j])
    return matrix

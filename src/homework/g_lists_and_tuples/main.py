import os, sys
if __package__ in (None, ""):
    _here = os.path.abspath(os.path.dirname(__file__))
    _root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
    if _root not in sys.path:
        sys.path.insert(0, _root)

from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

def read_sequences() -> list[list[str]]:
    print("Enter DNA strings (one per line). Press ENTER on an empty line to finish.")
    seqs: list[list[str]] = []
    while True:
        s = input().strip().upper()
        if not s:
            break
        seqs.append(list(s))
    if not seqs:
        return []

    # validate equal length
    L = len(seqs[0])
    if any(len(x) != L for x in seqs):
        raise ValueError("All sequences must be the same length.")
    return seqs

def print_matrix(mat: list[list[float]]) -> None:
    for row in mat:
        print(" ".join(f"{x:.5f}" for x in row))

def main() -> None:
    while True:
        print("\n1-Get p distance matrix")
        print("2-Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            seqs = read_sequences()
            if not seqs:
                print("No sequences provided.")
                continue
            matrix = get_p_distance_matrix(seqs)
            print("\nResult:")
            print_matrix(matrix)
        elif choice == "2":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

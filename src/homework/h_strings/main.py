import os
import sys

if __package__ is None or __package__ == "":
    _here = os.path.abspath(os.path.dirname(__file__))
    _root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
    if _root not in sys.path:
        sys.path.insert(0, _root)

from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement


def menu():
    print("\n1-Hamming Distance")
    print("2-Dna Complement")
    print("3-Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            s = input("Enter DNA string s: ").strip().upper()
            t = input("Enter DNA string t (same length as s): ").strip().upper()
            try:
                print(f"Hamming distance: {get_hamming_distance(s, t)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            s = input("Enter DNA string: ").strip().upper()
            try:
                print(f"DNA reverse complement: {get_dna_complement(s)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()

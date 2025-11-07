import os, sys
if __package__ is None or __package__ == "":
    _here = os.path.abspath(os.path.dirname(__file__))
    _root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
    if _root not in sys.path:
        sys.path.insert(0, _root)

from src.homework.g_lists_and_tuples.lists import (
    get_lowest_list_value,
    get_highest_list_value,
)

def menu():
    print("\n1-Show the list low/high values")
    print("2-Exit")

def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid number. Please enter an integer.")

def collect_values():
    values = []
    # Always collect at least 3 values
    while len(values) < 3:
        values.append(read_int("Enter a list value: "))

    # After at least 3 values, ask whether to continue
    while True:
        choice = input("Do you want to enter another value? (y/n): ").strip().lower()
        if choice == "y":
            values.append(read_int("Enter a list value: "))
        elif choice == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")
    return values

def main():
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            values = collect_values()
            try:
                low = get_lowest_list_value(values)
                high = get_highest_list_value(values)
                print(f"Lowest value: {low}")
                print(f"Highest value: {high}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()

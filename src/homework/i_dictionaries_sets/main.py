# Allow running this file directly: python src/homework/i_dictionaries_sets/main.py
import os, sys
if __package__ in (None, ""):
    _here = os.path.abspath(os.path.dirname(__file__))
    _root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
    if _root not in sys.path:
        sys.path.insert(0, _root)

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

def menu():
    print("\nInventory Menu")
    print("1-Add or Update Item")
    print("2-Delete Item")
    print("3-Exit")

def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter an integer.")

def print_inventory(inv: dict):
    if not inv:
        print("(inventory is empty)")
        return
    print("Current inventory:")
    for k in inv:
        print(f"  {k}: {inv[k]}")

def main():
    inventory = {}
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Enter widget name: ").strip()
            qty = read_int("Enter quantity to add (negative allowed to decrease): ")
            add_inventory(inventory, name, qty)
            print("Item added/updated.")
            print_inventory(inventory)
        elif choice == "2":
            name = input("Enter widget name to delete: ").strip()
            msg = remove_inventory_widget(inventory, name)
            print(msg)
            print_inventory(inventory)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()

from src.homework.c_decisions.decisions import (
    get_letter_grade_if,
    get_letter_grade_switch,
)

def main():
    print("MAIN MENU")
    print("1-Letter grade using if")
    print("2-Letter grade using switch")
    print("3-Exit")

    choice = input("Select option: ").strip()

    if choice in {"1", "2"}:
        try:
            raw = input("Enter a numerical grade (0-100): ").strip()
            grade = float(raw)
            if not (0 <= grade <= 100):
                print("Number is out of range.")
                return
            if choice == "1":
                print(get_letter_grade_if(grade))
            else:
                print(get_letter_grade_switch(grade))
        except ValueError:
            print("Invalid number.")
    else:
        return

if __name__ == "__main__":
    main()

from repetition import get_factorial, sum_odd_numbers


def _prompt_int(message: str) -> int:
    while True:
        s = input(message).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a whole number.")


def main() -> None:
    while True:
        print("\nHomework 4 Menu:")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit\n")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            # number > 0 and < 10
            n = _prompt_int("Enter a number (1-9): ")
            while not (1 <= n <= 9):
                print("Number must be greater than 0 and less than 10.")
                n = _prompt_int("Enter a number (1-9): ")
            print(get_factorial(n))

        elif choice == "2":
            # number > 0 and < 100
            n = _prompt_int("Enter a number (1-99): ")
            while not (1 <= n <= 99):
                print("Number must be greater than 0 and less than 100.")
                n = _prompt_int("Enter a number (1-99): ")
            print(sum_odd_numbers(n))

        elif choice == "3":
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

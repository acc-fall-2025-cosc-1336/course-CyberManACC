from void_func import display_payroll_check 
def main() -> None:
    hours_str = input("Enter hours: ").strip()
    rate_str = input("Enter rate: ").strip()

    hours = float(hours_str)
    rate = float(rate_str)

    display_payroll_check(hours, rate)

if __name__ == "__main__":
    main()

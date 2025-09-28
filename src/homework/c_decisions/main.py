from decisions import get_options_ratio, get_faculty_rating  # local import

def main() -> None:
    option_str = input("Enter options (number): ").strip()
    total_str = input("Enter total (number): ").strip()

    # Convert keyboard input
    option_f = float(option_str)
    total_f = float(total_str)

    # Float division (ratio used for rating)
    ratio = get_options_ratio(option_f, total_f)

    # Integer division (floor)
    option_i = int(option_f)
    total_i = int(total_f)
    int_div = option_i // total_i  # assumes total_i > 0

    # Show BOTH results, then the rating
    print(f"Float ratio (option/total): {ratio}")
    print(f"Integer division (option//total): {int_div}")

    rating = get_faculty_rating(ratio)
    print(rating)

if __name__ == "__main__":
    main()

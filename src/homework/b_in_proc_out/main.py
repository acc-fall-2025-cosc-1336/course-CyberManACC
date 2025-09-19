from output import multiply_numbers

def main():
    x1, y1 = 7, 7
    x2, y2 = 5, 5
    result1 = multiply_numbers(x1, y1)
    result2 = multiply_numbers(x2, y2)
    print(f"{x1} * {y1} = {result1}")
    print(f"{x2} * {y2} = {result2}")

if __name__ == "__main__":
    main()

from output import multiply_numbers, get_sales_tax_amount, get_tip_amount

def main():
    meal_str = input("Enter the meal amount (e.g., 20.00): ").strip()
    tip_str = input("Enter tip rate as a DECIMAL (e.g., 0.15 for 15%): ").strip()
    meal_amount = float(meal_str)
    tip_rate = float(tip_str)
    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount
    print(f"\nMeal Amount:   {meal_amount:10.2f}")
    print(f"Sales Tax:     {sales_tax:10.2f}")
    print(f"Tip Amount:    {tip_amount:10.2f}")
    print(f"Total:         {total:10.2f}")

if __name__ == "__main__":
    main()
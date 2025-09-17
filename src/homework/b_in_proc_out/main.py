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
from devprocess import echo_value
# Example usage of echo_value function
def main():
    echoed_value = echo_value("Hello, world!")
    print(echoed_value)  # Output: Hello, world!

    echoed_value = echo_value(42)
    print(echoed_value)  # Output: 42

if __name__ == "__main__":
    main()
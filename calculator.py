
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("\n=== PROFESSIONAL PYTHON CALCULATOR ===")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        operations = {
            "1": ("+", add),
            "2": ("-", subtract),
            "3": ("*", multiply),
            "4": ("/", divide),
        }

        if choice not in operations:
            print("Invalid choice. Please select 1-5.")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            symbol, operation = operations[choice]
            result = operation(a, b)

            print(f"\nResult: {a:g} {symbol} {b:g} = {result:g}")

        except ValueError as error:
            print(f"Input error: {error}")

        except OverflowError:
            print("Error: The numbers are too large.")

if __name__ == "__main__":
    main()

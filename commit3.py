# commit3.py
# Simple Python program for Git commit 3

def greet_user(name):
    return f"Hello, {name}! Welcome back."

def add_numbers(a, b):
    return a + b

def main():
    print("=== Commit 3 Program ===")

    # Greeting
    name = input("Enter your name: ")
    print(greet_user(name))

    # Addition feature (new in commit 3)
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add_numbers(num1, num2)
        print(f"Sum = {result}")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()

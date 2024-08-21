# Simple Arithmetic Calculator

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user choice
choice = input("Enter your choice (1/2/3/4): ")

# Get numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the chosen operation
if choice == '1':
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is: {result}")

elif choice == '2':
    result = subtract(num1, num2)
    print(f"The result of {num1} - {num2} is: {result}")

elif choice == '3':
    result = multiply(num1, num2)
    print(f"The result of {num1} * {num2} is: {result}")

elif choice == '4':
    result = divide(num1, num1)
    print(f"The result of {num1} / {num2} is: {result}")
else:
    print("Invalid choice! Please select a valid operation.")
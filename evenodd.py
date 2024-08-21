
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Welcome to the Even or Odd Checker!")
num = int(input("Enter a number to check if it is even or odd: "))

result = check_even_odd(num)
print(f"The number {num} is {result}.")
#find the  division of given num 

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    div = a / b
    return div

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

div = divide(num1, num2)
print(div)



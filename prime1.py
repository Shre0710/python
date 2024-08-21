

def is_prime(number):
    
    if number <= 1:
        return False 
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  
    return True  


print("Welcome to the Prime Number Checker!")
num = int(input("Enter a number to check if it is prime: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

print("Enter 5 numbers (type 'exit' to stop):")
for _ in range(5):
    user_input = input("Enter a number: ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break  
    
    try:
        number = int(user_input)
        if number % 2 == 0:
            continue  
        print(f"Odd number: {number}")
    except ValueError:
        print("Please enter a valid number.")
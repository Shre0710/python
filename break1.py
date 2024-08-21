
print("Enter numbers (type 'exit' to stop):")
while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break  
    
    try:
        number = int(user_input)
        if number > 10:
            print(f"First number greater than 10 is: {number}")
            break  
    except ValueError:
        print("Please enter a valid number.")
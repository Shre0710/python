
print("Enter numbers (type 'done' when finished):")
while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'done':
        print("Finished collecting numbers.")
        break  
    
    if user_input == "skip":
        pass 
    else:
        print(f"You entered: {user_input}")
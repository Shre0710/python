
user_input = input("Enter fruits separated by commas: ")


fruit_set = set(user_input.split(','))

# Display the original set
print("\n--- Original Fruit Set ---")
print(fruit_set)


print("Number of unique fruits:", len(fruit_set))
print("\n")


fruit_set.add("banana")
print("After adding 'banana':", fruit_set)


fruit_set.discard("apple")  
print("After discarding 'apple' (if it exists):", fruit_set)



if fruit_set:
    popped_fruit = fruit_set.pop()  # removes and returns an arbitrary fruit
    print("Popped Fruit:", popped_fruit)
    print("Fruit set after popping a fruit:", fruit_set)
else:
    print("Fruit set is empty, nothing to pop.")

# 6. Union with another set of fruits
another_fruit_set = {"kiwi", "mango", "orange"}
union_fruit_set = fruit_set.union(another_fruit_set)
print("Union with {'kiwi', 'mango', 'orange'}:", union_fruit_set)

# 7. Intersection with another set of fruits
intersection_fruit_set = fruit_set.intersection({"banana", "kiwi", "apple"})
print("Intersection with {'banana', 'kiwi', 'apple'}:", intersection_fruit_set)



# 12. Clear the set
fruit_set.clear()
print("Fruit set after clearing:", fruit_set)

# 13. Copy the original fruit set
original_fruit_set = {"apple", "orange", "banana", "grape"}
copied_fruit_set = original_fruit_set.copy()
print("Copied Fruit Set:", copied_fruit_set)
#string 

name = input("Enter your name: ")
sentence = input("Enter a sentence: ")
word_to_search = input("Enter a word to search in the sentence: ")

# Display user inputs
print("\n--- User Inputs ---")
print("Name:", name)
print("Sentence:", sentence)
print("Word to Search:", word_to_search)

# String methods 
print("\n--- String Methods on Name ---")
print("Uppercase Name:", name.upper())
print("Lowercase Name:", name.lower())
print("Capitalized Name:", name.capitalize())

# String methods for sentence
print("\n--- String Methods on Sentence ---")
print("Length of Sentence:", len(sentence))
print("Sentence in Title Case:", sentence.title())
print("Replaced 'a' with 'o':", sentence.replace('a', 'o'))
print("Words in Sentence:", sentence.split())
print("Join words with '-':", '-'.join(sentence.split()))

# Search for the word in the sentence
if word_to_search in sentence:
    print(f"\nThe word '{word_to_search}' is found in the sentence.")
    print("Count of the word:", sentence.count(word_to_search))
else:
    print(f"\nThe word '{word_to_search}' is not found in the sentence.")
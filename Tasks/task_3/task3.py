# Write a program to take a string input from the user and display it in uppercase.
# Step 1: Take input from the user
# Step 2: Convert the string to uppercase
# Step 3: Print the uppercase string
Name = input("Enter your name: ")
print("Your name in uppercase is:", Name.upper())



# Given the string "python", print its first and last characters.
# Step 1: Define the string
# Step 2: Access the first and last characters
Word = "python"
print("First character:", Word[0])
print("Last character:", Word[-1])



# Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
# Step 1: Take input from the user
# Step 2: Print the greeting message
Name = input("Enter your name: ")
print("Hello,", Name + "!")


# Write a program to count the number of characters in a string without using len().
# Step 1: Take the string input
# Step 2: Print number of characters
Characters = "Gbadamosi Divine"
print(Characters, "has", Characters.index("e"), "words")


# Given "Hello World", replace "World" with "Python".
# Step 1: Define the text
# Step 2: Replace "World" with "Python"
Text = "Hello World"
print(Text.replace("World", "Python"))


# Check if a given string contains the substring "python" (case-insensitive).
# Step 1: CREATE a string input from the user
# Step 2: Check for the substring "python"
Text = input("Enter a word: ")
print("Contains 'python':", "python" in Text.lower())


# Write a program to reverse a string without using slicing ([::-1]).
# Step 1: Take input from the user
# Step 2: Reverse the string 
# Step 3: Print the reversed string
word = "Gbadamosi Divine"
Reversed = "".join(reversed(word))
print(Reversed)


# Given a string with extra spaces, remove the leading and trailing spaces.
# Step 1: Define the string with extra spaces
# Step 2: Remove leading and trailing spaces
Text = "   The College of Animal Health and Management   "
print(Text.strip())


# Ask the user to enter a sentence and print the number of vowels in it.
# Step 1: Take input from the user
# Step 2: Count the vowels
word = input("Enter a sentence: ")
sentence = word.lower()
print("You have", sentence.count("a") + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u'), "vowels in the sentence." )


# Given "apple,banana,orange", split the string into a list of fruits.
# Step 1: Define the string
# Step 2: Split the string into a list
fruits = "apple,banana,orange"
print("List of fruits:", fruits.split(","))


# Ask the user for a sentence and print each word on a new line.
# Step 1: Take input from the user
# Step 2: Split the sentence into words
# Step 3: Print each word on a new line
sentence = input("Enter a sentence: ")
words = "\n".join(sentence.split())
print("Words in the sentence:\n", words)


# Replace all spaces in a string with underscores (_).
# Step 1: Take input from users
# Step 2: Replace spaces with underscores
text = input("Enter a string with spaces: ")
print("String with underscores:", text.replace(" ", "_"))   

# Count how many times the letter "a" appears in "Banana".
# Step 1: Define the string
# Step 2: Count occurrences of "a"
fruit = "Banana"
print("The letter 'a' appears", fruit.lower().count("a"), "times in 'Banana'.")


#  Check if a given string starts with "https://".
# Step 1: Take input from the user
# Step 2: Check if it starts with "https://"
url = input("Enter a URL: ")    
print("Starts with 'https://':", url.startswith("https://"))
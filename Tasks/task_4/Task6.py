# Word Analyzer
# Step 1: Ask user to input a word
# Step 2: Print length of the word
# Step 3: Check if it is uppercase, lowercase or titlecase
# Step 4: Reverse the word using slicing
# Step 5: Print result

word = input("Enter a word: ")
print(len(word))
if word.isupper():
    print("The word is uppercase.")
elif word.islower():
    print("The word is lowercase.")
elif word.istitle():
    print("The word is titlecase.")
else:
    print("The word is not in uniform case.")

reversed_word = word[::-1]
print("Reversed word: ", reversed_word)
# Word counter
# Step 1: Take a sentence from the user
# Step 2: Split the sentence into words
# Step 3: Count the number of words
# Step 4: Print the word count
sentence = input("Enter a sentence: ")
words = sentence.split()
Word_count = len(words)
print(f"The number of words in the sentence is: {Word_count}")
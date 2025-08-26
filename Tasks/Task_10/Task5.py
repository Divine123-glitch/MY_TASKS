# Word Analyzer
# Step 1: Ask user to input a word
# Step 2: Print length of the word
# Step 3: Check if it is uppercase, lowercase, or titlecase
# Step 4: Reverse the word using slicing
# Step 5: Print result

try:
    word = input("Enter a word: ").strip()
    if not word:
        raise ValueError("Word cannot be empty or just whitespace")

    # Print length of the word
    print(f"Length of word: {len(word)}")

    # Check case of the word
    if word.isupper():
        print("The word is uppercase.")
    elif word.islower():
        print("The word is lowercase.")
    elif word.istitle():
        print("The word is titlecase.")
    elif not any(c.isalpha() for c in word):
        print("The word contains no alphabetic characters.")
    else:
        print("The word is in mixed case.")

    # Reverse the word using slicing
    reversed_word = word[::-1]
    print(f"Reversed word: {reversed_word}")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)
# # Single quotes
# name = 'Ada'

# # Double quotes
# greeting = "Hello"

# # Triple quotes (for multi-line strings)
# story = '''Once upon a time,
# there was a coder named Ada.'''

# # String with numbers and symbols
# password = "p@ssw0rd123"

# # Indexing strings
# word = "Python"
# print(word[0])  # P
# print(word[-1]) # n

# # Slicing stringsword = "Python"
# word = "Once upon a time,there was a coder named Ada."
# print(word[0:15])   # Pyth
# print(word[10:])    # thon
# print(word[:20])    # Pyt
# print(word[::5])   # Pto
# print(word[::-1])

# # Concatenation
# a = "Hello"
# b = "World"
# print(a + " " + b)  # Hello World

# # Repetition
# word = "I love Rebecca"
# print(word * 3)  # I love Rebecca I love Rebecca I love Rebecca

# # Membership
# text = "Yesterday the Reds of Merseyside were disgraced by the Eagles of South London"
# print("Merseyside" in text)   # True
# print("Lond" not in text) # True

# # `find() / rfind()`
# text = "Hello World"
# print(text.find("o"))   # 4
# print(text.rfind("o"))  # 7

# # **`index() / rindex()`**
# #  (Like find() but raises an error if not found)
# text = "Hello World"
# print(text.index("Hello World"))   # 6

# **`startswith() / endswith()`**
filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))    # True
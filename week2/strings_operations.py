# Upper()
name = "Ada Balogun"
print(name.upper())

# Title()
sentence = "python is amazing"
print(sentence.title())

# Lower()
sentence = "PYTHON IS AMAZING"
print(sentence.lower())

# Strip()
text = "   Abuja   "
print(text.strip())  # Removes leading and trailing spaces

# Replace ()
message = "I love Java"
print(message.replace("Java", "Python"))

# Swapcase
text = "Hello ABEOKUTA"
print(text.swapcase())

# lstrip
text = "    Nigeria"
print(text.lstrip())

# rstrip
text = "Nigeria     "
print (text.rstrip())

# split()
fruits = "mango orange banana"
print(fruits.split())

# Split with a specific separator
fruits = "mango, orange, banana"
print(fruits.split(", "))

# Rsplit()
text = "one, two, three, four"
print(text.rsplit(", "))

# Rsplit with a specific separator
text = "one, two, three, four"
print(text.rsplit(", ", 2))  # Splits from the right, limiting to 2 splits

# Lsplit()
text = "one, two, three, four"
print(text.split(", "))

# Lsplit() with a specific separator
text = "one, two, three, four"
print(text.split(", ", 2))  # Splits from the left, limiting to 2 splits

# Splitlines()
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

# Splitlines with keepends
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines(keepends=True))

# Join()
words = ["Python", "is", "fun"]
print(" ".join(words))  # Joins with a space
print(", ".join(words))  # Joins with a comma and space

# Center()
text = "Python"
print(text.center(20))  # Centers the text in a field of width 20

# Ljust()
text = "Python"
print(text.ljust(20))  # Left-justifies the text in a field of width 20

# Rjust()
text = "Python"
print(text.rjust(20))  # Right-justifies the text in a field of width 20

# Count()
text = "banana"
print(text.count("a"))  # Counts occurrences of 'a'

# Find()
text = "Hello, world!"  
print(text.find("world"))  # Returns the index of the first occurrence of 'world'
print(text.find("Python"))  # Returns -1 if not found

# Zfill()
text = "42"
print(text.zfill(5))  # Pads the string with zeros to make it 5 characters long

# Startswith()
text = "Hello, world!"  
print(text.startswith("Hello"))  # Returns True
print(text.startswith("world"))  # Returns False

# Endswith()
text = "Hello, world!"  
print(text.endswith("world!"))  # Returns True
print(text.endswith("Hello"))  # Returns False

# Isalpha()
text = "HelloWorld"
print(text.isalpha())  # Returns True, all characters are alphabetic
text = "Hello World 123"
print(text.isalpha())  # Returns False, contains spaces and digits

# Isdigit()
text = "12345"
print(text.isdigit())  # Returns True, all characters are digits
text = "12345abc"
print(text.isdigit())  # Returns False, contains alphabetic characters

# Isalnum()
text = "Hello123"   
print(text.isalnum())  # Returns True, contains only alphanumeric characters
text = "Hello 123"
print(text.isalnum())  # Returns False, contains a space

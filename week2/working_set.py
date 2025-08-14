# Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

# Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

# Creating an empty set (must use set(), not{})
empty_set = set()
print(empty_set)

# from a string (duplicates re,oved automatically)
letters = set("mississippi")
print(letters)

# Adding element
colors = {"red", "blue"}
colors.add("green")
print(colors)

# Removing Elements
colors.remove("blue")
colors.discard("green")
print(colors)

# Pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining", colors)

# clear set
colors.clear()
print(colors)

# Mathematical operation
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)
print(set1.union(set2))

# Intersection
print(set1 & set2)
print(set1.intersection(set2))

# Difference
print(set1 - set2)
print(set1.difference(set2))

# Symmetric Difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Working with set

# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # Duplicate, ignored automatically
print("Visitors:", visitors)

# Checking if a visitor attended
# (Don't worry if you can't figure this part out yet. We will discuss it properly later in the course.)
name = "Aishai"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")
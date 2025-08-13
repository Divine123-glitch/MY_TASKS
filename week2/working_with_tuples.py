# TUPLES

# Using parentheses()
fruits = ("apple", "banana", "cherry")
print(fruits)

# Without parentheses (tuple packing)
numbers = 1, 2, 3, 
print(numbers)

# Single-item tuple (must include a comma)
single_item = ("apple", )
print(single_item)
print(type(single_item))

# Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


# Ordered
colors = ("red", "green", "blue")
print(colors[0])

# Allow Duplicates
numbers = (1, 2, 2, 3)
print(numbers)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# Nested Tuples
nested = (("a", "b"), (1, 2))
print(nested)

# TUPLE OPERATIONS
# Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])

# Slicing
print(fruits[0:2])
print(fruits[::-1])

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result) 

# Repetition
nums = (1, 2)
print(nums * 3)

# Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits) 
print("grape" in fruits)

# Iteration
for fruit in fruits:
    print(fruit)


# UNPACKING TUPLES
# dont count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2)) 
print(numbers.index(3))  

# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)  

# List back to Tuple
t = tuple(lst)
print(t)  

# Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))   # 4
print(max(nums))   # 7
print(min(nums))   # 1
print(sum(nums))   # 15

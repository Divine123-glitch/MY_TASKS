empty_list = []
print(empty_list)


empty_list2 = list()
print(empty_list2)


#List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)


#List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)   

#List of mixed data types
mixed_list = ["Apple", 25, 5.8, True]
print(mixed_list)


# From a string (each character becomes an element)
chars = list("hello")
print(chars)


# From a tuple
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)


# From a range
my_range = range(5)
list_from_range = list(my_range)
print(list_from_range)

numbers_range = list(range(1, 11))
print(numbers_range)


# Squares of number 0-4
squares = [x**2 for x in range(10)]
print(squares)

# List of even numbers from 0 to 20
evens = [x for x in range(21) if x % 2 == 0]
print(evens)


#  List of odd numbers from 0 to 20
odds = [x for x in range(21) if x % 2 != 0]
print(odds)


# Matrix-like list 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

# Accessing elements in a nested list
print(matrix[0])  
print(matrix[1][2])


# Ordered collection
fruits = ["apple", "banana", "cherry"]
print(fruits)  
print(fruits[0])  
print(fruits[1])


# Allows duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)


# Mutable collection
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)


# Different Data Types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)

# Can be nested
nested_list = [[1, 2], ["a","b"]]
print(nested_list)
print(nested_list[0][1])

# Dynamic size
names = ["Ada"]
names.append("Chuka")
names.append("Bola")
print(names)
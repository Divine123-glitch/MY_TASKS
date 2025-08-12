# Concatenation of two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)


# Repetition of a list
nums = [1, 2]
repeated_nums = nums * 3
print (repeated_nums)


# Indexing a list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])


# Slicing a list
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])


# Membership
colors = ["red", "green", "blue"]
print("red" in colors)
print("yellow" not in colors)

# Length of a list
Items = ["pen", "book", "laptop"]
print(len(Items))


# Minimum and maximum of a list
nums = [5, 2, 9, 1]
print(min(nums))
print(max(nums))


# Sorting a list
unsorted_list = [3, 1, 4, 2]    
print(sorted(unsorted_list))


# Summing element of a list
numbers = [1, 2, 3, 4]
print(sum(numbers))

# Reversing a list
reversed_list = numbers[::-1]
print(reversed_list)


# Finding the index of an element in a list
elements = ["apple", "banana", "cherry"]
print(elements.index("banana"))  # Output: 1

# Counting occurrences of an element in a list
count_list = [1, 2, 2, 3, 4, 2]
print(count_list.count(2))  # Output: 3

# Appending an element to a list
my_list = [1, 2, 3] 
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4

# Inserting an element at a specific position
my_list.insert(1, 5)  # Insert 5 at index 1
print(my_list)  

# Copying a list
a = [1, 2, 3]
b = a.copy()
print(b)
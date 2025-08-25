# Modularizing Your Code 1

# Example of Built-in Functions
for i in range(3):
    print(i)  # Outputs: 0, 1, 2

names = ["Esther", "Precious", "Kennie"]
scores = [85, 90, 75]
for n, s in zip(names, scores):
    print(n, "scored", s)  # Outputs: Esther scored 85, Precious scored 90, Kennie scored 75

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Outputs: [1, 4, 9, 16]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Outputs: [2, 4]

# Basic Function Example
def greet():
    print("Hello, welcome to AI Fellowship!")

# Calling the function multiple times
greet()
greet()
greet()

# Function with Arguments
def greet(name):
    print("Hello", name, "welcome to Python learning!")

greet("Class rep")
greet("Ridwan")

# Using print() vs return
def greet_print(name):
    print("Hello", name)

result = greet_print("Esther")
print("Result:", result)  # Outputs: None, because print() doesn't return a value

def add(a, b):
    return a + b

result = add(4, 6)
print("The sum is:", result)  # Outputs: The sum is: 10

# Using yield (Generators)
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number)  # Outputs: 1, 2, 3, 4, 5

# Types of Function Arguments
# 1. Positional Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

introduce("Ngozi", "AI Engineering")  # Correct order
# introduce("AI Engineering", "Ngozi")  # Incorrect order, causes semantic error

# 2. Keyword Arguments
introduce(name="Ngozi", track="AI Engineering")
introduce(track="AI Engineering", name="Ngozi")  # Order doesn't matter

# 3. Default Arguments
def introduce_default(name, track="AI Engineering"):
    print("My name is", name)
    print("I am learning", track, ".")

introduce_default("Paul")
introduce_default("Tunji Paul", track="AI Development")

# 4. Variable-Length Arguments
# a. Non-keyword (*args)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# b. Keyword (**kwargs)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Peter", track="AI Engineering", interest="Block Chain")

# Full Example with All Argument Types
def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
    return profile

# Testing participant_profile
print(participant_profile("Peter", 24))
print(participant_profile("Ridwan", 29, track="AI Engineering"))
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))

# Namespaces and Scope
# Namespace: A container that holds names (variables, functions, objects) and maps them to data in memory.
# Types: Built-in, Global, Local

# Example of Namespaces
employee = "General Employee"  # Global Namespace

def IT_department():
    employee = "Chris (IT)"  # Local Namespace
    print("Inside IT Department:", employee)

def Training_department():
    employee = "Chris (Training)"  # Local Namespace
    print("Inside Training Department:", employee)

print("In Global Namespace:", employee)
IT_department()
Training_department()
print("Length of 'Python':", len("Python"))  # Built-in Namespace

# Scope and LEGB Rule (Local, Enclosing, Global, Built-in)
x = "global x"  # Global Namespace

def outer():
    x = "enclosing x"  # Enclosing Namespace
    def inner():
        x = "local x"  # Local Namespace
        print("Inside inner:", x)
    inner()
    print("Inside outer:", x)

outer()
print("In global:", x)

# Global Keyword
x = 5

def change_global():
    global x
    x = 10

change_global()
print(x)  # Outputs: 10

# Nonlocal Keyword
def outer():
    x = "outer x"
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)
    inner()
    print("Inside outer:", x)

outer()

# Lambda Functions
# A small, anonymous function defined using the lambda keyword.
# Syntax: lambda arguments: expression

# Example: Normal vs Lambda Function
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2
print(square(5))
print(square_lambda(5))

# Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 7))  # Outputs: 10

# Lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Outputs: [1, 4, 9, 16]

# Lambda with filter()
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Outputs: [10, 20, 30]

# Lambda with sorted()
students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # Outputs: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)  # Outputs: [('Chika', 22), ('Ayo', 20), ('Bola', 18)]

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)  # Outputs: [('Ayo', 20), ('Bola', 18), ('Chika', 22)]
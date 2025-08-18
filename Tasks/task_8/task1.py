# TASK 1

# Ask user for input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check whether the numbers are equal
print(f"{num1} == {num2} : {num1 == num2}")

# Check whether they are not equal
print(f"{num1} != {num2}: {num1 != num2}")

# Check whether num1 is greater than num2
print(f"{num1} > {num2} : {num1 > num2}")

# Check whether num1 is less than num2
print(f"{num1} < {num2} : {num1 < num2}")

# Application of Program
# 1. Check eligibility for promotion in school
# 2. Check eligibility for selection into a sports team
# 3. Check eligibility for admission

# Check eligibility for selection into a basketball team
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
h = height
eligibility = h >= 175
print(f"Name: {name}.")
print(f"Age: {age}.")
print(f"Height: {height}.")
print(f"Eligible: {eligibility}.")

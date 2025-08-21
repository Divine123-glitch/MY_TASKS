# Handling Errors in Python

# 1. Syntax Errors
# Syntax errors occur when the Python interpreter cannot understand your code due to incorrect grammar.

# a. IndentationError – Incorrect spacing
for i in range(3):
    print(i)   # Wrong indentation fixed
# To fix: Ensure proper indentation (e.g., 4 spaces or one tab)

# b. Missing Colon/Parenthesis Error
if 5 > 3:   # Missing colon fixed
    print("Hello")
# To fix: Add the missing colon (if 5 > 3:)

# c. Invalid Syntax – General grammar mistakes
print("Hello")   # Fixed: Added parentheses for Python 3
# To fix: Use parentheses (print("Hello"))

# To Fix Syntax Errors: Double check Python grammar, colons, parentheses, and indentation.

# 2. Runtime Errors
# Runtime errors occur during program execution and are also called exceptions.
# They can be handled with try, except, and finally blocks.

# a. ZeroDivisionError – Dividing by zero
x = 10 / 0   # This will throw error

# b. NameError – Using a variable before defining it
print(Age)   # age not defined

# c. TypeError – Wrong data type in an operation
result = "10" + 5   # str + int not allowed

# d. ValueError – Invalid value for a function
number = int("abc")   # cannot convert string to int

# e. IndexError – Accessing list index out of range
fruits = ["apple", "banana"]
print(fruits[3])   # Index out of range

# f. KeyError – Accessing a dictionary with a missing key
data = {"name": "Ada"}
print(data["age"])   # Key not found

# g. FileNotFoundError – File does not exist
f = open("missing.txt")   # File not found

# Handling Runtime Errors
# Python provides exception handling to prevent programs from crashing when unexpected errors occur.
# The keywords used are;
# try:      # block of code to test for errors.
# except:   # block of code that runs if an error occurs.
# finally:  # block of code that always runs (whether error occurs or not).

# The `try` Block

# It is used to wrap code that might raise an error.

# If no error occurs Python skips the except block.

try:
    x = 10 / 2
    print("Result:", x)
except Exception as e:
    print("An error occurred:", e)


# The `try` Block
# It is used to wrap code that might raise an error.
# If no error occurs Python skips the except block.
# This is a specific exception

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# This is a case of multiple exception

try:
    number = int("abc")   # ValueError
    result = 10 / 0       # ZeroDivisionError

except ValueError:
    print("Invalid conversion to integer.")

except ZeroDivisionError:
    print(" Cannot divide by zero.")

# The finally Block
# Always runs, whether an error occurred or not
# Useful for cleanup tasks (e.g., closing files, releasing resources).
try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file if it was opened.")

# Example: ATM Transaction
balance = 5000  # starting balance
print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)  # convert input to number
    if amount > balance:
        raise ValueError("Insufficient funds.")
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Transaction session closed.")

# 3. Semantic Errors
# Semantic errors produce logically incorrect output but do not crash the program.

# Wrong Condition in Logic
age = 18
if age > 18:   # Should be >=
    print("Eligible to vote")
else:
    print("Not eligible")
# Output: Not eligible (wrong result)

# Wrong Formula/Computation
length = 10
width = 5
area = length + width   # Should be multiplication
print("Area:", area)
# Output: 15 (expected 50)

# Wrong Variable Usage
marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]   # Wrong, should be sum
print("Total:", total)

# To fix semantic errors: Carefully review logic, test with multiple cases, use debugging or print statements.
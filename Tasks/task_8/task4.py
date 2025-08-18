# Student record

# Create an empty dictionary
student = {}

# Ask user for input
student["name"] = input("Enter your full name: ")
student["age"] = int(input("Enter your age: "))

# Add a list of scores
student["scores"] = [70, 85, 90]

# Compare Score
average_score = sum(student["scores"]) / len(student["scores"])
student["passed"] = average_score >= 50

# Check if is a teenager
student["teenager"] = 13 <= student["age"] >= 21

# Print output
print("*" * 30, "Student Record", "*" * 30)
print(f"Name: {student["name"]}")
print(f"Age: {student["age"]}")
print(f"Scores: {student["scores"]}")
print(f"Passed: {student["passed"]}")
print(f"Teenager: {student["teenager"]}")
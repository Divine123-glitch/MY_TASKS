#   Student Bio Data Storage

# Step 1: Collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary
# Step 2 Collect courses (multiple values)
# Step 3: Courses should be stored as a list.

student = {
    "name": input("Enter student name: "),
    "age": input("Enter student age: "),
    "gender": input("Enter student gender: ")
}
courses = input("Enter courses separated by commas: ")
student["courses"] = courses.split(",")
print("\n--- Student Bio-Data ---")
print(f"Name:\t {student['name']}")
print(f"Age:\t {student['age']}")
print(f"Gender:\t {student['gender']}")
print(f"Courses: {', '.join(student['courses'])}")
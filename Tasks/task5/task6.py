# Attendance Tracker


# Create a tuple to store days of the week and moths of the year
Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
Days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


# Ask the user for inputs
Student_name = input("Enter student name: ")
Gender = input("Enter student gender: ")
Course_Track = input("Enter student course track: ")
current_month = int(input("Enter current month number: "))
current_day = int(input("Enter current day number: "))


# Print Data
print("\n\tStudent Attendance Tracker")
print("-" * 50)
print("Student's Name:", Student_name)
print("Gender: ", Gender)
print("Course Track: ", Course_Track)
print("Month: ", Months[current_month - 1])
print("Day: ", Days[current_month - 1])
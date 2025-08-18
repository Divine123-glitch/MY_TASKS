# Federal Government Scholarship Eligibility
# Step 1: Ask user for various input
# Step 2: Check eligibility
# Step 3: Print formatted output

name = input("Enter your name: ").title()
age = int(input("Enter your age: ").strip())
score = int(input("Enter your test score: ").strip())
citizen = input("Enter your nationality in title case: ").strip().title()
uni = input("Enter the name of your university (must be a recognized university in Nigeria): ").title()
enrol = input("Enter your current level of education Full Time\Part Time Undergraduate: ").strip().title()
scholars = input("Enter Yes or No if you are receiving a schloarship currently: ").strip().title()
waec = input("Enter Yes or No if you have at least 5 distinctions in your WAEC: ").strip().title()

eligibility = (age > 18) and (score > 70) and (citizen == "Nigerian")  and (enrol == "Full Time Undergraduate") and (scholars == "No") and (waec == "Yes")
print("-" * 45, "Student Eligibility checker","-" * 45)
print(f"Candidate: {name}\n\t\tAge: {age}\n\t\tScore: {score}\n\t\tUniversity: {uni}\n\t\tEnrollment In University: {enrol}\n\t\tEnrollment in Scholarship: {scholars}\n\t\tWAEC 5 Distinctions: {waec}\n\t\tEligible: {eligibility}")
print("-" * 45, "Student Eligibility checker","-" * 45)
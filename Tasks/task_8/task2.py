# Federal Government Scholarship Eligibility
# Step 1: Ask user for various input
# Step 2: Check eligibility
# Step 3: Print formatted output

name = input("Enter your name: ").title()
age = int(input("Enter your age: ").strip())
score = int(input("Enter your test score: ").strip())
citizen = input("Enter your nationality in title case: ").strip().title()
uni = input("Enter the name of your university (must be a recognized university in Nigeria): ").title()
enrol = input("Enter your current level of education Full Time or Part Time Undergraduate: ").strip().title()
scholars = input("Enter Yes or No if you are receiving a scholarship currently: ").strip().title()
subject = ["Maths", "English", "Biology", "Chemistry", "Physics"]

student_details = {
	"name": name,
	"age": age,
	"score": score,
	"citizen": citizen,
	"uni": uni,
	"enrol": enrol,
	"scholars": scholars,
	"subject": subject
}

Name = student_details["name"]
Age = student_details["age"]
Score = student_details["score"]
Citizen = student_details["citizen"]
Uni = student_details["uni"]
Enrol = student_details["enrol"]
Scholars = student_details["scholars"]

student_details["grade"] = {
            subject: input(f"Enter {subject} grade in WAEC or WASSCE: ").upper() for subject in student_details["subject"]
}

grade = student_details["grade"]

eligibility = (Age > 18) and (Score > 70) and (Citizen == "Nigerian") and (Uni != "") and (Enrol == "Full Time Undergraduate") and (Scholars == "No") and (grade["Maths"] == 'A' or grade["Maths"] == 'B') and (grade["English"] == 'A' or grade["English"] == 'B') and (grade["Biology"] == 'A' or grade["Biology"] == 'B') and (grade["Chemistry"] == 'A' or grade["Chemistry"] == 'B') and (grade["Physics"] == 'A' or grade["Physics"] == 'B')
print("-" * 45, "Student Eligibility checker","-" * 45)
print(f"Candidate: {Name}\nAge: {Age}\ngrade: {Score}\nUniversity: {Uni}\nEnrollment In University: {Enrol}\nEnrollment in Scholarship: {Scholars}\n\nWAEC/WASSCE Results:\n{student_details['subject'][0]}: {student_details['grade']['Maths']}\n{student_details['subject'][1]}: {student_details['grade']['English']}\n{student_details['subject'][2]}: {student_details['grade']['Biology']}\n{student_details['subject'][3]}: {student_details['grade']['Chemistry']}\n{student_details['subject'][4]}: {student_details['grade']['Physics']}\nEligible: {eligibility}")
print("-" * 45, "Student Eligibility checker","-" * 45)
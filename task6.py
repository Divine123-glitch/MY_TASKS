# UNILAG Admission Checker for a Science Student
# Step 1: Collect the needed input from users 
# Step 2: Check for eligibility
# Step 3: Print formatted output


student_input = {
    "name" : input("Enter your full name: ").title(),
    "age" : int(input("Enter your age: ")),
    "utme" : int(input("Enter your UTME score: ")),
    "subjects" : ['Maths', 'English', 'Biology', 'Chemistry', 'Physics']
}

student_input['grade'] = {
      subject: input(f"Enter {subject} grade in O'Level Result: ").strip().upper() for subject in student_input["subjects"]
}

name = student_input["name"]
age = student_input["age"]
utme = student_input["utme"]
grade = student_input["grade"]

eligibility = (age > 15) and (utme > 199) and (grade["Maths"] == 'A' or grade["Maths"] == 'B' or grade["Maths"] == 'C') and (grade["English"] == 'A' or grade["English"] == 'B' or grade["English"] == 'C') and (grade["Biology"] == 'A' or grade["Biology"] == 'B' or grade["Biology"] == 'C') and (grade["Chemistry"] == 'A' or grade["Chemistry"] == 'B' or grade["Chemistry"] == 'C') and (grade["Physics"] == 'A' or grade["Physics"] == 'B' or grade["Physics"] == 'C')
print(f"Eligibility: {eligibility}")

cut_mark = {"A":64, "B":44, "C":24}
total_score = sum(cut_mark.get(grade[subj], 0) for subj in student_input["subjects"])
admission_status = (total_score >= 200)
print("-" * 45, "Admission Checker", "-" * 45)
print(f"Candidate: {name}\nAge: {age}\nUTME Score: {utme}\nO'Level Result: ")
for subj in student_input["subjects"]:
    print(f"{subj}: {grade[subj]}")
print(f"Total Score: {total_score}")
print(f"Admission Status: {'Admitted' if admission_status else 'Not Admitted'}")
print("-" * 109)
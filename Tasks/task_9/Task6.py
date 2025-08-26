# Unique Name Collector
# Ask user number of attendees
people = set()
person = int(input("Enter number of attendees: "))

# Ask user to enter names of attendees
for i in range(person):
            t = input(f"Enter name of attendees {i + 1}: ")
            people.add(t)

# Print the name in alphabetical order
print(f"Attendees:\n {sorted(people)}")
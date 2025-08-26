# Unique Name Collector

# Initialize an empty set to store unique attendee names
people = set()

# Ask for number of attendees with exception handling
try:
    person = input("Enter number of attendees: ").strip()
    if not person:
        raise ValueError("Number of attendees cannot be empty")
    person = int(person)
    if person < 0:
        raise ValueError("Number of attendees cannot be negative")

    # Ask user to enter names of attendees
    for i in range(person):
        name = input(f"Enter name of attendee {i + 1}: ").strip().title()
        if not name:
            raise ValueError(f"Name of attendee {i + 1} cannot be empty")
        if name in people:
            print(f"{name} is already in the attendee list!")
        else:
            people.add(name)
            print(f"{name} added to the attendee list.")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Print the names in alphabetical order
print("\n--- Attendees ---")
print(f"Total unique attendees: {len(people)}")
if people:
    print("Attendee list:")
    for name in sorted(people):
        print(f"- {name}")
else:
    print("No attendees registered.")
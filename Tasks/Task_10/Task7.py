# Unique Voters Registration System

# Initialize an empty set to store unique voter names
voters = set()

# Collect up to 20 voter names with exception handling
try:
    for _ in range(20):
        name = input("Enter voter name or 'done' to end program: ").strip().title()
        if name.lower() == 'done':
            break
        if not name:
            raise ValueError("Voter name cannot be empty")
        if name in voters:
            print("This voter is already registered!")
        else:
            voters.add(name)
            print("Voter registered.")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Display results
print("\n--- Registered Voters ---")
print(f"Total unique voters: {len(voters)}")
if voters:
    print("Voter list:")
    for voter in sorted(voters):  # Sort for consistent output
        print(f"- {voter}")
else:
    print("No voters registered.")
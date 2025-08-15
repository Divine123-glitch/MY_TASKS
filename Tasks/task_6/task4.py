# Unique Voters Registration System

# Ask for voters name and store in a set
voters = set()

for _ in range(20):  
    name = input("Enter voter name or 'done' to end program: ")

    if name in voters:
        print("This voter is already registered!")
    else:
        voters.add(name)
        print("Voter registered.")

print("Total unique voters:", len(voters))

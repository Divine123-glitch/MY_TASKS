#  Contact Quick Lookup

# Store names and numbers in tuples
names = ("Pter", "James", "John", "Mary", "Alice")
numbers = ("07012345", "09167890", "08054321","09164370", "07098765")

# Create dictionary using dict(zip(...))
contacts = dict(zip(names, numbers))

# Ask user for a name
search_name = input("Enter a name to look up: ")

# Use .get() for safe retrieval
phone = contacts.get(search_name, " Name not found in contacts!")

#  Display result
print(f"Phone number: {phone}")
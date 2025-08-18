#   Unique Members Registration

# Ask user for names separated by commas
names = input("Enter three names separated by commas: ")

# Convert to a set, remove duplicates  and stores unique names
set_of_names = {name.strip() for name in names.split(",")}

# Create dictionary with names as keys and their lengths as values
members_dict = {name: len(name) for name in set_of_names}

# Display the result
print("\n--- Unique Members Dictionary ---")
print(members_dict)
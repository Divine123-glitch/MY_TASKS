# Name Organizer
# Step 1: Ask user for 5 names
# Step 2: convert to lowercase
# Step 3: sort the list
# Step 4: Print result
names = input("Enter 5 names (separeated by spaces):").split()
names = [name.lower() for name in names]
names.sort()
for i in range(len(names)):
    print(names[i])

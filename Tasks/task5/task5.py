# Modify Tuple Indirectly


# Ask the user for three items for their shooping list
List = ([
            input("Enter item 1: "),
            input("Enter item 2: "),
            input("Enter item 3: "),
])

# Convert to a list and add ask user to add two more item
Lists = list(List)
print("Add two more items.")
fr = input("Enter fourth item: ")
fv = input("Enter fifth item: ")
Lists.append(fr)
Lists.append(fv)


# Convert back to tuple
Shopping = tuple(Lists)


# Print Updated List 
print("| ".join(Shopping))
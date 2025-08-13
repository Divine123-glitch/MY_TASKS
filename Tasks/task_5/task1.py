# Creatw and Display
# Step 1: Take inpute from user
# Step 2: Convert list to tuple
# Step 3: Print tuple
# Step 4: Print each dish on a new line
dish = [
    input("Enter first dish: "),
    input("Enter second dish: "),
    input("Enter third dish: "),
    ]
dishes = tuple(dish)
print(dishes)
print("\n".join(dishes))
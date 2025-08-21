# Store Inventory Update

# Create a dictionary for store items

store = {"Book": 10, "Pen": 20, "Bag": 5}
print(f"Available store items: {store}\n")

# Ask user for inputs
items = input("Enter item to be purchased : ")
quantity = int(input(f"Enter the quantity of {items} to be purchased: "))

# Reduce quantity
store[items] -= quantity

# Print output
print(f"After purchase: {store}")


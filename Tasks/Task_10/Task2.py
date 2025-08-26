# Shopping List Manager
# Step 1: Create a list to hold shopping items
# Step 2: Ask the user to input items until they type 'done'
# Step 3: Print the final shopping list

shopping_list = []

try:
    while True:
        item = input("Enter an item for your shopping list (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        if not item:
            raise ValueError("Shopping list item cannot be empty or just whitespace")
        shopping_list.append(item.title())  # Normalize item names to title case
        print(f"{item.title()} added to the shopping list.")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Print the final shopping list
print("\n--- Your Shopping List ---")
if shopping_list:
    print("Items:")
    for item in shopping_list:
        print(f"- {item}")
else:
    print("Your shopping list is empty.")
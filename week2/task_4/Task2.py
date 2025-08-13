# Shopping List Manager
# Step 1: Create a list to hold shopping items
# Step 2: Ask the user to input items until they type 'done'    
# Step 3: Print the final shopping list
shopping_list = []
while True:
    item = input("Enter an item for your shopping list (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)
print("Your shopping list is:")
for item in shopping_list:
    print(f"- {item}")  
    

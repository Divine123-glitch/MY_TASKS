# Super Market Price List

# Items in a list
items = ["Rice", "Beans", "Milk", "Bread", "Sugar"]

# Create an empty dictionary to store price list
price_list = {}

# Ask user to enter prices for each item with exception handling
print("Enter prices for the following items:")
try:
    for item in items:
        price_input = input(f"Price of {item}: ").strip()
        if not price_input:
            raise ValueError(f"Price for {item} cannot be empty")
        price_list[item] = float(price_input)
        if price_list[item] < 0:
            raise ValueError(f"Price for {item} cannot be negative")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Display all items and their prices
print("\n--- Super Market Price List ---")
print("Item\t\tPrice")
for item in items:
    print(f"{item}\t\t{price_list[item]}")

# Allow the user to update the price of an item
try:
    item_to_update = input("Enter the item you want to update the price for: ").strip().title()
    if not item_to_update:
        raise ValueError("Item name cannot be empty")
    if item_to_update not in items:
        raise ValueError(f"{item_to_update} is not in the price list")
    new_price = input(f"Enter the new price for {item_to_update}: ").strip()
    if not new_price:
        raise ValueError(f"New price for {item_to_update} cannot be empty")
    price_list[item_to_update] = float(new_price)
    if price_list[item_to_update] < 0:
        raise ValueError(f"New price for {item_to_update} cannot be negative")
    print(f"The new price of {item_to_update} is {price_list[item_to_update]}.")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Display updated price list
print("\n--- Updated Super Market Price List ---")
print("Item\t\tPrice")
for item in items:
    print(f"{item}\t\t{price_list[item]}")
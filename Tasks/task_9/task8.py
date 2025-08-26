#   Super Market Price List

# Items should come from a list
items = ["Rice", "Beans", "Milk", "Bread", "Sugar"]

# create an empty dictionary to store price list
price_list = {}

#  Ask user to enter prices for each item
print("Enter prices for the following items:")

price = {
    items[0]: input(f"Price of {items[0]}: "),
    items[1]: input(f"Price of {items[1]}: "),
    items[2]: input(f"Price of {items[2]}: "),
    items[3]: input(f"Price of {items[3]}: "),
    items[4]: input(f"Price of {items[4]}: ")
  } 

# Display all items and their prices
print("\n--- Super Market Price List ---")
print("Item\t\tPrice")
print(f"{items[0]}\t\t{price[items[0]]}")
print(f"{items[1]}\t\t{price[items[1]]}")
print(f"{items[2]}\t\t{price[items[2]]}")
print(f"{items[3]}\t\t{price[items[3]]}")
print(f"{items[4]}\t\t{price[items[4]]}")

# allow the user to update the price of an item
item_to_update = input("Enter the item you want to update the price for: ")
if item_to_update in items:
    new_price = int(input(f"Enter the new price for {item_to_update}: "))
    price[item_to_update] = new_price
    print(f"The new price of {item_to_update} is {new_price}.")
else:
    print(f"{item_to_update} is not in the price list.")

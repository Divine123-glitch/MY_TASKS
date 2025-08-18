# Online Store Cart Calculation

# Create a list of items
items = ["Book", "Pen", "Bag", "Shoes"]
prices = [1200, 300, 7000, 10000]

# Pair item with prices
cart_items = {item: price for item, price in zip(items, prices)}

# Print Output
print("---------------Your Shopping cart---------------")
print(cart_items)

Total = sum(cart_items.values())
print(f"Amount: {Total}.")
print("------------------------------------------------")
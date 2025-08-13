# Ask user for the price of garri per paint in naira
# Step 1: Collect price in naira
# Step 2: Convert to float
# Step 3: Convert to kobo
# Step 4: Display result


price_naira = input("Enter the price of garri per paint in naira: ")

price_naira = float(price_naira)

price_kobo = int(price_naira * 100)

print(f"The price of garri is {price_naira} naira, which is {price_kobo} kobo.")
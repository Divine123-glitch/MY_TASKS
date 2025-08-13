# Daily Market Report
# Step 1: Collect market name
# Step 2: Collect number of traders
# Step 3: Calculate daily revenue
# Step 4: Print formatted result


market_name = input("Enter the market name: ")
num_traders = int(input("Enter the number of traders: "))
daily_revenue = num_traders * 100  # Assuming each trader pays ₦100 daily

print(f"\nMarket: {market_name}")
print(f"Number of Traders: {num_traders:,}")
print(f"Daily Revenue: ₦{daily_revenue:,}")
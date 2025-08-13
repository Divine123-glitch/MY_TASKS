# Electricity Bill Formatter
# Step 1: Collect customer name
# Step 2: Collect units consumed
# Step 3: Collect cost per unit
# Step 4: Calculate total bill
# Step 5: Print formatted receipt

customer_name = input("Enter customer's full name: ")
units = int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (naira): "))

total_bill = units * cost_per_unit

print("\n\t ELECTRICITY BILL RECEIPT")
print(f"Customer Name:\t{customer_name}")
print(f"Units Consumed:\t{units} kWh")
print(f"Cost per Unit:\t₦{cost_per_unit:}")
print(f"Total Bill:\t₦{total_bill:,}")
print("-------------------------------")
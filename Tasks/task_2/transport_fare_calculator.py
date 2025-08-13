# Transport Fare Calculator
# Step 1: Collect distance 
# Step 2: Collect fare per km
# Step 3: Calculate total fare
# Step 4: Print total fare

distance = float(input("Enter distance in km: "))
fare_per_km = float(input("Enter fare per km: "))

total_fare = distance * fare_per_km

print(f"\nTotal Fare: ₦{total_fare:,}\n")
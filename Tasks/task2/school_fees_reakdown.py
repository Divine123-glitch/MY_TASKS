# School Fees Breakdown
# Step 1: Collect school name
# Step 2: Collect tuition fee
# Step 3: Collect hostel fee
# Step 4: Collect feeding fee
# Step 5: Calculate total fee
# Step 6: Display formatted receipt

school_name = input("Enter the school name: ")
tuition_fee = float(input("Enter the tuition fee (naira): "))
hostel_fee = float(input("Enter the hostel fee (naira): "))
feeding_fee = float(input("Enter the feeding fee (naira): "))

total_fee = tuition_fee + hostel_fee + feeding_fee

print(f"\n\tSCHOOL FEES RECEIPT ")
print(f"School Name:\t{school_name}")
print(f"Tuition Fee:\t₦{tuition_fee:,}")
print(f"Hostel Fee:\t₦{hostel_fee:,}")
print(f"Feeding Fee:\t₦{feeding_fee:,}")
print(f"Total Fee:\t₦{total_fee:,}")
print(f"---------------------------")
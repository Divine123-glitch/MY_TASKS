# 1. Welcome screen
print("===== WELCOME TO THE DIVINE INTERACTIVE HUB =====\n")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"\nHello {name}, you are {age} years old. Let's get started!\n")

# 2. Currency conversion
print("=== Naira Currency Converter ===")
amount_naira = float(input("Enter amount in Naira: ₦"))
rate_usd = float(input("Enter exchange rate to USD: "))
rate_gbp = float(input("Enter exchange rate to GBP: "))
usd_value = amount_naira / rate_usd
gbp_value = amount_naira / rate_gbp
print(f"\n₦{amount_naira:,.2f} = ${usd_value:,.2f} USD")
print(f"₦{amount_naira:,.2f} = £{gbp_value:,.2f} GBP\n")

# 3. School fees breakdown
print("=== School Fees Breakdown ===")
school_name = input("Enter your school name: ")
tuition_fee = float(input("Enter tuition fee (naira): "))
hostel_fee = float(input("Enter hostel fee (naira): "))
feeding_fee = float(input("Enter feeding fee (naira): "))
total_fees = tuition_fee + hostel_fee + feeding_fee
print(f"\n--- SCHOOL FEES RECEIPT ---")
print(f"School:\t\t{school_name}")
print(f"Tuition Fee:\t₦{tuition_fee:,.2f}")
print(f"Hostel Fee:\t₦{hostel_fee:,.2f}")
print(f"Feeding Fee:\t₦{feeding_fee:,.2f}")
print(f"Total Fee:\t₦{total_fees:,.2f}")
print(f"----------------------------\n")

# 4. Electricity bill calculation
print("=== Electricity Bill Calculator ===")
customer_name = input("Enter your full name: ")
units = int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (naira): "))
bill_total = units * cost_per_unit
print("\n--- ELECTRICITY BILL RECEIPT ---")
print(f"Customer:\t{customer_name}")
print(f"Units:\t\t{units} kWh")
print(f"Rate:\t\t₦{cost_per_unit:.2f} per kWh")
print(f"Total Bill:\t₦{bill_total:,.2f}")
print(f"----------------------------------\n")

# 5. USSD Menu Simulation
print("=== USSD Menu Simulation ===")
ussd_code = input("Please dial your USSD code (e.g., *123#): ")
print("\nYou have dialed: " + ussd_code)
print("Please select an option:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")
choice = input("Enter option (1, 2, or 3): ")

if choice == "1":
    print(f"\nYou selected Option {choice}: Check Balance.")
    print("Your account balance is ₦2,500.00")

elif choice == "2":
    print(f"\nYou selected Option {choice}: Buy Airtime.")
    amount_airtime = float(input("Enter airtime amount: ₦"))
    print(f"You have successfully purchased ₦{amount_airtime:.2f} airtime.")

elif choice == "3":
    print(f"\nYou selected Option {choice}: Buy Data.")
    amount_data = float(input("Enter data bundle price: ₦"))
    print(f"You have successfully purchased data worth ₦{amount_data:.2f}.")

else:
    print("\nInvalid option selected.")

print("\n===== THANK YOU FOR USING THE DIVINE INTERACTIVE HUB =====")
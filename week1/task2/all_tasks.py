# # ==========================================
# # PYTHON BEGINNER TO ADVANCED PRACTICE SET
# # NIGERIAN-THEMED EXERCISES
# # Covers: input(), print(), variables, f-strings, concatenation, escape sequences,
# # data types, type casting, arithmetic, formatted output
# # ==========================================

# # --------------------------
# # Exercise 1: Collecting User Details
# # --------------------------
# """
# This program collects the user's first name and age,
# then prints a welcome message using an f-string.
# """
# first_name = input("Enter your first name: ")
# age = input("Enter your age: ")
# print(f"\\nWelcome {first_name}, you are {age} years old.\\n")

# # --------------------------
# # Exercise 2: Price Display with Type Casting
# # --------------------------
# price_naira = input("Enter the price of garri per paint in naira: ")
# price_naira = float(price_naira)
# price_kobo = int(price_naira * 100)
# print(f"\\nThe price of garri is {price_naira} naira, which is {price_kobo} kobo.\\n")

# # --------------------------
# # Exercise 3: School Registration Form
# # --------------------------
# name = input("Enter student name: ")
# student_class = input("Enter class: ")
# state = input("Enter state of origin: ")
# print("\\nStudent " + name + " is in " + student_class + " and is from " + state + ".\\n")

# # --------------------------
# # Exercise 4: Escape Sequence
# # --------------------------
# dish = input("Enter the name of a Nigerian dish: ")
# state = input("Enter the state where it is popular: ")
# print("\\nDish: " + dish + "\\n\\tState: " + state)

# # --------------------------
# # Exercise 5: Daily Market Report
# # --------------------------
# market_name = input("Enter the market name: ")
# num_traders = int(input("Enter the number of traders: "))
# daily_revenue = float(input("Enter the daily revenue in naira: "))
# print(f"\\nMarket: {market_name}")
# print(f"Number of Traders: {num_traders:,}")
# print(f"Daily Revenue: ₦{daily_revenue:,.2f}\\n")

# # --------------------------
# # Exercise 6: Electricity Bill Formatter
# # --------------------------
# customer_name = input("Enter customer's full name: ")
# units = int(input("Enter units consumed (kWh): "))
# cost_per_unit = float(input("Enter cost per unit (naira): "))
# total_bill = units * cost_per_unit
# print("\\n--- ELECTRICITY BILL RECEIPT ---")
# print(f"Customer Name:\\t{customer_name}")
# print(f"Units Consumed:\\t{units} kWh")
# print(f"Cost per Unit:\\t₦{cost_per_unit:.2f}")
# print(f"Total Bill:\\t₦{total_bill:,.2f}")
# print("-------------------------------\\n")

# # --------------------------
# # Exercise 7: Mixing Data Types
# # --------------------------
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))
# name = input("Enter your name: ")
# print(f"\\n{name} is {age} years old and {height} meters tall.\\n")

# # --------------------------
# # Exercise 8: Transport Fare Calculator
# # --------------------------
# distance = float(input("Enter distance in km: "))
# fare_per_km = float(input("Enter fare per km: "))
# total_fare = distance * fare_per_km
# print(f"\\nTotal Fare: ₦{total_fare:.2f}\\n")

# # --------------------------
# # Exercise 9: Nigerian Festival Info
# # --------------------------
# festival_name = input("Enter the festival name: ")
# location = input("Enter the location: ")
# month = input("Enter the month it is held: ")
# print("\\nThe festival \\\"" + festival_name + "\\\" is held in " + location + " every " + month + ".\\n")

# # --------------------------
# # Exercise 10: School Fees Breakdown
# # --------------------------
# school_name = input("Enter the school name: ")
# tuition_fee = float(input("Enter the tuition fee (naira): "))
# hostel_fee = float(input("Enter the hostel fee (naira): "))
# feeding_fee = float(input("Enter the feeding fee (naira): "))
# total_fee = tuition_fee + hostel_fee + feeding_fee
# print(f"\\n--- SCHOOL FEES RECEIPT ---")
# print(f"School Name:\\t{school_name}")
# print(f"Tuition Fee:\\t₦{tuition_fee:,.2f}")
# print(f"Hostel Fee:\\t₦{hostel_fee:,.2f}")
# print(f"Feeding Fee:\\t₦{feeding_fee:,.2f}")
# print(f"Total Fee:\\t₦{total_fee:,.2f}")
# print(f"---------------------------\\n")

# --------------------------
# Exercise 11: Nigerian Currency Converter
# --------------------------
amount_naira = float(input("Enter the amount in Naira: "))
rate_usd = float(input("Enter the exchange rate to US Dollars: "))
rate_gbp = float(input("Enter the exchange rate to British Pounds: "))
amount_usd = amount_naira / rate_usd
amount_gbp = amount_naira / rate_gbp
print("\\n--- NIGERIAN CURRENCY CONVERTER ---")
print(f"Amount in Naira:\\t₦{amount_naira:,.2f}")
print(f"{'Currency':<10}\\t{'Amount':>15}")
print("-" * 30)
print(f"{'USD ($)':<10}\\t${amount_usd:,.2f}")
print(f"{'GBP (£)':<10}\\t£{amount_gbp:,.2f}")
print("-" * 30 + "\\n")

# # --------------------------
# # Exercise 12: Simulated USSD Menu Interaction
# # --------------------------
# print("Welcome to Naija Mobile Services!")
# ussd_code = input("Please dial your USSD code (e.g., *123#): ")
# print("\\nYou have dialed: " + ussd_code)
# print("Please select an option:\\n1. Check Balance\\n2. Buy Airtime\\n3. Buy Data")
# choice = input("Enter option (1, 2, or 3): ")
# if choice == "1":
#     print(f"\\nYou selected Option {choice}: Check Balance.")
#     print("Your account balance is ₦2,500.00")
# elif choice == "2":
#     print(f"\\nYou selected Option {choice}: Buy Airtime.")
#     amount = float(input("Enter airtime amount: ₦"))
#     print(f"You have successfully purchased ₦{amount:.2f} airtime.")
# elif choice == "3":
#     print(f"\\nYou selected Option {choice}: Buy Data.")
#     amount = float(input("Enter data bundle price: ₦"))
#     print(f"You have successfully purchased data worth ₦{amount:.2f}.")
# else:
#     print("\\nInvalid option selected.")

# # --------------------------
# # Exercise 13: Mega Project - Naija Interactive Hub
# # --------------------------
# print("\\n===== WELCOME TO THE NAIJA INTERACTIVE HUB =====\\n")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"\\nHello {name}, you are {age} years old. Let's get started!\\n")
# # Currency conversion
# print("=== Naira Currency Converter ===")
# amount_naira = float(input("Enter amount in Naira: ₦"))
# rate_usd = float(input("Enter exchange rate to USD: "))
# rate_gbp = float(input("Enter exchange rate to GBP: "))
# usd_value = amount_naira / rate_usd
# gbp_value = amount_naira / rate_gbp
# print(f"\\n₦{amount_naira:,.2f} = ${usd_value:,.2f} USD")
# print(f"₦{amount_naira:,.2f} = £{gbp_value:,.2f} GBP\\n")
# # School fees
# print("=== School Fees Breakdown ===")
# school_name = input("Enter your school name: ")
# tuition_fee = float(input("Enter tuition fee (naira): "))
# hostel_fee = float(input("Enter hostel fee (naira): "))
# feeding_fee = float(input("Enter feeding fee (naira): "))
# total_fees = tuition_fee + hostel_fee + feeding_fee
# print(f"\\n--- SCHOOL FEES RECEIPT ---")
# print(f"School:\\t\\t{school_name}")
# print(f"Tuition Fee:\\t₦{tuition_fee:,.2f}")
# print(f"Hostel Fee:\\t₦{hostel_fee:,.2f}")
# print(f"Feeding Fee:\\t₦{feeding_fee:,.2f}")
# print(f"Total Fee:\\t₦{total_fees:,.2f}")
# print(f"----------------------------\\n")
# # Electricity bill
# print("=== Electricity Bill Calculator ===")
# customer_name = input("Enter your full name: ")
# units = int(input("Enter units consumed (kWh): "))
# cost_per_unit = float(input("Enter cost per unit (naira): "))
# bill_total = units * cost_per_unit
# print("\\n--- ELECTRICITY BILL RECEIPT ---")
# print(f"Customer:\\t{customer_name}")
# print(f"Units:\\t\\t{units} kWh")
# print(f"Rate:\\t\\t₦{cost_per_unit:.2f} per kWh")
# print(f"Total Bill:\\t₦{bill_total:,.2f}")
# print(f"----------------------------------\\n")
# # USSD Menu
# print("=== USSD Menu Simulation ===")
# ussd_code = input("Please dial your USSD code (e.g., *123#): ")
# print("\\nYou have dialed: " + ussd_code)
# print("Please select an option:\\n1. Check Balance\\n2. Buy Airtime\\n3. Buy Data")
# choice = input("Enter option (1, 2, or 3): ")
# if choice == "1":
#     print(f"\\nYou selected Option {choice}: Check Balance.")
#     print("Your account balance is ₦2,500.00")
# elif choice == "2":
#     print(f"\\nYou selected Option {choice}: Buy Airtime.")
#     amount_airtime = float(input("Enter airtime amount: ₦"))
#     print(f"You have successfully purchased ₦{amount_airtime:.2f} airtime.")
# elif choice == "3":
#     print(f"\\nYou selected Option {choice}: Buy Data.")
#     amount_data = float(input("Enter data bundle price: ₦"))
#     print(f"You have successfully purchased data worth ₦{amount_data:.2f}.")
# else:
#     print("\\nInvalid option selected.")
# print("\\n===== THANK YOU FOR USING THE NAIJA INTERACTIVE HUB =====")
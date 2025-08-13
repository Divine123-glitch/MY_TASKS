# USSD Menu Interaction
# Step 1: Welcome screen
print("Welcome to Naija Mobile Services!")

# Step 2: Ask user to dial a USSD code
ussd_code = input("Please dial your USSD code (e.g., *123#): ")

# Step 3: Print menu
print("\nYou have dialed: " + ussd_code)
print("Please select an option:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# Step 4: Ask for option
choice = input("Enter option (1, 2, or 3): ")

# Step 5: Confirmation message
if choice == "1":
    print(f"\nYou selected Option {choice}: Check Balance.")
    print("Your account balance is ₦2,500.00")

elif choice == "2":
    print(f"\nYou selected Option {choice}: Buy Airtime.")
    amount = float(input("Enter airtime amount: ₦"))
    print(f"You have successfully purchased ₦{amount:.2f} airtime.")

elif choice == "3":
    print(f"\nYou selected Option {choice}: Buy Data.")
    amount = float(input("Enter data bundle price: ₦"))
    print(f"You have successfully purchased data worth ₦{amount:.2f}.")

else:
    print("\nInvalid option selected.")
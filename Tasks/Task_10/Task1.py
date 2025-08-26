# USSD Menu Interaction
# Step 1: Welcome screen
# Step 2: Ask user to dial a USSD code
# Step 3: Print menu
# Step 4: Ask for option
# Step 5: Confirmation message

try:
    print("Welcome to Naija Mobile Services!")
    ussd_code = input("Please dial your USSD code (e.g., *123#): ").strip()
    if not ussd_code:
        raise ValueError("USSD code cannot be empty")

    print("\nYou have dialed:", ussd_code)
    print("Please select an option:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")
    
    choice = input("Enter option (1, 2, or 3): ").strip()
    if not choice:
        raise ValueError("Option cannot be empty")
    if choice not in ["1", "2", "3"]:
        raise ValueError("Invalid option selected. Please choose 1, 2, or 3")

    if choice == "1":
        print(f"\nYou selected Option {choice}: Check Balance.")
        print("Your account balance is ₦2,500.00")

    elif choice == "2":
        print(f"\nYou selected Option {choice}: Buy Airtime.")
        amount_input = input("Enter airtime amount: ₦").strip()
        if not amount_input:
            raise ValueError("Airtime amount cannot be empty")
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Airtime amount must be positive")
        print(f"You have successfully purchased ₦{amount:.2f} airtime.")

    elif choice == "3":
        print(f"\nYou selected Option {choice}: Buy Data.")
        amount_input = input("Enter data bundle price: ₦").strip()
        if not amount_input:
            raise ValueError("Data bundle price cannot be empty")
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Data bundle price must be positive")
        print(f"You have successfully purchased data worth ₦{amount:.2f}.")

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)
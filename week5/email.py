# Username Extractor

# Step 1: Define username extractor
# Step 2: Ask user for input
# Step 3: Extract username and domain
# Step 4: Print formatted output

# Define email slicer
def username_extractor(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except: ValueError
    return None, None

# Ask user for input
user_email = input("Enter your email address: ").title()
username, domain = username_extractor(user_email)

# Validate Input
if username and domain:
    print(f"\n" + "=" * 45)
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"\n" + "=" * 45)

else:
    print("The email is incorrect. Add @")
 

from pathlib import Path
from file_ops import save_contact, load_contacts, update_contact, delete_contact

def validate_name(name):
    """Return True if name is not empty, else False."""
    return bool(name.strip())

def validate_age(age_str):
    """Return (True, age) if age is a valid integer >= 0, else (False, None)."""
    try:
        age = int(age_str)
        return (age >= 0, age)
    except ValueError:
        return (False, None)

def validate_phone(phone):
    """Return True if phone number is 10-15 digits, else False."""
    return phone.isdigit() and 10 <= len(phone) <= 11

def validate_track(track):
    """Return True if track is not empty, else False."""
    return bool(track.strip())

def get_contact_details():
    """Prompt for contact details with validation, return dictionary or None."""
    while True:
        print("\nEnter contact details:")
        name = input("\tName: ").strip().title()
        if not validate_name(name):
            print("Error: Name cannot be empty. Please try again.")
            continue

        age_str = input("\tAge: ").strip()
        is_valid_age, age = validate_age(age_str)
        if not is_valid_age:
            print("Error: Age must be a number. Please try again.")
            continue

        phone = input("\tPhone (11 digits): ").strip()
        if not validate_phone(phone):
            print("Error: Phone must be 11digits and must start with 0. Please try again.")
            continue

        track = input("\tTrack: ").strip().title()
        if not validate_track(track):
            print("Error: Track cannot be empty. Please try again.")
            continue

        return {"Name": name.title(), "Age": str(age), "Phone": phone, "Track": track.title()}

def display_contacts(contacts):
    """Display all contacts with a summary count."""
    if not contacts:
        print("\nNo contacts found.")
        return
    print(f"\nSummary: {len(contacts)} contact(s) found.")
    print("\ncontacts:")
    for p in contacts:
        print(f"\tName: {p['Name']}, Age: {p['Age']}, Phone: {p['Phone']}, Track: {p['Track']}")

def search_contacts(contacts, search_name):
    """Search for contacts by name (case-insensitive partial match)."""
    search_name = search_name.lower().strip()
    matches = [p for p in contacts if search_name in p['Name'].lower()]
    if not matches:
        print(f"\nNo contacts found matching '{search_name}'.")
    else:
        print(f"\nFound {len(matches)} contact(s) matching '{search_name}':")
        for p in matches:
            print(f"\tName: {p['Name']}, Age: {p['Age']}, Phone: {p['Phone']}, Track: {p['Track']}")
    return matches

def main():
    csv_path = Path("workspace/contacts.csv")
    
    while True:
        print("\n============== Contact Saver Menu ==============")
        print("\t1. Create new contact")
        print("\t2. Update existing contact")
        print("\t3. Display all contacts")
        print("\t4. Delete a contact")
        print("\t5. Search for a contact")
        print("\t6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":  # Create
            contact = get_contact_details()
            if contact:
                try:
                    save_contact(csv_path, contact)
                    print("=" * 45)
                    print(f"\ncontact {contact['Name']} created successfully!")
                except Exception as e:
                    print(f"Error creating contact: {e}")
        
        elif choice == "2":  # Update
            name = input("\nEnter the name of the contact to update: ").strip().title()
            if not validate_name(name):
                print("Error: Name cannot be empty.")
                continue
            contacts = load_contacts(csv_path)
            if not any(p['Name'].lower() == name.lower() for p in contacts):
                print(f"No contact found with name '{name}'.")
                continue 
            print(f"\nFound contact. Enter new details for {name}:")
            updated_contact = get_contact_details()
            if update_contact(csv_path, name, updated_contact):
                print("=" * 45)
                print(f"\ncontact {name} updated successfully!")
            else:
                print(f"\nFailed to update contact {name}.")
        
        elif choice == "3":  # Display
            contacts = load_contacts(csv_path)
            display_contacts(contacts)
        
        elif choice == "4":  # Delete
            name = input("\nEnter the name of the contact to delete: ").strip()
            if not validate_name(name):
                print("Error: Name cannot be empty.")
                continue
            if delete_contact(csv_path, name):
                print(f"\ncontact {name} deleted successfully!")
            else:
                print(f"\nNo contact found with name '{name}' or error occurred.")
        
        elif choice == "5":  # Search
            search_name = input("\nEnter name to search for: ").strip()
            if not validate_name(search_name):
                print("Error: Search name cannot be empty.")
                continue
            contacts = load_contacts(csv_path)
            search_contacts(contacts, search_name)
        
        elif choice == "6":  # Exit
            print("\nExiting Contact Saver. Goodbye!")
            contacts = load_contacts(csv_path)
            display_contacts(contacts)
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
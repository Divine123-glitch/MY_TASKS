from pathlib import Path
import csv

def save_contact(path, contact_dict):
    """Append contact details to a CSV file, creating it with headers if it doesn't exist."""
    path = Path(path)
    # Create parent directory (workspace) if it doesn't exist
    path.parent.mkdir(parents=True, exist_ok=True)
    
    file_exists = path.is_file()
    
    try:
        with path.open('a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Phone', 'Track'])
            if not file_exists:
                writer.writeheader()
            writer.writerow(contact_dict)
    except IOError as e:
        print(f"Error saving contact: {e}")

def load_contacts(path):
    """Read all contacts from a CSV file and return them as a list of dictionaries."""
    path = Path(path)
    contacts = []
    
    try:
        if path.is_file():
            with path.open('r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contacts.append(row)
        return contacts
    except IOError as e:
        print(f"Error loading contacts: {e}")
        return []

def update_contact(path, name, updated_dict):
    """Update a contact's details in the CSV file by name."""
    path = Path(path)
    contacts = load_contacts(path)
    updated = False
    
    # Update the matching contact
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact.update(updated_dict)
            updated = True
    
    # Rewrite the entire CSV file with updated data
    if updated:
        try:
            with path.open('w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Phone', 'Track'])
                writer.writeheader()
                writer.writerows(contacts)
            return True
        except IOError as e:
            print(f"Error updating contact: {e}")
            return False
    return False

def delete_contact(path, name):
    """Delete a contact from the CSV file by name."""
    path = Path(path)
    contacts = load_contacts(path)
    initial_len = len(contacts)
    
    # Filter out the contact with the matching name
    contacts = [p for p in contacts if p['Name'].lower() != name.lower()]
    
    # Rewrite the CSV file if a contact was removed
    if len(contacts) < initial_len:
        try:
            with path.open('w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Phone', 'Track'])
                writer.writeheader()
                writer.writerows(contacts)
            return True
        except IOError as e:
            print(f"Error deleting contact: {e}")
            return False
    return False
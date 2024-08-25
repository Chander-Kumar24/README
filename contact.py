import json

contacts = {}

def add_contact():
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()

    if not name or not phone or not email:
        print("All fields are required.")
        return

    if name in contacts:
        print(f"Contact with the name '{name}' already exists.")
        return

    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print(f"Contact '{name}' added successfully.")

def search_contact():
    """Search for a contact by name."""
    name = input("Enter the name of the contact to search: ").strip()
    contact = contacts.get(name)

    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact():
    """Delete a contact by name."""
    name = input("Enter the name of the contact to delete: ").strip()
    
    if contacts.pop(name, None):
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def view_all_contacts():
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
        return

    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print()

def save_to_file(filename):
    """Save contacts to a file."""
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
    print(f"Contacts saved to {filename}.")

def load_from_file(filename):
    """Load contacts from a file."""
    global contacts
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
        print(f"Contacts loaded from {filename}.")
    except FileNotFoundError:
        print(f"No file found with the name {filename}.")
    except json.JSONDecodeError:
        print("Error reading the file. It might be corrupted.")

def main():
    """Main function to run the contact management system."""
    filename = 'contacts.json'

    load_from_file(filename)

    while True:
        print("\nSimple Contact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Save to File")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            view_all_contacts()
        elif choice == '5':
            save_to_file(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

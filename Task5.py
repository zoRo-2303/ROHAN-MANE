import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    contacts = load_contacts()
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Display all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("No contacts found!")
        return

    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    contacts = load_contacts()
    search = input("Enter name or phone number to search: ")
    found_contacts = [c for c in contacts if search in (c['name'], c['phone'])]

    if not found_contacts:
        print("No matching contacts found!")
        return

    print("\nSearch Results:")
    for contact in found_contacts:
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

def update_contact():
    """Update contact details."""
    contacts = load_contacts()
    search = input("Enter name or phone number of the contact to update: ")

    for contact in contacts:
        if search in (contact['name'], contact['phone']):
            print("Leave field empty to keep the current value.")
            new_name = input(f"New name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New email ({contact['email']}): ") or contact['email']
            new_address = input(f"New address ({contact['address']}): ") or contact['address']

            contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found!")

def delete_contact():
    """Delete a contact."""
    contacts = load_contacts()
    search = input("Enter name or phone number of the contact to delete: ")

    for contact in contacts:
        if search in (contact['name'], contact['phone']):
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{contact['name']}' deleted successfully!")
            return

    print("Contact not found!")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

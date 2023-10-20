# Initialize an empty contact book (dictionary)
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    
    contact_book[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("\nContact List:")
        for name, contact_info in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}\n")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter a name or phone number to search for a contact: ").lower()
    
    found_contacts = []
    for name, contact_info in contact_book.items():
        if (
            search_term in name.lower() or
            search_term in contact_info['Phone']
        ):
            found_contacts.append((name, contact_info))
    
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for name, contact_info in found_contacts:
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}\n")

# Function to update a contact's information
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    
    if name in contact_book:
        print(f"Updating contact: {name}")
        new_phone = input("Enter the new phone number (leave empty to keep the current one): ")
        new_email = input("Enter the new email address (leave empty to keep the current one): ")
        new_address = input("Enter the new address (leave empty to keep the current one): ")
        
        if new_phone:
            contact_book[name]["Phone"] = new_phone
        if new_email:
            contact_book[name]["Email"] = new_email
        if new_address:
            contact_book[name]["Address"] = new_address
        
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found in the contact book.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found in the contact book.")

# Main program loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

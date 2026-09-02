contacts = {}


def add_contact():
    name = input("Enter name: ")

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== CONTACT LIST =====")

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("Address:", details["address"])


def search_contact():
    search = input("Enter name or phone number: ").lower()

    found = False

    for name, details in contacts.items():

        if (search in name.lower() or
                search in details["phone"].lower()):

            print("\nContact Found!")
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])

            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ")

    if name not in contacts:
        print("Contact not found.")
        return

    print("\nEnter new details:")

    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email
    contacts[name]["address"] = address

    print("Contact updated successfully!")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

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
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice.")

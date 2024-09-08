class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactList:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_contact(self, contact):
        with open(self.file_name, 'a') as file:
            file.write(f"{contact.name},{contact.phone}\n")
        print("Contact added successfully.")

    def delete_contact(self, name):
        contacts = self.get_contacts()
        found = False
        with open(self.file_name, 'w') as file:
            for contact in contacts:
                if contact.name == name:
                    found = True
                else:
                    file.write(f"{contact.name},{contact.phone}\n")
        if found:
            print(f"{name} deleted from contacts.")
        else:
            print(f"{name} not found in contacts.")

    def view_contacts(self):
        contacts = self.get_contacts()
        if not contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for contact in contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def get_contacts(self):
        contacts = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    name, phone = line.strip().split(',')
                    contacts.append(Contact(name, phone))
        except FileNotFoundError:
            pass
        return contacts

def authenticate(password):
    return password == "password123"  # Change this to your desired password

def main():
    password = input("Enter password: ")
    if not authenticate(password):
        print("Incorrect password. Access denied.")
        return

    contact_list = ContactList("contacts.txt")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact = Contact(name, phone)
            contact_list.add_contact(contact)
        elif choice == '2':
            name = input("Enter name to delete: ")
            contact_list.delete_contact(name)
        elif choice == '3':
            contact_list.view_contacts()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
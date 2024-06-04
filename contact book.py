class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print("Contact added successfully.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact removed successfully.")
        else:
            print("Contact not found.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            contact_book.add_contact(name, number)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            contact_book.remove_contact(name)
        elif choice == '3':
            contact_book.display_contacts()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

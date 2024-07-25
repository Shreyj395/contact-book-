class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f'Contact {name} added successfully.')

    def view_contacts(self):
        if not self.contacts:
            print('No contacts found.')
            return
        for idx, contact in enumerate(self.contacts):
            print(f'{idx+1}. Name: {contact.name}, Phone: {contact.phone}')

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not results:
            print('No contacts found.')
            return
        for contact in results:
            print(f'Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}')

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f'Contact {name} updated successfully.')
                return
        print('Contact not found.')

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f'Contact {name} deleted successfully.')
                return
        print('Contact not found.')

def user_interface():
    contact_book = ContactBook()
    while True:
        print('\nContact Book Menu:')
        print('1. Add Contact')
        print('2. View Contact List')
        print('3. Search Contact')
        print('4. Update Contact')
        print('5. Delete Contact')
        print('6. Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone number: ')
            email = input('Enter email: ')
            address = input('Enter address: ')
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input('Enter name or phone number to search: ')
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input('Enter the name of the contact to update: ')
            new_phone = input('Enter new phone number (leave blank to keep current): ')
            new_email = input('Enter new email (leave blank to keep current): ')
            new_address = input('Enter new address (leave blank to keep current): ')
            contact_book.update_contact(name, new_phone or None, new_email or None, new_address or None)
        elif choice == '5':
            name = input('Enter the name of the contact to delete: ')
            contact_book.delete_contact(name)
        elif choice == '6':
            print('Exiting Contact Book. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    user_interface()

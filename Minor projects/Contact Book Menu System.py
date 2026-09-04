contacts = {}

def add_contacts():
    name = input("Enter contact name:")
    phone = input("Enter phone number:")
    
    contacts[name] = phone 
    
    print("Added contact Successfully!")


def search_contacts():
    name = input("Enter the name you want to Search:")
    
    if name in contacts:
        print("Name:", name)
        print("phone:", contacts[name])    
        
    else:
        print("contact not found")
        
def delete_contacts():
    name = input("Enter the name you want to delete:")
    
    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully.")
        
    else:
        print("Contact not found.")
        
def view_contacts():
    
    if len(contacts) == 0:
        print("No Contacts Available.")
        
    else:
        print("***** All Contacts *****")
        
        for name, phone in contacts.items():
            print(name, ":", phone)


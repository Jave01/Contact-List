from contacthandler import ContactHandler

cHandler = ContactHandler()

def enter_personal_data():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    mobile = input("Mobile: ")
    home = input("Home: ")
    email = input("Email: ")
    address = input("Address: ")
    return [first_name, last_name, mobile, home, email, address]

if __name__ == "__main__":
    while True:
        cmd = input("Enter command: ")

        if cmd == 'q':
            print("Quitting...")
            exit()

        elif cmd == 'add':
            cHandler.add_contact(*enter_personal_data())

        elif cmd == 'list':
            cHandler.list_contacts()
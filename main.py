from contacthandler import ContactHandler

HELP_MESSAGE = "\n\
Command arguments have to be entered after entering the command. The command itself takes no arguments\n\
\n\
Valid commands:\n\
    add         Create a new contact\n\
    list        Lists all contacts\n\
    search      Search for a contact by his name. Lists all names of contacts that contain the given input\n\
    del         Delete a contact\n\
    h, help     Prints this message\n\
    q, quit     Quits the program\n\
"

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
    print('Enter help for information of how to use this module')
    while True:
        cmd = input("> ")

        if cmd == 'q' or cmd == 'quit':
            print("Quitting...")
            exit()

        elif cmd == 'add':
            cHandler.add_contact(*enter_personal_data())

        elif cmd == 'list':
            cHandler.list_contacts()

        elif cmd == 'search':
            first_name = input("First name: ")
            last_name = input("Last name: ")
            cHandler.search_contact(first_name, last_name)

        elif cmd == 'del':
            first_name = input("First name: ")
            last_name = input("Last name: ")
            cHandler.del_contact(first_name, last_name)

        elif cmd == 'h' or cmd == 'help':
            print(HELP_MESSAGE)

        elif len(cmd) > 0:
            print("Command not valid")
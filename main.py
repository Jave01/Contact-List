from contacthandler import ContactHandler

HELP_MESSAGE = "\
Command arguments have to be given after entering the command. The command itself takes no arguments\n\
\n\
Valid commands:\n\
    add         Create a new contact\n\
    list        Lists all contacts\n\
    search      Search for a contact by his name. Lists all names of contacts that contain the given input\n\
    del         Delete a contact\n\
    print       Print detailed information from contact\n\
    h, help     Prints this message\n\
    q, quit     Quits the program\n\
"


cHandler = ContactHandler(path="ContactList/testfolder", filename="random.json")


def enter_personal_data(name=True, mobile=False, home=False, email=False, address=False, full=False):
    if name or full:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
    if mobile or full:
        mobile = input("Mobile: ")
    if home or full:
        home = input("Home: ")
    if email or full:
        email = input("Email: ")
    if address or full:
        address = input("Address: ")

    return [x for x in [first_name, last_name, mobile, home, email, address] if x != False] # only return entered values


def main():
    print('Enter help for information of how to use this module')
    while True:
        cmd = input("> ")

        if cmd == 'q' or cmd == 'quit':
            print("Quitting...")
            exit()

        elif cmd == 'add':
            data = enter_personal_data(full=True)

        elif cmd == 'list':
            if not cHandler.list_contacts():
                print("No contacts found")
            print() # new line

        elif cmd == 'search':
            data = enter_personal_data(name=True)
            if not cHandler.search_contact(*data):
                print("No contact found")

        elif cmd == 'del':
            data = enter_personal_data(name=True)
            if not cHandler.del_contact(*data):
                print("Contact doesn't exist")

        elif cmd == 'print':
            inp = enter_personal_data(name=True)
            if not cHandler.print_contact(inp["first_name"] + ' ' + inp["last_name"]):
                print("Contact doesn't exist")

        elif cmd == 'h' or cmd == 'help':
            print(HELP_MESSAGE)

        elif len(cmd) > 0:
            print("Command not valid")


if __name__ == "__main__":
    main()

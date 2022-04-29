from aifc import Error
import json
import platform
import os

class ContactHandler:
    def __init__(self, path="./", filename="contacts.json"):
        self.path = path
        self.filename = filename
        self.file = None

        if not self.filename.endswith('.json'):
            raise ValueError("File must be of type json")

        if platform.system() == "Windows":
            self.DIR_SPLIT_CHAR = '\\'
            self.ABS_PATH_INITIAL_STR = 'C:\\'
        elif platform.system() == "Linux":
            self.DIR_SPLIT_CHAR = '/'
            self.ABS_PATH_INITIAL_STR = '/home'
        else:
            raise SystemError('OS Platform not supported')

        if not self.path.startswith(self.ABS_PATH_INITIAL_STR):
            # if path is relative get path to running file and remove the filename
            path_to_file = self.DIR_SPLIT_CHAR.join(__file__.split('/')[:-1])
            # combine path to file with the given relative path to make an absolute path
            self.path = path_to_file + self.DIR_SPLIT_CHAR + self.path

        # don't know why it works that way but can't add it in the sum above
        self.path += self.DIR_SPLIT_CHAR

        self.path.replace(2 * self.DIR_SPLIT_CHAR, self.DIR_SPLIT_CHAR)

        # if the path already exists it must be a directory, otherwise the directories are created
        if os.path.exists(self.path):
            if not os.path.isdir(self.path):
                raise FileNotFoundError("Given path is not a directory")
        else:
            os.makedirs(self.path)

        self.filepath = self.path + self.filename

        # Check if file exists and create one if not
        try:
            with open(f'{self.filepath}', 'r') as f:
                pass
        except FileNotFoundError:
            with open(f'{self.filepath}', 'w+') as f:
                json.dump(dict(), f)
            
        with open(f'{self.filepath}', 'r') as f:
            self.contacts = json.load(f)

    def add_contact(self, first_name, last_name, mobile=0, home="", email="", address=""):
        if self.contacts.get(f"{first_name} {last_name}", None) != None:
            raise NameError("Contact already exists")

        self.contacts[f"{first_name} {last_name}"] = {}
        self.contacts[f"{first_name} {last_name}"]["mobile"] = mobile
        self.contacts[f"{first_name} {last_name}"]["home"] = home
        self.contacts[f"{first_name} {last_name}"]["email"] = email
        self.contacts[f"{first_name} {last_name}"]["address"] = address

        with open(self.path + "contacts.json", "w") as f:
            json.dump(self.contacts, f)

        print("Contact added")

    def del_contact(self, first_name, last_name):
        name = first_name + ' ' + last_name
        if name in self.contacts.keys():
            del self.contacts[f"{first_name} {last_name}"]
        else:
            print("That contact doesn't exist")

    def list_contacts(self):
        # convert the contact names to a list and sort it by name
        contact_names = sorted(list(self.contacts.keys()), key=lambda x: x[0])

        # Get and validate the range of contacts that get printed
        start = 0
        stop = len(contact_names)
        while True:
            print_range = input(f'Enter range, empty -> whole range, max: {len(contact_names)}: ')
            if print_range == "":
                break
            # handle if only one number is entered -> print from 0 to entered number
            try:
                start, stop = print_range.split()
                start, stop = int(start), int(stop)
            except ValueError:
                # if range is numeric only one number is entered -> valid input
                if print_range.isnumeric():
                    stop = int(range)
                    start = 0
                    break
                else:
                    print("Range invalid. Enter one number or two numbers divided by a space")
                    continue
            if start > stop:
                print("Stop value can't be bigger than the start value")
                continue
            if stop > len(contact_names) or stop < 0:
                print("Stop value to big/small")
                continue
            if start < 0:
                print("Start value to small")
                continue
            break

        for name in contact_names[start:stop]:
            self.print_contact(name)

    def print_contact(self, name: str):
        if name not in self.contacts:
            print("Contact does not exist")
            return
        print()     # new line
        contact = self.contacts[name]
        print(name)
        print('-----------------------------')
        print(f'mobile: {contact["mobile"]}')
        print(f'home: {contact["home"]}')
        print(f'email: {contact["email"]}')


    def search_contact(self, search_first_name, search_last_name):
        index = 1
        for name in self.contacts.keys():
            first_name, last_name = name.split()
            if search_first_name in first_name and search_last_name in last_name:
                print(f"{index}. {first_name} {last_name}")
                index += 1

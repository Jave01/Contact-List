import json

class ContactHandler:
    def __init__(self, path="./"):
        self.path = path
        with open(self.path + "contacts.json", "r") as f:
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
        range_valid = False
        start = 0
        stop = len(contact_names)
        while not range_valid:
            range = input(f'Enter range, empty -> whole range, max: {len(contact_names)}: ')
            if range == "":
                break
            # handle if only one number or is entered -> print from 0 to entered number
            try:
                start, stop = range.split()
                start, stop = int(start), int(stop)
            except ValueError:
                # if range is numeric only one number is entered -> valid input
                if range.isnumeric():
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

        for i, name in enumerate(contact_names[start:stop]):
            self._print_contact(name, i)

    def _print_contact(self, name: str, index=-1):
        contact = self.contacts[name]

        if index == -1:
            print(name)
        else:
            print(f'{index+1}. ' + name)
        print(f'\tmobile: {contact["mobile"]}')
        print(f'\thome: {contact["home"]}')
        print(f'\temail: {contact["email"]}')
        print(f'\tmobile: {contact["mobile"]}')

    def search_contact(self, search_first_name, search_last_name):
        index = 1
        for name in self.contacts.keys():
            first_name, last_name = name.split()
            if search_first_name in first_name and search_last_name in last_name:
                print(f"{index}. {first_name} {last_name}")
                index += 1


if __name__ == "__main__":
    c = ContactHandler()
    c.add_contact("Alan", "Joss")
    c.add_contact("Haonan", "Nüssli")
    c.add_contact("David", "Jäggli")


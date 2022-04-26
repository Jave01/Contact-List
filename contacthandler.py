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


    def del_contact(self, first_name, last_name):
        del self.contacts[f"{first_name} {last_name}"]


    def list_contacts(self):
        self.contact_list = []
        for name in self.contacts.keys():
            self.contact_list.append([name, self.contacts[name]["mobile"], self.contacts[name]["home"], self.contacts[name]["email"], self.contacts[name]["address"]])
        self._print_contacts()


    def _print_contacts(self):
        for i, element in enumerate(sorted(self.contact_list, key=lambda x: x[0])):
            if element != None:
                print(f'{i+1}. ' + element[0])
                print(f"\tmobile: {element[1]}")
                print(f"\thome: {element[2]}")
                print(f"\temail: {element[3]}")
                print(f"\tmobile: {element[4]}")


    def search_contact(self, first_name, last_name):
        return self.contacts[f'{first_name} {last_name}']

c = ContactHandler()
# c.add_contact("Alan", "Joss")
# c.add_contact("Haonan", "Nüssli")
# c.add_contact("David", "Jäggli")

print(c.search_contact("David", "Jäggli"))
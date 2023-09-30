from contact import Contact

class Notebook:
    def __init__(self):
        self._id = 0
        self._contacts = dict()

    def add_contact(self, contact: Contact):
        self._id += 1
        self._contacts[str(self._id)] = contact

    def change_contact(self, id: str, new_contact: Contact):
        self._contacts[id] = new_contact

    def del_contact(self, id: str):
        del self._contacts[id]

    def get_contacts(self):
        return self._contacts
    
    
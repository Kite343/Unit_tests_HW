import unittest
from unittest.mock import patch

from contact import Contact
from notebook import Notebook
from user_interface import *

class TestUserInterface(unittest.TestCase):
    def setUp(self) -> None:
        self.user_interface = UserInterface()

    # интеграционный тест
    # Проверка того, что при добавлении контакта через  пользовательский интерфейс,
    #  контакт корректно отображается в списке контактов.
    def test_add_contact(self):
        contact = Contact("test", "12345")
        self.user_interface.notebook.add_contact(contact)
        self.assertTrue(contact in self.user_interface.notebook._contacts.values(), 'test_add_contact failed')
        contact = Contact("test2", "0000")
        self.user_interface.notebook.add_contact(contact)
        self.assertEqual(self.user_interface.notebook._contacts["2"], contact)

    @patch('builtins.input', side_effect=['test', '0000'])    
    def test_def_add_contact(self, input_mock):
        self.user_interface.actions["2"](self.user_interface.notebook)
        self.assertEqual(self.user_interface.notebook._contacts["1"].__str__(), "test: 0000")


    # @patch('builtins.input', lambda *args: 'test')    
    # def test_def_add_contact(self):
    #     self.user_interface.actions["2"](self.user_interface.notebook)
    #     self.assertEqual(self.user_interface.notebook._contacts["1"].__str__(), "test: test")

    
if __name__ == '__main__':
    unittest.main(verbosity=2)

# coverage run -m unittest test_user_interfase.py -v
# coverage report

# contact.py                   6      0   100%
# notebook.py                 14      3    79%
# test_user_interfase.py      21      1    95%
# user_interface.py           66     48    27%
# --------------------------------------------
# TOTAL                      107     52    51%
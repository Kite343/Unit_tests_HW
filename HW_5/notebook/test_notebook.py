import unittest
from contact import Contact
from notebook import Notebook

# Юнит-тесты:
#         * для Notebook проверка отдельных функций:
#             - add_contact -  добавление контакта
#             - change_contact - редактирование контакта
#             - del_contact - удаление контакта
#             - get_contacts - получение всех контактов

class TestNotebook(unittest.TestCase):
    def setUp(self) -> None:
        self.notebook = Notebook()

    # Проверка того, что функция addContact корректно добавляет новый контакт в список контактов
    def test_add_contact(self):
        contact = Contact("test", "12345")
        self.notebook.add_contact(contact)
        self.assertTrue(contact in self.notebook._contacts.values(), 'test_add_contact failed')
        contact = Contact("test2", "0000")
        self.notebook.add_contact(contact)
        self.assertEqual(self.notebook._contacts["2"], contact)

    def test_change_contact(self):
        contact = Contact("test", "12345")
        self.notebook.add_contact(contact)
        contact_1 = Contact("new", "0000")
        self.notebook.change_contact("1", contact_1)
        self.assertEqual(self.notebook._contacts["1"], contact_1)

    def test_del_contact(self):
        test_dict = dict()
        for i in range(1, 4):
            contact = Contact(f"test_{i}", "000{i}")        
            self.notebook.add_contact(contact)
            test_dict[str(i)] =  contact
        
        self.notebook.del_contact("2")
        del test_dict["2"]
        self.assertTrue(test_dict == self.notebook._contacts , 'test_del_contact failed')

    def test_get_contacts(self):
        test_dict = dict()
        for i in range(1, 4):
            contact = Contact(f"test_{i}", "000{i}")        
            self.notebook.add_contact(contact)
            test_dict[str(i)] =  contact
        self.assertTrue(test_dict == self.notebook.get_contacts() , 'test_get_contacts failed')

if __name__ == '__main__':
    unittest.main(verbosity=2)

# coverage run -m unittest test_notebook.py -v
# coverage report

# Name               Stmts   Miss  Cover
# --------------------------------------
# contact.py             6      1    83%
# notebook.py           14      0   100%
# test_notebook.py      37      1    97%
# --------------------------------------
# TOTAL                 57      2    96%
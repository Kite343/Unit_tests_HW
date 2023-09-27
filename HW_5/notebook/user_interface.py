from contact import Contact
from notebook import Notebook

def all_contacts(notebook: Notebook):
    print("контакты:\n")
    for key, value in notebook.get_contacts().items():
        print(f"id: {key} \n{value}\n")

def add_contact(notebook: Notebook):
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    new_contact = Contact(name, phone)
    notebook.add_contact(new_contact)
    print("контакт добавлен")

def change_contact(notebook: Notebook):
    contacts = notebook.get_contacts()
    id = input("Введите id контакта: ")

    if id in contacts:
        print("""Выберите действие:
                1. изменить имя
                2. изменить телефон
                3. изменить все данные""")
        choice = input("Ваш выбор: ")

        if choice == "1":
            name = input("Введите имя: ")
            new_contact = Contact(name, contacts[id].phone)
            notebook.change_contact(id, new_contact)
            print("контакт изменен")
        elif choice == "2":
            phone = input("Введите номер телефона: ")
            new_contact = Contact(contacts[id].name, phone)
            notebook.change_contact(id, new_contact)
            print("контакт изменен")
        elif choice == "3":
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            new_contact = Contact(name, phone)
            notebook.change_contact(id, new_contact)
            print("контакт изменен")
        else:
            print("Неверный ввод. Такое действие отсутствует")        
    else:
        print("Неверный ввод. контакта с таким id не существует")

def del_contact(notebook: Notebook):
    contacts = notebook.get_contacts().keys()
    id = input("Введите id контакта: ")

    if id in contacts:
        notebook.del_contact(id)
        print("контакт удален")
    else:
        print("Неверный ввод. контакта с таким id не существует")

def get_contact(notebook: Notebook):
    contacts = notebook.get_contacts()
    id = input("Введите id контакта: ")

    if id in contacts:
        print(contacts[id])
    else: 
        print("Неверный ввод. контакта с таким id не существует")
  


class UserInterface:

    def __init__(self):
        self.notebook = Notebook()
        self.actions = {
                    "1": all_contacts,
                    "2": add_contact,
                    "3": change_contact,
                    "4": del_contact,
                    "5": get_contact,
        }

    def main(self):
        while True:
            print("""Выберите действие:
                    1. Показать все контакты
                    2. Добавить контакт
                    3. Редактировать контакт
                    4. Удалить контакт
                    5. Показать контакт
                    6. Выйти""")

            choice = input("Ваш выбор: ")

            if choice in self.actions:
                self.actions[choice](self.notebook)
            elif choice == "6":
                print("Выход из программы")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")




if __name__ == "__main__":
    user_notebook = UserInterface()
    user_notebook.main()
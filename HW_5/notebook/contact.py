class Contact:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name}: {self.phone}'
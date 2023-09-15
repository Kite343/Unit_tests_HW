from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, company, model, year_release):
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = 0
        self._speed = 0

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def test_drive(self):
        pass

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def park(self):
        pass
    
    @property
    @abstractmethod
    def speed(self):
        pass

    @property
    @abstractmethod
    def num_wheels(self):
        pass


class Car(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self._num_wheels = 4
        self._speed = 0

    def test_drive(self):
        self._speed = 60

    def park(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed
    
    @property
    def num_wheels(self):
        return self._num_wheels

    def __str__(self):
        return f'Car: {self.company}, {self.model}, {self.year_release}'


class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self._num_wheels = 2
        self._speed = 0

    def test_drive(self):
        self._speed = 75

    def park(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed
    
    @property
    def num_wheels(self):
        return self._num_wheels

    def __str__(self):
        return f'Motorcycle: {self.company}, {self.model}, {self.year_release}'
import unittest

from vehicles import Car, Motorcycle, Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.test_car = Car("Lada", "Calina", 2012)
        self.test_moto = Motorcycle("Harley-Davidson", "Sportster", 2017)

    def test_car_is_instance_of_vehicle(self):
        """test: объект Car также является экземпляром Vehicle"""
        self.assertIsInstance(self.test_car, Vehicle)

    def test_car_has_4_wheels(self):
        """test: количества колёс Car"""
        self.assertEqual(self.test_car.num_wheels, 4)

    def test_motorcycle_has_2_wheels(self):
        """test: количества колёс Motorcycle"""
        self.assertEqual(self.test_moto.num_wheels, 2)

    def test_car_speed_after_test_drive(self):
        """test: объект Car развивает скорость 60
          в режиме тестового вождения 
          (используя метод testDrive())"""
        
        self.test_car.test_drive()
        self.assertEqual(self.test_car.speed, 60)

    def test_motorcycle_speed_after_test_drive(self):
        """test: объект Motorcycle развивает скорость 75 
        в режиме тестового вождения 
        (используя метод testDrive())."""

        self.test_moto.test_drive()
        self.assertEqual(self.test_moto.speed, 75)

    def test_car_speed_after_park(self):
        """test: Проверка остановки в режиме парковки для Car"""
        self.test_car.test_drive()
        self.test_car.park()
        self.assertEqual(self.test_car.speed, 0)

    def test_motorcycle_speed_after_park(self):
        """test: Проверка остановки в режиме парковки для Car"""
        self.test_moto.test_drive()
        self.test_moto.park()
        self.assertEqual(self.test_moto.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
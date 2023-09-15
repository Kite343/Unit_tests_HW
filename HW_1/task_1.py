# В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки и
# возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ. Если метод calculateDiscount
# получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения

class Calculator:
    def __new__(cls):
        instance = super().__new__(cls)
        return instance
    
    def calculate_discount(self, purchase_amount: float, discount_percentage: float)  -> float:
        if not isinstance(purchase_amount, (int, float)) or purchase_amount < 0:
            raise ValueError(f"{purchase_amount} должно быть числом >= 0")
        
        if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError(f"{discount_percentage} должно быть числом в диапозоне от 0 до 100")

        discount_price = purchase_amount * (1 - discount_percentage / 100)
        return discount_price
    

def test_calculate_discount_valid_inputs():
    calculator = Calculator()
    assert calculator.calculate_discount(100, 2) == 98.0, "неверный ввод"
    assert calculator.calculate_discount(50.5, 25) == 37.875, "неверный ввод"


def test_calculate_discount_inputs_negative():
    calculator = Calculator()
    try:
        calculator.calculate_discount("test", 10)
    except ValueError:
        assert "Неверный ввод: введено не число"

    try:
        calculator.calculate_discount(-100, 10)
    except ValueError:
        assert "purchase_amount отрицательное число"

    try:
        calculator.calculate_discount(100, -10)
    except ValueError:
        assert "discount_percentage отрицательное число"

    try:
        calculator.calculate_discount(100, 110)
    except ValueError:
        assert "Неверный диапазон discount_percentage"


if __name__ == "__main__":
    test_calculate_discount_valid_inputs()
    test_calculate_discount_inputs_negative()
    print("Все тесты пройдены успешно!")


import doctest


class Car:
    """
    Класс для описания автомобиля.

    Атрибуты:
    make (str): Марка автомобиля.
    model (str): Модель автомобиля.
    year (int): Год выпуска автомобиля.
    fuel_level (float): Уровень топлива в автомобиле (в литрах).
    """

    def __init__(self, make: str, model: str, year: int, fuel_level: float):
        """
        Инициализация автомобиля.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param fuel_level: Уровень топлива в автомобиле.
        :raise ValueError: Если уровень топлива меньше 0 или больше максимума.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020, 50)
        >>> car.make
        'Toyota'
        >>> car.fuel_level
        50
        """
        if fuel_level < 0 or fuel_level > 100:
            raise ValueError("Уровень топлива должен быть от 0 до 100 литров.")
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> None:
        """
        Метод для движения автомобиля на определенное расстояние.

        :param distance: Расстояние в километрах, которое будет преодолен автомобиль.
        :raise ValueError: Если недостаточно топлива для поездки.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020, 50)
        >>> car.drive(20)
        >>> car.fuel_level
        48
        """
        fuel_needed = distance * 0.1  # 1 км требует 0.1 литра топлива
        if fuel_needed > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки.")
        self.fuel_level -= fuel_needed

    def refuel(self, amount: float) -> None:
        """
        Заправка автомобиля.

        :param amount: Количество топлива, которое заправляется.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020, 50)
        >>> car.refuel(30)
        >>> car.fuel_level
        80
        """
        if self.fuel_level + amount > 100:
            raise ValueError("Перелив топлива! Максимальный уровень — 100 литров.")
        self.fuel_level += amount


class Person:

    def __init__(self, name: str, age: int, height: float):
        """
        Инициализация данных человека.

        :param name: Имя человека.
        :param age: Возраст человека.
        :param height: Рост человека.
        :raise ValueError: Если возраст или рост отрицательные.

        Примеры:
        >>> person = Person("John", 30, 175)
        >>> person.name
        'John'
        >>> person.age
        30
        """
        if age < 0 or height < 0:
            raise ValueError("Возраст и рост не могут быть отрицательными.")
        self.name = name
        self.age = age
        self.height = height

    def birthday(self) -> None:
        """
        Метод для увеличения возраста человека на 1 год.

        Примеры:
        >>> person = Person("John", 30, 175)
        >>> person.birthday()
        >>> person.age
        31
        """
        self.age += 1

    def grow(self, cm: float) -> None:
        """
        Метод для увеличения роста человека.

        :param cm: Количество сантиметров, на которое вырастет человек.

        Примеры:
        >>> person = Person("John", 30, 175)
        >>> person.grow(5)
        >>> person.height
        180
        """
        self.height += cm


class BankAccount:
    """
    Класс для описания банковского счета.

    Атрибуты:
    account_holder (str): Имя владельца счета.
    balance (float): Баланс счета.
    """

    def __init__(self, account_holder: str, balance: float = 0):
        """
        Инициализация банковского счета.

        :param account_holder: Имя владельца счета.
        :param balance: Начальный баланс счета.
        :raise ValueError: Если баланс отрицателен.

        Примеры:
        >>> account = BankAccount("John", 100)
        >>> account.balance
        100
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счет.

        :param amount: Сумма депозита.

        Примеры:
        >>> account = BankAccount("John", 100)
        >>> account.deposit(50)
        >>> account.balance
        150
        """
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег с счета.

        :param amount: Сумма для снятия.
        :raise ValueError: Если на счете недостаточно средств.

        Примеры:
        >>> account = BankAccount("John", 100)
        >>> account.withdraw(30)
        >>> account.balance
        70
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount


if __name__ == "__main__":
    doctest.testmod()  # Проверка работы примеров в документации

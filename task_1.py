class SocialNetwork:
    """
    Базовый класс для социальных сетей.
    Реализует общие атрибуты и методы для различных социальных сетей.
    """

    def __init__(self, name: str, launch_year: int, user_count: int):
        """
        Конструктор для инициализации базовых атрибутов.

        :param name: Название социальной сети.
        :param launch_year: Год запуска социальной сети.
        :param user_count: Количество пользователей.
        """
        self.name = name
        self.launch_year = launch_year
        self.user_count = user_count

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с информацией о социальной сети.
        """
        return f"{self.name} (Запуск: {self.launch_year}, Пользователей: {self.user_count})"

    def __repr__(self) -> str:
        """
        Возвращает более подробное строковое представление объекта для отладки.

        :return: Строка для представления объекта.
        """
        return f"SocialNetwork(name='{self.name}', launch_year={self.launch_year}, user_count={self.user_count})"

    def total_revenue(self) -> float:
        """
        Метод для вычисления дохода социальной сети (упрощенная модель).

        :return: Предположительный доход.
        """
        return self.user_count * 0.5  # например, 0.5 доллара на пользователя


class VK(SocialNetwork):
    """
    Класс, представляющий социальную сеть VK.
    Наследует от базового класса SocialNetwork.
    """

    def __init__(self, name: str, launch_year: int, user_count: int, region: str):
        """
        Конструктор для инициализации атрибутов социальной сети VK.
        Расширяет конструктор базового класса.

        :param name: Название социальной сети (по умолчанию VK).
        :param launch_year: Год запуска.
        :param user_count: Количество пользователей.
        :param region: Регион, в котором популярна социальная сеть.
        """
        super().__init__(name, launch_year, user_count)
        self.region = region

    def __str__(self) -> str:
        """
        Переопределение метода для строкового представления объекта.

        :return: Строка с информацией о VK.
        """
        return f"VK (Запуск: {self.launch_year}, Пользователей: {self.user_count}, Регион: {self.region})"

    def __repr__(self) -> str:
        """
        Переопределение метода для представления объекта для отладки.

        :return: Строка для отладки объекта.
        """
        return f"VK(name='{self.name}', launch_year={self.launch_year}, user_count={self.user_count}, region='{self.region}')"

    def total_revenue(self) -> float:
        """
        Переопределение метода для вычисления дохода VK.
        Модель дохода отличается от общей социальной сети.

        :return: Модифицированный расчет дохода.
        """
        # Более высокая ставка на пользователя в VK (например, 1 доллар на пользователя)
        return self.user_count * 1.0


if __name__ == "__main__":
    # Создаем экземпляры классов
    social_network = SocialNetwork("Generic Network", 2005, 1000000)
    vk_network = VK("VK", 2006, 250000000, "Россия")

    # Выводим информацию о социальных сетях
    print(social_network)
    print(vk_network)

    # Выводим информацию о доходах
    print(f"Доход Generic Network: {social_network.total_revenue()} долларов")
    print(f"Доход VK: {vk_network.total_revenue()} долларов")

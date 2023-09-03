import csv
from abc import ABC


class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # Коэффицент скидки
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        """
        :return: Class(name, price, quantity)
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        :return: name
        """
        return f"{self.__name}"

    def __add__(self, other):
        """
        Складывание колличества товаров одного или нескольких классов
        :param other: количество товара того же или другого класса
        :return: общая сумма или предварительная ошибка
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от него')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        result = self.price * self.quantity
        if result < 0:
            raise ValueError('Количество товара не может быть отрицательным.')
        return result

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        if Item.pay_rate < 0:
            raise ValueError('Скидка не может быть отрицательной.')
        return self.price

    @property
    def name(self):
        """
        геттер имени товара
        :return: имя
        """
        return self.__name

    @name.setter
    def name(self, __name):
        """
        сеттер имени товара (сокращает, если имя длиннее 10 символов)
        :param __name:
        :return: имя
        """
        if len(__name) > 10:
            self.__name = __name[:9]
        else:
            self.__name = __name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Метод класса для открытия файла
        :return:
        """
        cls.all = []
        with open('/home/alex/PycharmProjects/electronics-shop-project /electronics-shop-project/src/items.csv',
                  'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(row.get('name'), float(row.get('price')), int(row.get('quantity')))

    @staticmethod
    def string_to_number(str_num):
        """
        Статический метод для перевода строки в цыфру
        :param str_num: строка
        :return: цыфра
        """
        return int(float(str_num))

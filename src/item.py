import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.price}', {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, __name):
        if len(__name) > 10:
            self.__name = __name[:9]
        else:
            self.__name = __name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('/home/alex/PycharmProjects/electronics-shop-project /electronics-shop-project/src/items.csv',
                  'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(row.get('name'), float(row.get('price')), int(row.get('quantity')))

    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))

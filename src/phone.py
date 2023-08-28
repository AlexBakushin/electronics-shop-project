from src.item import Item


class Phone(Item):
    """
    Дочерний класс от класса Item, представляющий телефоны
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляка класса
        :param name: имя
        :param price: цена за шт
        :param quantity: количество телефонов
        :param number_of_sim: количество сим-карт

        взятие инициализации у родительского класса Item
        проверка количества сим-карт
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        if self.number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

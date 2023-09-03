from src.item import Item


class MixinLog:
    """
    Класс - Миксин, для товара - клавиатуры
    """
    def __init__(self):
        """
        Инициализация ( по умолчанию язык клавиатуры - EN )
        """
        self.__language = 'EN'

    @property
    def language(self):
        """
        Сеттер для языка клавиатуры
        :return: язык клав.
        """
        return self.__language

    def change_lang(self):
        """
        Меняет язык клавиатуры (с EN > RU и с RU > EN)
        :return: Смененный язык
        """
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        elif self.__language == 'RU':
            self.__language = 'EN'
            return self.__language


class Keyboard(Item, MixinLog):
    """
    Класс клавиатуры
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализыция товара - клавиатуры со взятием функцианала от класса Item и Миксина
        :param name: Имя
        :param price: Цена
        :param quantity: Количество
        """
        super().__init__(name, price, quantity)


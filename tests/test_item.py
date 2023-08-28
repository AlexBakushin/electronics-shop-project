from src.item import Item
from src.phone import Phone


def test___init__():
    """
    Тест на проверку инициализации
    :return:
    """
    item1 = Item('test', 100, 10)
    assert str(item1) == 'test'


def test_calculate_total_price():
    """
    Тест на проверку общей цены товара
    :return:
    """
    item1 = Item("test", 10000, -1)
    assert item1.calculate_total_price() == -10000
    item2 = Item('test', 1000, 12)
    assert item2.calculate_total_price() == 12000


def test_apply_discount():
    """
    Тест на проверку применения скидки
    :return:
    """
    item1 = Item('test', 100, 10)
    Item.pay_rate = 0.1
    assert item1.apply_discount() == 10


def test_name():
    """
    Тест на проверку длинны имени
    :return:
    """
    item1 = Item('super_test_phone', 1000, 5)
    assert item1.name == 'super_test_phone'
    item1.name = 'super_test_phone'
    assert item1.name == 'super_tes'


def test_instantiate_from_csv():
    """
    Тест на проверку открытия файла
    :return:
    """
    item1 = Item.instantiate_from_csv()
    assert isinstance(item1, Item) == False


def test_string_to_number():
    """
    Тест на проверку перевода строки в цифру
    :return:
    """
    assert Item.string_to_number('120') == 120


def test___repr__():
    """
    Тест __repr__
    :return:
    """
    item1 = Item("Наушники", 2000, 50)
    assert repr(item1) == "Item('Наушники', 2000, 50)"


def test___str__():
    """
    Тест __str__
    :return:
    """
    item1 = Item("Наушники", 2000, 50)
    assert str(item1) == 'Наушники'


def test___add__():
    """
    Тест на проверку правильного сложения количества товаров разных классов
    :return:
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

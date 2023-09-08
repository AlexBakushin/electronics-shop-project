from src.item import Item, InstantiateCSVError
from src.phone import Phone
import pytest
import csv


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
    item1 = Item('test', 1000, 12)
    assert item1.calculate_total_price() == 12000


def test_calculate_total_price__value_error():
    """
    Тест общей цены товара c проверкой количества товара на складе
    :return:
    """
    with pytest.raises(ValueError):
        item1 = Item("test", 10000, -1)
        item1.calculate_total_price()


def test_apply_discount():
    """
    Тест на проверку применения скидки
    :return:
    """
    item1 = Item('test', 100, 10)
    Item.pay_rate = 0.2
    assert item1.apply_discount() == 20


def test_apply_discount_value_error():
    """
    Проверка, что скидка не отрицательное число
    :return:
    """
    with pytest.raises(ValueError):
        item1 = Item('test', 100, 10)
        Item.pay_rate = -0.1
        item1.apply_discount()


def test_name():
    """
    Тест на проверку длинны имени
    :return:
    """
    item1 = Item('Super_test_phone', 1000, 5)
    item2 = Item('Test_phone', 500, 20)
    assert item1.name == 'Super_test_phone'
    assert item2.name == 'Test_phone'
    item1.name = 'Super_test_phone'
    item2.name = 'Test_phone'
    assert item1.name == 'Super_tes'
    assert item2.name == 'Test_phone'


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


def test___add____value_error():
    """
    Проверка типа для объектов суммы их количества
    :return:
    """
    with pytest.raises(ValueError):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        phone1 + 15


def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError):
        row = {'name': 'Колонки', 'price': '75', 'quantity': None}
        if type(row.get('name')) is str and row.get('name') != '':
            if type(row.get('price')) is str and row.get('price') != '':
                if type(row.get('quantity')) is str and row.get('quantity') != '':
                    pass
                else:
                    raise InstantiateCSVError
            else:
                raise InstantiateCSVError
        else:
            raise InstantiateCSVError


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
            reader = csv.DictReader(
                open('/home/alex/PycharmProjects/electronics-shop-project /electronics-shop-project/src/items.csv',
                     'r'))
            raise FileNotFoundError

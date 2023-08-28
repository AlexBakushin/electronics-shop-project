from src.item import Item
from src.phone import Phone


def test___init__():
    item1 = Item('test', 100, 10)
    assert str(item1) == 'test'


def test_calculate_total_price():
    item1 = Item("test", 10000, -1)
    assert item1.calculate_total_price() == -10000


def test_apply_discount():
    item1 = Item('test', 100, 10)
    Item.pay_rate = 0.1
    assert item1.apply_discount() == 10


def test_name():
    item1 = Item('super_test_phone', 1000, 5)
    assert item1.name == 'super_test_phone'
    item1.name = 'super_test_phone'
    assert item1.name == 'super_tes'


def test_instantiate_from_csv():
    item1 = Item.instantiate_from_csv()
    assert isinstance(item1, Item) == False


def test_string_to_number():
    assert Item.string_to_number('120') == 120


def test___repr__():
    item1 = Item("Наушники", 2000, 50)
    assert repr(item1) == "Item('Наушники', 2000, 50)"


def test___str__():
    item1 = Item("Наушники", 2000, 50)
    assert str(item1) == 'Наушники'


def test___add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

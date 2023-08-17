from src.item import Item


def test_calculate_total_price():
    item1 = Item("test", 10000, -1)
    assert item1.calculate_total_price() == -10000


def test_apply_discount():
    item1 = Item('test', 100, 10)
    Item.pay_rate = 0.1
    assert item1.apply_discount() == 10

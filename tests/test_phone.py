from src.phone import Phone


def test___init__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test___repr__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

from src.phone import Phone
import pytest


def test___init__():
    """
    Тест инициализации
    :return:
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test___init____value_error():
    """
    Тест инициализации с проверкой ошибки малого количества сим-карт
    :return:
    """
    with pytest.raises(ValueError):
        phone2 = Phone("iPhone 20", 120_000, 5, 0)
        str(phone2)


def test___repr__():
    """
    Тест __repr__
    :return:
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

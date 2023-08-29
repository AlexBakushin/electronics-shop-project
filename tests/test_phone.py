from src.phone import Phone
import pytest


def test___init__():
    """
    Тест инициализации
    :return:
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    """
    Тест с проверкой ошибки малого количества сим-карт
    :return:
    """
    phone1 = Phone("iPhone 10", 20_000, 5, 2)
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2


def test_number_of_sim__value_error():
    with pytest.raises(ValueError):
        phone2 = Phone("iPhone 20", 120_000, 5, 0)
        phone2.number_of_sim = 0
        phone2.number_of_sim


def test___repr__():
    """
    Тест __repr__
    :return:
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

from src.keyboard import Keyboard, MixinLog
import pytest


def test___init__():
    """
    Тест на проверку инициализации
    :return:
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == 'Dark Project KD87A'
    assert str(kb.language) == 'EN'

    kb.change_lang()
    assert str(kb.language) == 'RU'

    kb.change_lang()
    assert str(kb.language) == 'EN'


def test_language():
    """
    Тест на проверку языка по умолчанию
    :return:
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'


def test_change_lang():
    """
    Тест на проверку смены языка клавиатуры
    :return:
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == 'RU'
    kb.change_lang()
    assert str(kb.language) == 'EN'

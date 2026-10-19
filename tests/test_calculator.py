import pytest

from toolkit.calculator import calculate, tokenize


def test_add():
    assert calculate(tokenize("2+2")) == 4.0


def test_priority():
    assert calculate(tokenize("2+2*2")) == 6.0


def test_division():
    assert calculate(tokenize("10/2")) == 5.0


def test_space():
    assert calculate(tokenize("1 + 2")) == 3.0


def test_negative():
    assert calculate(tokenize("-5")) == -5.0


def test_mod():
    assert calculate(tokenize("10%3")) == 1.0


def test_div_zero():
    with pytest.raises(ValueError):
        calculate(tokenize("10/0"))


def test_invalid_char():
    with pytest.raises(ValueError):
        tokenize("2@2")
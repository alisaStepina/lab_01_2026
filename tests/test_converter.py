import pytest

from toolkit.converter import convert


def test_cm_to_m():
    assert convert(100, "cm", "m") == 1.0


def test_kg_to_g():
    assert convert(1, "kg", "g") == 1000.0


def test_c_to_f():
    assert convert(0, "c", "f") == 32.0


def test_km_to_mm():
    assert convert(1, "km", "mm") == 1000000.0


def test_unknown_unit():
    with pytest.raises(ValueError):
        convert(1, "xyz", "m")


def test_incompatible():
    with pytest.raises(ValueError):
        convert(1, "m", "kg")


def test_below_zero():
    with pytest.raises(ValueError):
        convert(-300, "c", "k")
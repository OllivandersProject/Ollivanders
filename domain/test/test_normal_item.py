import pytest
from


def test_normal_item_day_0():
    normal = NormalItem('NormalItem', 5, 13)
    normal.update_quality()
    assert normal.get_quality() == 12


def test_normal_item_day_1():
    normal = NormalItem('NormalItem', 4, 12)
    normal.update_quality()
    assert normal.get_quality() == 11


def test_normal_item_day_2():
    normal = NormalItem('NormalItem', 3, 11)
    normal.update_quality()
    assert normal.get_quality() == 10


def test_normal_item_day_3():
    normal = NormalItem('NormalItem', 2, 10)
    normal.update_quality()
    assert normal.get_quality() == 9


def test_normal_item_day_4():
    normal = NormalItem('NormalItem', 1, 9)
    normal.update_quality()
    assert normal.get_quality() == 8


def test_normal_item_day_5():
    normal = NormalItem('NormalItem', 0, 8)
    normal.update_quality()
    assert normal.get_quality() == 6


def test_normal_item_day_6():
    normal = NormalItem('NormalItem', -1, 6)
    normal.update_quality()
    assert normal.get_quality() == 4


def test_normal_item_day_7():
    normal = NormalItem('NormalItem', -2, 4)
    normal.update_quality()
    assert normal.get_quality() == 2


def test_normal_item_day_8():
    normal = NormalItem('NormalItem', -3, 2)
    normal.update_quality()
    assert normal.get_quality() == 0


def test_normal_item_day_9():
    normal = NormalItem('NormalItem', -4, 0)
    normal.update_quality()
    assert normal.get_quality() == 0


def test_normal_item_day_10():
    normal = NormalItem('NormalItem', -5, 0)
    normal.update_quality()
    assert normal.get_quality() == 0

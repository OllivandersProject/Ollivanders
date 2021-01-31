from src.aged_bire import AgedBrie
import pytest


def test_aged_brie_day_0():
    AbedBrieItem = AgedBrie('AgedBrie', 2, 0)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 1


def test_aged_brie_day_1():
    AbedBrieItem = AgedBrie('AgedBrie', 1, 1)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 2


def test_aged_brie_day_2():
    AbedBrieItem = AgedBrie('AgedBrie', 0, 2)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 4


def test_aged_brie_day_3():
    AbedBrieItem = AgedBrie('AgedBrie', -1, 4)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 6


def test_aged_brie_day_4():
    AbedBrieItem = AgedBrie('AgedBrie', -2, 6)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 8


def test_aged_brie_day_5():
    AbedBrieItem = AgedBrie('AgedBrie', -3, 8)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 10


def test_aged_brie_day_6():
    AbedBrieItem = AgedBrie('AgedBrie', -4, 10)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 12


def test_aged_brie_day_7():
    AbedBrieItem = AgedBrie('AgedBrie', -5, 12)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 14


def test_aged_brie_day_8():
    AbedBrieItem = AgedBrie('AgedBrie', -6, 14)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 16


def test_aged_brie_day_9():
    AbedBrieItem = AgedBrie('AgedBrie', -7, 16)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 18


def test_aged_brie_day_10():
    AbedBrieItem = AgedBrie('AgedBrie', -8, 18)
    AgedBrieItem.update_quality()
    assert AgedBrieItem.get_quality() == 20

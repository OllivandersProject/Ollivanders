from src.backstagePasses import BackstagePasses
import pytest


def test_bakstage_passes_day_0():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 15, 20)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 21

    BackstagePassesItem = BackstagePasses('BackstagePasses', 10, 49)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses', 5, 49)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50


def test_bakstage_passes_day_1():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 14, 21)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 22

    BackstagePassesItem = BackstagePasses('BackstagePasses', 5, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses', 5, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50


def test_bakstage_passes_day_2():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 13, 22)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 23

    BackstagePassesItem = BackstagePasses('BackstagePasses', 8, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses', 3, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50


def test_bakstage_passes_day_3():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 12, 23)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 24

    BackstagePassesItem = BackstagePasses('BackstagePasses', 7, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses', 2, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50


def test_bakstage_passes_day_4():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 11, 24)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 25

    BackstagePassesItem = BackstagePasses('BackstagePasses', 6, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses', 1, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50


def test_bakstage_passes_day_5():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 10, 25)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 27

    BackstagePassesItem = BackstagePasses('BackstagePasses', 5, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses', 0, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0


def test_bakstage_passes_day_6():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 9, 27)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 29

    BackstagePassesItem = BackstagePasses('BackstagePasses', 4, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses',  -1, 0)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0


def test_bakstage_passes_day_7():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 8, 29)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 31

    BackstagePassesItem = BackstagePasses('BackstagePasses', 2, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses',  -3, 0)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0


def test_bakstage_passes_day_8():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 7, 31)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 33

    BackstagePassesItem = BackstagePasses('BackstagePasses', 2, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 50

    BackstagePassesItem = BackstagePasses('BackstagePasses',  -3, 0)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0


def test_bakstage_passes_day_9():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 6, 33)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 35

    BackstagePassesItem = BackstagePasses('BackstagePasses', 0, 50)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0

    BackstagePassesItem = BackstagePasses('BackstagePasses',  -5, 0)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0


def test_bakstage_passes_day_10():
    BackstagePassesItem = BackstagePasses('BackstagePasses', 4, 38)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 41

    BackstagePassesItem = BackstagePasses('BackstagePasses', -1, 0)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0

    BackstagePassesItem = BackstagePasses('BackstagePasses',  -6, 0)
    BackstagePassesItem.update_quality()
    assert BackstagePassesItem.get_quality() == 0

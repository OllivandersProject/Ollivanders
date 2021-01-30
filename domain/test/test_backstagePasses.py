from src.backstagePasses import backstagePasses


def test_bakstage_passes_day_0():
    assert Item('BackstagePasses', 15, 20).update_quality()
    assert Item('BackstagePasses', 10, 49).update_quality()
    assert Item('BackstagePasses', 5, 49).update_quality()


def test_bakstage_passes_day_1():
    assert Item('BackstagePasses', 14, 21).update_quality()
    assert Item('BackstagePasses', 9, 50).update_quality()
    assert Item('BackstagePasses', 4, 50).update_quality()


def test_bakstage_passes_day_2():
    assert Item('BackstagePasses', 13, 20).update_quality()
    assert Item('BackstagePasses', 8, 50).update_quality()
    assert Item('BackstagePasses', 3, 50).update_quality()


def test_bakstage_passes_day_3():
    assert Item('BackstagePasses', 12, 23).update_quality()
    assert Item('BackstagePasses', 7, 50).update_quality()
    assert Item('BackstagePasses', 2, 50).update_quality()


def test_bakstage_passes_day_4():
    assert Item('BackstagePasses', 11, 24).update_quality()
    assert Item('BackstagePasses', 6, 50).update_quality()
    assert Item('BackstagePasses', 1, 50).update_quality()


def test_bakstage_passes_day_5():
    assert Item('BackstagePasses', 10, 25).update_quality()
    assert Item('BackstagePasses', 5, 50).update_quality()
    assert Item('BackstagePasses', 0, 50).update_quality()


def test_bakstage_passes_day_6():
    assert Item('BackstagePasses', 9, 27).update_quality()
    assert Item('BackstagePasses', 4, 50).update_quality()
    assert Item('BackstagePasses', -1, 50).update_quality()


def test_bakstage_passes_day_7():
    assert Item('BackstagePasses', 8, 29).update_quality()
    assert Item('BackstagePasses', 3, 50).update_quality()
    assert Item('BackstagePasses', -2, 0).update_quality()


def test_bakstage_passes_day_8():
    assert Item('BackstagePasses', 7, 31).update_quality()
    assert Item('BackstagePasses', 2, 50).update_quality()
    assert Item('BackstagePasses', -3, 0).update_quality()


def test_bakstage_passes_day_9():
    assert Item('BackstagePasses', 6, 33).update_quality()
    assert Item('BackstagePasses', 1, 50).update_quality()
    assert Item('BackstagePasses', -4, 0).update_quality()


def test_bakstage_passes_day_10():
    assert Item('BackstagePasses', 5, 35).update_quality()
    assert Item('BackstagePasses', 0, 50).update_quality()
    assert Item('BackstagePasses', -5, 0).update_quality()

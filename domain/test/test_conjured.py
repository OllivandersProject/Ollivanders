from src.Conjured import Conjured
import pytest

def test_conjured_properties():
    
    conjuredItem = Conjured('Conjured Item', 15, 50)
    
    assert conjuredItem.get_sell_in() == 15
    assert conjuredItem.get_quality() == 50
    assert conjuredItem.__str__() == "Item \n Name Sellin Quality \n 'Conjured Item' 15 50"
    

def test_conjured_day_six():
    
    conjuredItem = Conjured('Conjured Item', 6, 30)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == 5
    assert  conjuredItem.get_quality() == 28
    
def test_conjured_day_five():
    
    conjuredItem = Conjured('Conjured Item', 5, 28)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == 4
    assert  conjuredItem.get_quality() == 26
    
def test_conjured_day_four():
    
    conjuredItem = Conjured('Conjured Item', 4, 26)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == 3
    assert  conjuredItem.get_quality() == 24
    
def test_conjured_day_three():
    
    conjuredItem = Conjured('Conjured Item', 3, 24)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == 2
    assert  conjuredItem.get_quality() == 22
    
def test_conjured_day_two():
    
    conjuredItem = Conjured('Conjured Item', 2, 22)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == 1
    assert  conjuredItem.get_quality() == 20
    
def test_conjured_day_one():
    
    conjuredItem = Conjured('Conjured Item', 1, 20)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == 0
    assert  conjuredItem.get_quality() == 18
    
def test_conjured_no_sell_in():
    
    conjuredItem = Conjured('Conjured Item', 0, 18)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == -1
    assert  conjuredItem.get_quality() == 14
    
    conjuredItem = Conjured('Conjured Item', -1, 14)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == -2
    assert  conjuredItem.get_quality() == 10
    
    conjuredItem = Conjured('Conjured Item', -2, 10)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == -3
    assert  conjuredItem.get_quality() == 6
    
    conjuredItem = Conjured('Conjured Item', -3, 6)
    
    conjuredItem.update_quality()
    
    assert  conjuredItem.get_sell_in() == -4
    assert  conjuredItem.get_quality() == 2
    
    
import pytest
from src.app import add, sub

def test_add_function():
    assert add(2,3)==5
    assert add(3,4)==7


def test_sub_function():
    assert sub(5,2)==3
    assert sub(2,-3)==5
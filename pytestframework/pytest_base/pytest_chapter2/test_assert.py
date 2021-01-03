
import pytest

def func(x):
    sum = x + 2
    return sum

@pytest.fixture
def add_sum():
    sum = 2 + 3
    return sum

def test_add(add_sum):
    assert 2 + add_sum == 7


def test_one():
    assert func(4) == 6, "断言失败"


# pytest.raises()上下文关联

def myfunc():
    raise ValueError("Expection 123 raised")

def test_match():
    with pytest.raises(ValueError):
        myfunc()
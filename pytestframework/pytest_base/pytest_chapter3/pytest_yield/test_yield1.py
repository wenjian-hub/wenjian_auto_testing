
import pytest

@pytest.fixture()
def func_yield():
    sum = 5 + 5
    yield sum
    sum = 0


def test_one(func_yield):
    assert func_yield == 10


x_param = 5
y_param = 6
def test_request(fun_request):
    assert fun_request == 30
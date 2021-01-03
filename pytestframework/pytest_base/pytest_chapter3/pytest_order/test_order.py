
import pytest


order = []


@pytest.fixture(scope="seesion")
def s1():
    order.append("seesion")


@pytest.fixture(scope="module")
def s2():
    order.append("module")


@pytest.fixture(scope="function")
def s3():
    order.append("function")


@pytest.fixture(autouse=True)
def s4():
    order.append("autouse")


def test_order(s3, s2, s1, s4):
    assert order == ["seesion", "module", "function", "autouse"]
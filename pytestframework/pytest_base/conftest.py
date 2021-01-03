import pytest


# @pytest.fixture
# def fun1():
#     sum = 3 + 2
#     return sum

#
# @pytest.fixture(scope="module")
# def fun2():
#     sum1 = 6 + 6
#     return sum1


@pytest.fixture(scope="session")
def fun3():
    sum2 = 6 * 6
    return sum2


@pytest.fixture(scope="package")
def fun4():
    sum3 = 2 ** 3
    return sum3


@pytest.fixture(scope="module")
def fun_request(request):
    x, y = getattr(request.module, "x_param", "5")
    sum = x + y
    return sum

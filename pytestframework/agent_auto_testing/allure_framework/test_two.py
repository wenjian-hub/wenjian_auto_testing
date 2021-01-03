# __Author__: Dats
# __Date__ : 2020/5/8下午4:02

# 将多个测试用例分组到一个类里面

"""
    test_ :测试用例以test_ 开头

    Test: 测试用例类以 Test开头

    pytest -q 测试用例/测试目录    pytestpytest pytest_framework/test_one.py     pytest pytest_framework

"""



import pytest

def setup_module():
    print("setup_module 111")



def setup_class():
    print("setup_class 222")


def setup_mothod():
    print("setup_mothod 333")


def setup():
    print("setup 444")


def setup_function():
    print("setup_function 555")


# def test_one():
    print("pytest 6666")


class Test_pytest():

    def test_two(self):
        a = 5
        print(a)


if __name__ == "__main__":
    pytest.main(["-s", "pytest_framework"])





import pytest

def func(x):
    sum = x * x
    return sum

# 单个测试用例
def test_func():
    assert func(5) == 25

# 在一个类组织多个测试用例, 不允许存在__init__构造函数
class TestClass:
    def test_one(self):
        x = "this"
        assert "m" in x

    def test_two(self):
        x = "hello"
        assert "h" in x
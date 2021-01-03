
import pytest

# 这里将func 写入到func中， pytest会自动寻找


def test_one(fun1):
    assert fun1 == 5


def test_two_module(fun2):
    assert fun2 == 6


def test_three_module(fun2):
    assert fun2 == 12


def test_four_session(fun3):
    assert fun3 == 36


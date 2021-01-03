
import pytest
import time

def test_node1():
    time.sleep(2)
    print("test_nodeid1")
    assert 1


class TestNodeid:
    def test_nodeid1(self):
        time.sleep(3)
        print('TestNodeid::test_one')
        assert 1

    @pytest.mark.parametrize('x,y', [(1, 1), (3, 4)])
    def test_node2(self, x, y):
        time.sleep(2)
        print(f'TestNodeid::test_node2::{x} == {y}')
        assert x == y

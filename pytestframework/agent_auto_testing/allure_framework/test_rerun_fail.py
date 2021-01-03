
# 安装插件  pip install pytest-rerunfailures
# https://pypi.org/project/pytest-rerunfailures/


# 函数执行方式：@pytest.mark.flaky(reruns=2. reruns_deley=3)
# 命令执行方式：pytest --reruns=2 --reruns-delay=3

import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerun():
    assert 3 == 4



def test_rerun1():
    assert 5 == 6


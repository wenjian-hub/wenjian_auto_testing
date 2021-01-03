
import pytest


@pytest.fixture(scope="module", params=[10, 20])
def func(request):
    x = request.param
    sum = x + x
    return sum


def test_one(func):
    assert func == 20


# 自定义测试名称
@pytest.fixture(params=[1, 2, 3,4, 5], ids=["A", "B", "C", "D", "E"])
def func1(request):
    x = request.param
    sum = x + x
    return sum


def test_two(func1):
    print(func1)


@pytest.fixture(params=[1, 2, 3,4, 5])
def func2(request):
    x = request.param
    sum = x + x
    return sum


def test_three(func2):
    print(func2)

order = [
    {
        "addr": "黄金书",
        "city": "shenzhen"
    },
    {
        "addr": "wengan",
        "city": "guizhou"
    }
]

order = [
    {
        "addr": "黄金书",
        "city": "shenzhen"
    },
    {
        "addr": "福田",
        "city": "深圳"
    }
]


@pytest.fixture(params=order)
def func4(request):
    infor = request.param
    addr = infor["addr"]
    city = infor
    return addr

# 标记测试用例
@pytest.fixture(params=[('3+5', 8), pytest.param(('6*9', 54), marks=pytest.mark.xfail, id="failed")])
def data_set(request):
    data = request.param

    data_set1 = data[0]
    data_set2 = data[1]
    print(data_set1, data_set2)
    return data


def test_data(data_set):
    assert eval(data_set[0]) == data_set[1]


@pytest.mark.parametrize('test_input, expected', [('3 + 5', 8), pytest.param('6*9', 42, marks=pytest.mark.xfail, id='test_failed')])
def test_data2(test_input, expected):
    assert eval(test_input) == expected


# 模块化fixture, 就是fixture
@pytest.fixture(scope="module", params=["module1", "module2"])
def module(request):
    param = request.param
    print("set up param:{}".format(param))
    yield param
    print("tear down:{}".format(param))


@pytest.fixture(scope="function", params=["function1", "function2"])
def function(request):
    param = request.param
    print("set up param:{}".format(param))
    yield param
    print("tear down:{}".format(param))

def test_wenjian1(function):
    print("run to function:{}".format(function))

def test_wenjian2(module):
    print("run to module:{}".format(module))

def test_wenjian3(function, module):
    print("run to functon:{} and module:{}".format(function, module))

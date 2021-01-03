# 模块化fixture, 就是fixture
import pytest
@pytest.fixture(scope="module", params=["module1", "module2"])
def module(request):
    param = request.param
    print("set up param:{}".format(param))
    yield param
    print("tear down:{}".format(param))

@pytest.fixture(scope="session", params=["session1", "session2"])
def session(request):
    param = request.param
    print("set up param:{}".format(param))
    yield param
    print("tear down:{}".format(param))

@pytest.fixture(scope="class", params=["class1", "class2"])
def class_(request):
    param = request.param
    print("set up param:{}".format(param))
    yield param
    print("tear down:{}".format(param))

@pytest.fixture(scope="package", params=["package1", "package2"])
def package(request):
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

# def test_wenjian1(function):
#     print("run to function:{}".format(function))
#
# def test_wenjian2(module):
#     print("run to module:{}".format(module))
#
def test_wenjian3(session, module):
    print("run to module:{} and session:{}".format(module, session))


def test_wenjian4(class_, package):
    print("run to package:{} and class_:{}".format(package, class_))

# 执行顺序： session > module > package > class > function
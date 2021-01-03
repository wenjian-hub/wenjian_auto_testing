###fixture的使用

- fixture: 作为形参使用，对应的fixture就是函数的返回值
    ```
    @pytest.fixture
    def func():
        sum = 3 + 2
        return sum

    def test_one(func):
        assert func == 5

    def test_two(func):
        assert func == 6
    
    当test_one和test_two测试用例接收 func 函数时， fixture的作用是hi实例化函数，然后将函数返回
  然后返回 func 的值
  
 
- fixture 使用规则
    ````
    1. 如果想在多个测试模块中共用一个fixture, 可以把fixture 移动到conftest.py中，测试模块不需要手动导入，
   pytest会自动导入。
     
    2. fixture 自动导入的顺序： 测试类 > 测试模块 > conftest.py > 内置和第三方插件
    
- fixture 使用参数
    ```
    1. module 在当前.py脚本里面所有用例开始前只执行一次

    2. fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，如果多个用例只需调用一次fixture，
    那就可以设置为scope="session"，并且写到conftest.py文件里。
  
    3. package 会作用于包内的每一个测试用例, 且只被调用一次
    
    4. function  每个测试用例都会调用一次
  
    5. class  如果一个class 中有多个测试用例， 在类中只调用一次
  
- fixture 的清理操作
    ````
    比如在连接数据库时，操作完数据库之后，需要关闭数据库
    将fixture函数中的 return 换成 yield， 则yield后面的代码就是我们需要清理的操作, 也可以用with
    
- fixture 访问测试请求的上下文 request
    ````
   
- fixture 返回工厂函数

- fixture 参数化
    ```
  1. params是列表形式，当参数列表，request.param遍历参数
     @pytest.fixture(params=[1, 2, 3 ,4, 5], ids=["A", "B", "C", "D", "E"])
         def func1(request):
         x = request.param
         sum = x + x
         return sum
  
  2. params是列表形式， 当参数是字典，request.param遍历参数
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
  
  3. 同理，当参数是元组，或是其他数据类型，记住，首先params接收的是列表，然后处理列表里面的数据类型
  
- fixture参数化中标记测试用例  
    ```
    1. test_input, expected 接收输入和期望值, @pytest.mark.parametrize
    @pytest.mark.parametrize('test_input, expected', [('3 + 5', 8), pytest.param('6*9', 42, marks=pytest.mark.xfail, id='test_failed')])
    def test_data2(test_input, expected):
        assert eval(test_input) == expected
 
 - fixture中使用其他的fixture
    ```
    
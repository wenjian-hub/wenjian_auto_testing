###allure测试报告

####allure.step


####allure.attach 测试附件

    ```
    @allure.attach(body, name, attachment_type, extension)
    
    body: 写入附件的内容
    name: 附件的标题
    allure: 
        1. allure.attachment_type.TEXT
        2. allure.attachment_type.PNG
        3. allure.attachment_type.HTML
        
        
    @allure.attach.file(source, name, attachment, extension)
    source: 写入附件的文件路径
    
    
####allure.description 测试内容描述
    ```
    @allure.description("""描述内容"""")
    def text_xxx()
    
    
    
    或者
    def test_xxx():
        """
        xxxxx
        """
        
    动态更新
    @allure.dynamic.description("xxxxxxx)
    最后内容描述显示动态更新的内容
    
    
####allure.title  测试标题
    ```
    @allure.title("标题名称")
    def test_xxx()
    
    
    参数化标题名称  需要结合@pytest.make.parametrize("var1, var2", [value1, value2])
    @allure.title({var1}, {var2})
    @pytest.make.parametrize("var1, var2", [value1, value2])
    def test_title(var1, var2):
        pass
    
    例子：
    @allure.title("Parameterized test title: adding {param1} with {param2}")
    @pytest.mark.parametrize('param1,param2,expected', [(2, 2, 4),(1, 2, 5)])
    def test_with_parameterized_title(param1, param2, expected):
        assert param1 + param2 == expected
        
    动态更新测试标题
    @allure.title("开始计算")
    def test_title():
        assert 5 + 5 == 10
        allure.dynamic.title("计算结束")
        
        
####allure.link 测试连接
    ```
    allure.link("网址连接", name=None)
    例子：
    @allure.link("https://github.com/")
    def test_link():
        pass
        
    allure.link("网址连接"， name="链接名称")
    例子：
    @allure.link("http://github.com/", name="github")   
    def test_link():
        pass
        
    @allure.issue("网址连接"， name="链接名称")  提供带小图标的错误链接
    @allure.testcase("网址连接"， name="链接名称")
    
    
####BDD标记
    ```
    @allure.feature
    @allure.story
    
    
    allure.severity 安全级别的标记：
    1. @allure.severity(allure.severity_level.TRIVIAL)   不重要的
    2. @allure.severity(allure.severity_level.NORMAL)    正常的
    3. @allure.severity(allure.severity_level.CRITICAL)  重要的
    
    @allure.severity可以作用于函数，方法或者类
    通过将--allure-severities命令行选项与以逗号分隔的严重性级别列表结合使用，将仅运行具有相应严重性的测试
    pytest tests.py --allure-severities normal,critical
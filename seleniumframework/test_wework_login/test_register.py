from wenjian_auto_testing.seleniumframework.test_wework_login.index import Index


class TestRigister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        result = self.index.goto_register().register()
        assert result
import allure

class Test_Abc:
    @allure.step(title="这是第一个步骤----->test_a")
    def test_a(self):
        print("----->test_a")
        assert True
    @allure.step(title="这是第二个步骤----->test_b")
    def test_b(self):
        print("----->test_b")
        assert True
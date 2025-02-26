import pytest

class BD_Test_Demo1(object):

    version = 25
    @pytest.mark.run(order=1002)
    def test_method1(self):
        """测试函数1"""
        print("This is a test METHOD 1-1 - 002")

    @pytest.mark.skipif(version > 20, reason="skipped as version is less than 25")
    @pytest.mark.run(order=1004)
    def test_method2(self):
        """测试函数2"""
        print("This is a test METHOD 1-2 - 004")


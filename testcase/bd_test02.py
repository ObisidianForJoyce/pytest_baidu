import pytest

class BD_Test_Demo2(object):


    @pytest.mark.run(order=1001)
    @pytest.mark.parametrize('name, age',[("xiaoming",18),('xiaohong',55)])
    def test_method21(self, name, age):
        """测试函数1"""
        print("This is a test METHOD 2-1 - 001, 多个参数化传入测试: name is ",name,"age is ",age)
        assert age > 60

    @pytest.mark.run(order=1003)
    def test_method22(self):
        """测试函数2"""
        print("This is a test METHOD 2-2 - 003")
        print("error:", 1/0)

    @pytest.mark.run(order=1005)
    @pytest.mark.parametrize('name',['xiaoming','xiaohong'])
    def test_method23(self, name):
        """测试函数2"""
        print("This is a test METHOD 2-3 - 005, 参数传入测试", name)
        assert "xiao" in name


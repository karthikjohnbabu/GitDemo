import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print(" I will execute steps in fixtureDemo method") #used to set the prerequiste

    def test_fixtureDemo1(self):
        print(" I will execute steps in fixtureDemo1 method") #used to set the prerequiste

    def test_fixtureDemo2(self):
        print(" I will execute steps in fixtureDemo2 method") #used to set the prerequiste

    def test_fixtureDemo3(self):
        print(" I will execute steps in fixtureDemo3 method") #used to set the prerequiste
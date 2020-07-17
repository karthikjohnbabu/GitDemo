#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only.
#method name should have sense.
# -k stands for method names execution, -s stands for logs in output. -v stands for more info metadata.
#you can run specific filw with py.test <filename>
#you can mark (tag) tests "@pytest.mark.smoke" and then run with -m
#@pytest.mark.xfail #(this particular test case will run, but it will not report pass or fail in the command prompt)
#fixtures are used as setup and tear down methods for test cases
#Conftest file to generalize fixture and make it available to all test cases.

#Data driver parameterization can be done with rturn statements in tuple format
#when you define fixture scope to class only, it will run once before the class in initiated and at the end
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail #(this particular test case will run, but it will not report pass or fail in the command prompt)
def test_greetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

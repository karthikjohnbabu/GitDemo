import pytest


@pytest.fixture(scope="class")

def setup():
    print(" I will be executed first") #used to invoke the browsers
    yield
    print("I will be executed last") # used to close the browser and cookies

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "shetty", "Rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome","rahul", "shetty" ),("Firefox","Shetty"),("IE", "SS")])
def crossBrowser(request):
    return request.param

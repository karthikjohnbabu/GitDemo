#classes are user defined blue print or prototype.
#class will have methods, class variables, instance variable, constructor objects.
#constructor is one method which is called when we create an object
#Self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object


class Calculator:
    num = 100 #class variables
    #default constructor
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber =b
        print("Am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj= Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator (4,5)
obj1.getData()
print(obj1.num)

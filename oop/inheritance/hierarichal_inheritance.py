class parent:
    def function1(self):
        print("inside parent class")
class child1(parent):
    def function2(self):
        print("inside 1st child class")
class child2(parent):
    def function3(self):
        print("inside 2nd child class")
class child3(parent):
    def function3(self):
        print("inside 3rd child class")
obj1=child1()
obj1.function1()
obj1.function2()

obj2=child2()
obj2.function1()
obj2.function3()

obj3=child3()
obj3.function1()
obj3.function3()
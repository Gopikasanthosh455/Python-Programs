class parent1:
    def functon1(self):
        print("inside 1st parent1 class")
class parent2:
    def function2(self):
        print("inside 2nd parent class")
class child(parent2,parent1):
    def function3(self):
        print("inside child class")
obj=child()
obj.functon1()
obj.function2()
obj.function3()
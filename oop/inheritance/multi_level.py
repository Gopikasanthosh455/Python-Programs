class A:
    def function1(self):
        print("inside A class")
class B(A):
    def function2(self):
        print("inside B class")
class C(B):
    def function3(self):
        print("inside C class")

obj2=C()
obj2.function3()
obj2.function2()
obj2.function1()
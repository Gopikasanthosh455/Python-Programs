class demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name :",self.name)
        print("age :",self.age)
obj = demo("aswin",21)
obj.display()
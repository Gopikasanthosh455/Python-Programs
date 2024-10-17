class demo:
    def __init__(self):
        self.name=""
        self.age=""
        self.place=""
    def data(self):
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.place=input("Enter your place:")
    def display(self):
        print("name  :",self.name)
        print("age  :",self.age)
        print("place  :",self.place)
obj=demo()
obj.data()
obj.display()
class student:
    def __init__(self,name,place,age,course,mobile):
        self.name=name
        self.place=place
        self.age=age
        self.course=course
        self.mobile=mobile
    def display(self):
        print("------Student Details------ ")
        print("Name :",self.name)
        print("place :",self.place)
        print("age :",self.age)
        print("course :",self.course)
        print("mobile :",self.mobile)
obj = student("Gopika","guruvayoor",21,"python",77365777066)
obj.display()
class student:
    def __init__(self):
        self.name=""
        self.age=""
        self.place=""
    def student_data(self):
        print("-----Register new student-----")
        self.name=input("Enter ur name:")
        self.age=int(input("Enter ur age:"))
        self.place=input("Enter ur place:")
    def display(self):
        print("-----student details-----")
        print("Name   :",self.name)
        print("Age    :",self.age)
        print("Place  :",self.place)
obj=student()
obj.student_data()
obj.display()
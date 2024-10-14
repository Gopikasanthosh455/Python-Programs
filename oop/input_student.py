class student:
    def __init__(self):
        self.name=""
        self.department=""
        self.college=""
    def student(self):
        self.name=input("Enter ur name:")
        self.department=input("Enter department:")
        self.college=input("Enter ur college name:")
    def dispaly(self):
        print("-----student details------")
        print("name :",self.name)
        print("department :",self.department)
        print("college :",self.college)
obj=student()
obj.student()
obj.dispaly()
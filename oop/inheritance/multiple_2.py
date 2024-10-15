class person:
    def __init__(self):
        self.name=""
        self.age=""
    def person_data(self):
        print("----ENTER PERSON DETAILS----")
        self.name=input("Enter name      :")
        self.age=int(input("Enter age    :"))
    def person_details(self):
        print("---- PERSON DETAILS ----")
        print(" Name          :",self.name)
        print(" Age          :",self.age)
class company:
    def __init__(self):
        self.company_name=""
        self.company_place=""
        self.company_mobile=""
    def company_data(self):
        print("----ENTER COMPANY DETAILS----")
        self.company_name=input("Enter company Name                     :")
        self.company_place=input("Enter company location                :")
        self.company_mobile=int(input("Enter company contact number     :"))
    def company_details(self):
        print("----COMPANY DETAILS----")
        print("Company Name                 :",self.company_name)
        print("Company location             :",self.company_place)
        print("Company contact number       :",self.company_mobile)
class employee(person,company):
    def __init__(self):
        self.designation=""
        self.salary=""
        self.skill=""
    def employee_data(self):
        print("----ENTER EMPLOYEE DETAILS----")
        self.designation=input("Enter designation      :")
        self.salary=int(input("Enter salary            :"))
        self.skill=input("Enter skill                 :")
    def employee_details(self):
        print("----EMPLOYEE DETAILS----")
        print(" Designation    :",self.designation)
        print(" Salary         :",self.salary)
        print(" Skills         :",self.skill)
obj=employee()
obj.person_data()
obj.company_data()
obj.employee_data()
obj.person_details()
obj.company_details()
obj.employee_details()


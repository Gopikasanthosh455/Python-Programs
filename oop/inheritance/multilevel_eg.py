class college:
    def __init__(self):
        self.college_name=""
        self.college_loction=""
        self.college_number=""
    def college_data(self):
        print("--ENTER COLLEGE DETAILS--")
        self.college_name=input("Enter college name:")
        self.college_loction=input("Enter college location:")
        self.college_number=int(input("Enter college contact number:"))
    def college_details(self):
        print("----COLLEGE DETAILS----")
        print("collage name            :",self.college_name)
        print("collage location        :",self.college_loction)
        print("collage contact number  :",self.college_number)
class department(college):
    def __init__(self):
        self.dept_name=""
        self.dept_hod=""
        self.dept_sem=""
    def department_data(self):
        print("--ENTER DEPARTMENT DETAILS--")
        self.dept_name = input("Enter department name:")
        self.dept_hod = input("Enter department hod name:")
        self.dept_id = input("Enter department id:")
    def department_details(self):
        print("----DEPARTMENT DETAILS----")
        print("Department id          :",self.dept_id)
        print("Department Name        :",self.dept_name)
        print("Department HOD Name    :",self.dept_hod)
class student(department):
    def __init__(self):
        self.student_name=""
        self.student_age=""
        self.student_mobile=""
    def student_data(self):
        print("--ENTER STUDENT DETAILS--")
        self.student_name = input("Enter student Name:")
        self.student_age = int(input("Enter student age:"))
        self.student_mobile = int(input("Enter student contact number:"))
    def student_details(self):
        print("----STUDENT DETAILS----")
        print("Student name              :",self.student_name)
        print("Student age               :",self.student_age)
        print("Student contact number    :",self.student_mobile)
obj=student()
obj.college_data()
obj.department_data()
obj.student_data()
obj.college_details()
obj.department_details()
obj.student_details()

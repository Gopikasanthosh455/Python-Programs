class hospital:
    def __int__(self):
        self.h_name=""
        self.h_place=""
        self.h_mobile=""
    def hospital_data(self):
        print("----ENTER HOSPITAL DETAILS----")
        self.h_name=input("Enter hospital Name         :")
        self.h_place=input("Enter hospital location    :")
        self.h_mobile=int(input("Enter contact number  :"))
    def hospital_details(self):
        print("----HOSPITAL DETAILS----")
        print("Hospital name           :",self.h_name)
        print("Hospital place          :",self.h_place)
        print("Hospital contact number :",self.h_mobile)
class department(hospital):
    def __init__(self):
        self.dept_id=""
        self.dept_name=""
        self.dept_beds=""
    def department_data(self):
        obj.hospital_data()
        print("----ENTER DEPARTMENT DETAILS----")
        self.dept_id=int(input("Enter department id     :"))
        self.dept_name=input("Enter department name     :")
        self.dept_beds=int(input("Enter number of beds  :"))
    def department_details(self):
        obj.hospital_details()
        print("----DEPARTMENT DETAILS----")
        print("Department id   :",self.dept_id)
        print("Department name :",self.dept_name)
        print("Number of beds  :",self.dept_beds)
class patient(department):
    def __init__(self):
        self.p_name=""
        self.p_place=""
        self.p_age=""
        self.p_mobile=""
    def patient_data(self):
        obj.department_data()
        print("----ENTER PATIENT DETAILS----")
        self.p_name=input("Enter patient name                    :")
        self.p_place=input("Enter patient location               :")
        self.p_age=int(input("Enter patient age                :"))
        self.p_mobile=int(input("Enter patient contact number  :"))
    def patient_details(self):
        obj.department_details()
        print("----PATIENT DETAILS----")
        print("Patient name          :",self.p_name)
        print("Patient age           :",self.p_age)
        print("Patient location      :",self.p_place)
        print("Patient contact number:",self.p_mobile)
obj=patient()
obj.patient_data()
obj.patient_details()

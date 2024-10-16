class teacher:
    def myfunction(self):
        print("inside class teacher")
    def newfunction(self):
        print("Example for method overriding...!")
class student(teacher):
    def student_function(self):
        print("inside class student")
    def myfunction(self): # Overriding the 'myfunction' method from the base class 'teacher'
        print("Welcome....!")# This will replace the behavior of 'myfunction' in the base class
obj=student()
obj.myfunction()# Calling the overridden 'myfunction' method. It calls the version in 'student', not in 'teacher'
obj.student_function()
obj.newfunction()
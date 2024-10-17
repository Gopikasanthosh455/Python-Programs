class student:
    __name=""
    __course=""
    __place=""
    def __init__(self,name,course,place):
        self.__name=name
        self.__course=course
        self.__place=place
    def __display(self):
        print("Name :",self.__name)
        print("course :",self.__course)
        print("place :",self.__place)
    def access_private_function(self):
        self.__display()
obj=student("Gopika","python","guruvayoor")
obj.access_private_function()

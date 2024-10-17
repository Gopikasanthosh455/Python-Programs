class college:
    __college_name=""
    __college_place=""
    __college_mobile=""
    __college_email=""
    def __init__(self,name,place,mobile,email):
        self.__college_name=name
        self.__college_place=place
        self.__college_mobile=mobile
        self.__college_email=email
    def __display(self):
        print("college name :",self.__college_name)
        print("college place :",self.__college_place)
        print("college mobile :",self.__college_mobile)
        print("college email :",self.__college_email)
    def access_private_function(self):
        self.__display()
obj=college("GEC PALAKKAD","SREEKRISHNAPURAM",7736577066,"gecskp@gmail.com")
obj.access_private_function()
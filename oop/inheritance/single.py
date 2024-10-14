class myclass:
    def myfunction(self):
        print("inside myclass")
class newclass(myclass):
    def newfunction(self):
        print("inside new class")
obj =myclass()
obj.myfunction()

obj1=newclass()
obj1.myfunction()
obj1.newfunction()

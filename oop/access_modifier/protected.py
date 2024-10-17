class myclass:
    _name=""
    _age=""
    _place=""
    def __init__(self,name,age,place):
        self._name=name
        self._age=age
        self._place=place
    def _display(self):
        print("Name :",self._name)
        print("age :",self._age)
class newclass(myclass):
    def __init__(self,name,age,place):
        myclass.__init__(self,name,age,place)
    def displaydata(self):
        print("place :", self._place)
        self._display()
obj=newclass("Gopika",21,"guruvayoor")
obj.displaydata()


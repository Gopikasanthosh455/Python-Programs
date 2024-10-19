class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of a circle is :",3.14*(self.radius**2))
    def perimeter(self):
        print("perimeter of a circle is :",2*3.14*self.radius)
obj = circle(5)
obj.area()
obj.perimeter()
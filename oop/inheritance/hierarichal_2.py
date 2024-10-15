class vehicle:
    def __init__(self):
        self.make=""
        self.model=""
        self.year=""
    def vehicle_data(self):
        print("----ENTER VEHICLE DETAILS----")
        self.make=input("Enter make:")
        self.model=input("Enter model:")
        self.year=int(input("Enter year:"))
    def vehicle_details(self):
        print("----VEHICLE DETAILS----")
        print(" MAKE :",self.make)
        print(" MODEL :",self.model)
        print(" YEAR :",self.year)
class car(vehicle):
    def __init__(self):
        self.car_color=""
        self.car_wheels=""
        self.car_door=""
    def car_data(self):
        print("----ENTER CAR DETAILS----")
        self.car_color=input("Enter the color:")
        self.car_wheels=int(input("Enter the number of wheels:"))
        self.car_door=int(input("Enter the number of doors:"))
    def car_details(self):
        print("----CAR DETAILS----")
        print("color:",self.car_color)
        print("number of wheels:",self.car_wheels)
        print("number of door:",self.car_door)
class bike(vehicle):
    def __init__(self):
        self.bike_color = ""
        self.bike_wheels = ""
        self.bike_type = ""

    def bike_data(self):
        print("----ENTER BIKE DETAILS----")
        self.bike_color = input("Enter the color:")
        self.bike_wheels = int(input("Enter the number of wheels:"))
        self.bike_type = input("Enter the type:")

    def bike_details(self):
        print("----BIKE DETAILS----")
        print("color:", self.bike_color)
        print("number of wheels:", self.bike_wheels)
        print("Type:", self.bike_type)
class bus(vehicle):
    def __init__(self):
        self.bus_color = ""
        self.bus_wheels = ""
        self.bus_door = ""

    def bus_data(self):
        print("----ENTER BUS DETAILS----")
        self.bus_color = input("Enter the color:")
        self.bus_wheels = int(input("Enter the number of wheels:"))
        self.bus_door = int(input("Enter the number of doors:"))

    def bus_details(self):
        print("----BUS DETAILS----")
        print("color:", self.bus_color)
        print("number of wheels:", self.bus_wheels)
        print("number of door:", self.bus_door)
obj1=car()
obj1.vehicle_data()
obj1.car_data()
obj1.vehicle_details()
obj1.car_details()

obj2=bike()
obj2.vehicle_data()
obj2.bike_data()
obj2.vehicle_details()
obj2.bike_details()

obj3=bus()
obj3.vehicle_data()
obj3.bus_data()
obj3.vehicle_details()
obj3.bus_details()

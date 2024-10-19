from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def age(self):
        today = datetime.now()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def display_age(self):
        print("Name             :", self.name)
        print("Country          :", self.country)
        print("Date of birth    :", self.date_of_birth.strftime("%Y-%m-%d"))
        print("Age              :", self.age())
        
obj = Person("Gopika", "India", "2003-05-18")
obj.display_age()

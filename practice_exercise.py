class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(self.make)
        print(self.model)
        print(self.year)

my_car = Car('Suzuki', 'Swift', 2007)
my_car.display_info()

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def user_info(self):
        print(self.name)
        print(self.age)
user = User('Pubudu Piyumal', 27)
user.user_info()

class Animal:
    def __init__(self, breed_1, breed_2):
        self.breed_1 = breed_1
        self.breed_2 = breed_2
    
    def breed_info(self):
        print(self.breed_1)
        print(self.breed_2)
animal = Animal('Dog', 'Cat')
animal.breed_info()

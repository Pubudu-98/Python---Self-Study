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
        return f"Breed Category: {self.breed_1} | Breed Category: {self.breed_2}"
animal = Animal('Dog', 'Cat')
print(animal.breed_info())

class Module:
    def __init__(self, module_name, module_id):
        self.module_name = module_name
        self.module_id = module_id

    def module_info(self):
        return f"Module Name: {self.module_name} | Module ID: {self.module_id}"
module = Module('Python', 'CS001')
print(module.module_info())
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
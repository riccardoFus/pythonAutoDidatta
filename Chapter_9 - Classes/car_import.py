# from car_module import Car
# from car_module import ElectricCar
# from car_module import Car, ElectricCar
# import car_module
from car_module import *

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('testa', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, odometer_reading):
        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading
        else:
            print(f"You can't roll back odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"I'm filling the gas tank")

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")
        
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# method 1 to change attribute value: directly
my_new_car.odometer_reading = 1222
# method 2 to change attribute value: method
my_new_car.update_odometer(423423)
my_new_car.increment_odometer(42342342)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_new_car.fill_gas_tank()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
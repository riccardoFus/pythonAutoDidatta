cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')
print(car == "Audi")
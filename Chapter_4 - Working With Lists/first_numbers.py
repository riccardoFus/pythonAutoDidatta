for value in range(1, 5):
    print(value)

print("\n")

for value in range(1, 6):
    print(value)

print("\n") 

for value in range(0, 6):
    print(value)

numbers = list(range(0, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    squares.append(value**2)

print(squares)

print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))

#list comprehension
squares = [value**2 for value in range(2, 11)]
print(squares)

for value in range(1, 21):
    print(value)

million_numbers = [value for value in range(1, 10000001)]

# for value in million_numbers:
#     print(value)

print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

odd_numbers = [value for value in range(1, 21, 2)]

for value in odd_numbers:
    print(value)

multiple_of_three = [value for value in range(3, 31, 3)]

for value in multiple_of_three:
    print(value)

first_ten_cubes = [value**3 for value in range(1, 11)]

for value in first_ten_cubes:
    print(value)
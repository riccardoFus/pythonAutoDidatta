number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    result = 'even'
else:
    result = 'odd'

print(f"\nThe number {number} is {result}")

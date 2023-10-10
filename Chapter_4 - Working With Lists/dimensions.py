dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 -> ERRORE: tuple sono IMMUTABILI

my_t = (3,) # with only one value

print("Original dimension")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions: 
    print(dimension)
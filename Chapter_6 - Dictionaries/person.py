person = {'first_name' : 'Riccardo', 'last_name' : 'Fusiello', 'age' : 20, 'city' : 'Andria'}
print(f"First name is : {person['first_name']}\nLast name is : {person['last_name']}\nAge is : {person['age']}\nCity is : {person['city']}")

favorite_numbers = {
    'riccardo' : 25,
    'michele' : 18,
    'antonio' : 17
}
print(favorite_numbers['riccardo'])
print(favorite_numbers['michele'])
print(favorite_numbers['antonio'])

favorite_numbers = {
    'riccardo' : [25, 26, 27],
    'michele' : [12, 13, 543],
    'antonio' : [324, 32, 4234]
}

for person, fav in favorite_numbers.items():
    print(f"\nFavorite numbers of {person.title()} are:")
    for num in fav:
        print(f"\t{num}")

rivers = {
    'nile' : 'egypt',
    'gange' : 'india',
    'mississippi' : 'usa'
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

for river in rivers:
    print(river)

for country in set(rivers.values()):
    print(country)
def define_city(city_name, country_name, population=""):
    if population:
        city = f"{city_name}, {country_name} - {population}"
    else:
        city = f"{city_name}, {country_name}"
    return city.title()
def make_car(manufacturer, model_name, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking the {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t{topping}")
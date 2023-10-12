def describe_pet(animal_type, pet_name):
    """Display info about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def describe_pet_default(pet_name, animal_type = 'dog'):
    """Display info about pet with default animal_type"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry') # keyword arguments
describe_pet_default(pet_name='willie')
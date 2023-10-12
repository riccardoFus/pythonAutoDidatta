def print_models(unprinted_design, completed_models):
    # simulate printing each design, until none are left
    # move each design to completed_models after printing
    while unprinted_design:
        print("Printing design ...")
        current_design = unprinted_design.pop()
        print(f"Printed: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# start with some designs that need to be printed
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_design[:], completed_models)
print(unprinted_design)
show_completed_models(completed_models)
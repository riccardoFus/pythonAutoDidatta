def make_sandwich(*args):
    print("\nMaking a sandwich with:")
    for arg in args:
        print(f"\t{arg}")

make_sandwich('ketchup', 'salad', 'mayonaise')
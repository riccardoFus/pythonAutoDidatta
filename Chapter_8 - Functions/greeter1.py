def greet_user1():
    """Display a simple greeting.""" #docstring
    print("Hello!")

def greet_user2(username):
    """Display a simple greeting with username."""
    print(f"Hello, {username.title()}!")

greet_user1()
greet_user2('jane')
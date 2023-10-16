import json
filename = 'text_files/username.json'

def get_stored_username():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def store_username():
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}")

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        store_username()
        

greet_user()

# username = input("What is your name? ")

#filename = 'text_files/username.json'

# with open(filename, 'w') as f:
#    json.dump(username, f)
#    print(f"We'll remember you when you're back, {username}!")


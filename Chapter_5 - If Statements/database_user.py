usernames = ['user1', 'user2', 'user3', 'user4', 'admin']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")
else:
    print("We need to find some users!")

current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user6', 'User1']
if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print("You need to enter a new username")
        else:
            print("Your username is available")
else:
    print("There are no new users")

ordinals = [value for value in range(1, 10)]
if ordinals:
    for ordinal in ordinals:
        if ordinal == 1:
            print(f"{ordinal}st")
        elif ordinal == 2:
            print(f"{ordinal}nd")
        elif ordinal == 3:
            print(f"{ordinal}rd")
        else:
            print(f"{ordinal}th")
else:
    print("Empty list")
class User:
    def __init__(self, first, last, age, city):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"These are the attributes of this user:")
        print(f"First Name = {self.first_name}")
        print(f"Last Name = {self.last_name}")
        print(f"Age = {self.age}")
        print(f"City = {self.city}")
        print(f"Login attempts = {self.login_attempts}\n")

    def greet_user(self):
        print(f"Hi, dear {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("These are the privileges of the administrator:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")
        

class Admin(User):
    def __init__(self, first, last, age, city):
        super().__init__(first, last, age, city)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
        

user1 = User('Riccardo', 'Fusiello', 20, 'Andria')

user1.describe_user()

user1.greet_user()

user1.increment_login_attempts()
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()

admin = Admin('Michele', 'Matera', 21, 'Andria')
admin.privileges.show_privileges()
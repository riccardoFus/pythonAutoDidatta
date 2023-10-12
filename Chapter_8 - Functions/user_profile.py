def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

# *args, **kwargs

user_profile = build_profile('riccardo', 'fusiello', location = 'andria', passion = 'computer science', phone = '+39 123-456-7890')
print(user_profile)
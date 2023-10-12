responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response
    
    #find out if anyone else is going to take a poll
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete - show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
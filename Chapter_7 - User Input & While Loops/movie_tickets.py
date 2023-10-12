prompt = "\nHow old are you? (Enter 'quit' to stop insert data) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            ticket = 0
        elif age < 12:
            ticket = 10
        else:
            ticket = 15
        print(f"\nThe cost of your movie ticket is ${ticket}")

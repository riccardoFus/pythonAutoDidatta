guests = ['Kendrick Lamar', 'Beyonce', 'Steven Basalari']
print(f"You're welcome to my party, dear {guests[0].title()}!")
print(f"You're welcome to my party, dear {guests[1].title()}!")
print(f"You're welcome to my party, dear {guests[2].title()}!")
print(f"Oh, {guests[2]} can't make the party!")
guests[2] = 'Micheal Jackson'
print(f"You're welcome to my party, dear {guests[0].title()}!")
print(f"You're welcome to my party, dear {guests[1].title()}!")
print(f"You're welcome to my party, dear {guests[2].title()}!")

guests.insert(0, 'Favij')
guests.insert(2, 'Michele Misseri')
guests.append('Leonardo Addati')
print(f"You're welcome to my party, dear {guests[0].title()}!")
print(f"You're welcome to my party, dear {guests[1].title()}!")
print(f"You're welcome to my party, dear {guests[2].title()}!")
print(f"You're welcome to my party, dear {guests[3].title()}!")
print(f"You're welcome to my party, dear {guests[4].title()}!")
print(f"You're welcome to my party, dear {guests[5].title()}!")

print('Ops... I can invite only two person :(')
print(f"Sorry but I can't invite {guests.pop()}")
print(f"Sorry but I can't invite {guests.pop()}")
print(f"Sorry but I can't invite {guests.pop()}")
print(f"Sorry but I can't invite {guests.pop()}")
print(f"You're welcome to my party, dear {guests[0].title()}!")
print(f"You're welcome to my party, dear {guests[1].title()}!")

del guests[1]
del guests[0]

print(guests)
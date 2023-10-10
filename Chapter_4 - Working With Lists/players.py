players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # 0, 1, 2
print(players[1:4])
print(players[:4]) # 0, 1, 2, 3
print(players[2:]) # 2, 3, 4, ...

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
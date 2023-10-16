from random import randint
class Dice:
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        return randint(1, self.sides)
    
class Dice_Ten(Dice):
    def __init__(self):
        self.sides = 10

    def roll_die(self):
        return randint(1, self.sides)
    
class Dice_Twenty(Dice):
    def __init__(self):
        self.sides = 20

    def roll_die(self):
        return randint(1, self.sides)
    
i = 0
normal_dice = Dice()
ten_sides_dice = Dice_Ten()
twenty_sides_dice = Dice_Twenty()

while i < 10:
    print(f"Normal dice : {normal_dice.roll_die()}")
    print(f"Ten-Sides dice : {ten_sides_dice.roll_die()}")
    print(f"Twenty-Sides dice : {twenty_sides_dice.roll_die()}\n")
    i += 1


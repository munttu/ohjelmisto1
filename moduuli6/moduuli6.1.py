import random
rolls=random.randint(1,6)
def dice_roll():
    rolls=random.randint(1,6)
    print(rolls)
    return rolls

while rolls!=6:
    rolls=dice_roll()
else:
    print(rolls)

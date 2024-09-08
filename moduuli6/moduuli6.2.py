import random
dice=int(input("enter any number: "))
roll=0
def dice_roll(b):
    rolls=random.randint(1,b)
    print(rolls)
    return rolls
while roll!=dice:
    roll=dice_roll(dice)
else:
    print(roll)
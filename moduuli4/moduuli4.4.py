import random
guess1 = random.randint(1,10)
guess2= int(input("Guess a number between 1 and 10: "))
while guess1!=guess2 :
    if guess1>guess2:
        print("too low")
    elif guess1<guess2:
        print("too high")
    guess2 = int(input("Guess a number between 1 and 10: "))
print("Correct")
import random, math
amount=0
rolls=int(input("how many dice rolls do you want? "))


for i in range(0,rolls):
    amount+= random.randint(1,6)

print(amount)

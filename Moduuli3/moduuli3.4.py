import math
vuos= int(input("mikä vuosiluku?: "))
if vuos%4==0:
    if vuos%100==0:
        if vuos%400==0:
            print("tämä on hyppyvuosi")
        else :print ("tämä ei ole hyppyvuosi")
    else: print("tämä on hyppyvuosi")
else :print("tämä ei ole hyppyvuosi")


import math
LEIVISKA = float (input  ("anna leiviskät: ") )
NAULAT = float (input ("anna naulat: "))
LUODIT= float( input("anna luodit: "))
KAIKKINAULAT = NAULAT + LEIVISKA*20
KAIKKILUODIT = LUODIT + KAIKKINAULAT*32
KILOGRAMMAMUUT=KAIKKILUODIT * 13.3/1000
print("Kilogrammoina: ",KILOGRAMMAMUUT/1000, "Grammoina: ",KILOGRAMMAMUUT)







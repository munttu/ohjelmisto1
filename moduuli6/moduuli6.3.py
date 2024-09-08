def convert(gal):
    gas_lit =gal*3.78541
    return gas_lit

gas = int(input("Insert gas volume in gallons: "))

while gas>0:
    print(convert(gas))
    gas = int(input("Insert gas volume in gallons: "))



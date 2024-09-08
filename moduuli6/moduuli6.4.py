def sum_list(numerot):
    return sum(numerot)


def main():
    num= []
    luku1=int(input("anna alkuluku: "))
    luku2=int(input("anna alkuluku: "))
    num.append(luku1)
    num.append(luku2)

    summa = sum_list(num)

    print(f"listan lukujen summa on: {summa}")

main()
kokonaisluku=int(input("anna kokonaisluku:"))
if kokonaisluku>1:
    for i in range(2,(kokonaisluku//2)+1):
        if (kokonaisluku%i)==0:
            print(kokonaisluku,"is not a prime number")
            break

    else:
        print(kokonaisluku,"is a prime number")

else:
    print(kokonaisluku,"ei ole alkuluku")
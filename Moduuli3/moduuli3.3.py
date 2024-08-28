sukupuoli= input("anna biologinen sukupuoli mies tai nainen: ")

hemoglob= int(input("anna biologinen hemoglobiiniarvo: "))

if sukupuoli=="mies":
    if hemoglob<134:
        print("alhainen hemoglobiiniarvo")
    elif hemoglob >134 and hemoglob <195:
        print("hemoglobiiniarvo on normaali")
    else:
        print("hemoglobiiniarvo on korkea")

if sukupuoli== "nainen":
    if hemoglob<117:
        print("alhainen hemoglobiiniarvo")
    elif hemoglob >117 and hemoglob<175:
        print("hemoglobiiniarvo on normaali")
    else:
        print("hemoglobiiniarvo on korkea")
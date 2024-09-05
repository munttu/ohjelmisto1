nums = []

while True :
    num = (input("anna luku?(tyhjä väli lopettaa) "))
    if num=="":
        break
    nums.append(int(num))

nums.sort(reverse=True)
print("viisi suurinta lukua:", nums[:5])


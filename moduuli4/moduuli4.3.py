number=float(input("Enter a number: "))
maxnum=minnum=number

while number:
    if float(number)>float(maxnum):
        maxnum=number
    elif float(number)<float(minnum):
        minnum=number
    number=input("Enter a number: ")
    if not number:
        print("maxnum: ",maxnum,"minnum: ",minnum)
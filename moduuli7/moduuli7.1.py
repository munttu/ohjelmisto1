months=("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
order= int(input("anna kuukauden numero 1-12: "))
months_name= months[order-1]
if order==12 or order==1 or  order==2:
    print(f" {order} on {months_name} ja vuoden aika on talvi.")
elif order==3 or order==4 or order==5:
    print(f"the {order} on {months_name} ja vuoden aika on kevät.")
elif order==6 or order==7 or order==8:
    print(f"the {order} on {months_name} ja vuoden aika on kesä")
else:
    print(f"{order} on {months_name} ja vuoden aika on syksy")

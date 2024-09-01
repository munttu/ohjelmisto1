from Tools.scripts.mailerdaemon import emparse_list_from

user='python'
password='rules'
maxattemps=5
attemps=0
while maxattemps>attemps:
   user=input("enter username: ")
   password=input("enter password: ")
   if user=='python' and password=='rules':
       print("welcome")
       break
   else:
    attemps+=1
else:print("access denied")


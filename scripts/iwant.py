#I want to go travling to france,and I want to choose a city to go

#i create a selection to see which city I would go
T = int(input("how many degree of that city"))
time = float(input("how many hours for getting there"))
if T > 23 :
    print("the temperature looks fine,but how long for getting there?")
   
elif time > 12:
    print("too long to go")
else:

    print("yes plesase go there")

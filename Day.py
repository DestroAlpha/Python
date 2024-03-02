a=eval(input("Enter the no. of day"))
day=["Sunday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
sport=["Cricket","Football","Volleyball","Basketball","Kabbadi"]
b="It's boring day"
if a==1:
    print(day[0],b)
elif a==2:
    print(day[1]," ","game to be played",sport[0])
elif a==3:
    print(day[2]," ","game to be played",sport[1])
elif a==4:
    print(day[3]," ","game to be played",sport[2])
elif a==5:
    print(day[4]," ","game to be played",sport[3])
elif a==6:
    print(day[5]," ","game to be played",sport[4])
elif a==7:
    print(day[6],b)

else:
    print("Invalid input")

    

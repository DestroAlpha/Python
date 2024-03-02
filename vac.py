name=['Boring day','Cricket','Football','Chess','Kabbadi','Basketball']
a=eval(input('Enter the no. of days between (1 to 7)'))
if a==1:
    print("Sunday",name[a-1])
elif a==2:
    print("Monday",name[a-1])
elif a==3:
    print("Tuesday",name[a-1])
elif a==4:
    print("Wednesday",name[a-1])
elif a==5:
    print("Thursday",name[a-1])
elif a==6:
    print("Friday",name[a-1])
elif a==7:
    print("Saturday",name[a-7])
else:
    print("Invalid")

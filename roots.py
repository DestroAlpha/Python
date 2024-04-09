import math
import cmath
a=eval(input("Enter the value of cofficient of x**2:- "))
b=eval(input("Enter the value of cofficient of x:- "))
c=eval(input("Enter the constan value:- "))
def find_roots(a,b,c):
    roots=[]
    d=b**2-4*a*c
    if d>0:
        print("Roots are real and different")
        r1=(-b + math.sqrt(d))/2*a
        r2=(-b- math.sqrt(d))/2*a
        roots.append(r1)
        roots.append(r2)
    elif d<0:
        print("Roots are imginary and different")
        r1=(-b+ cmath.sqrt(d))/2*a
        r2=(-b- cmath.sqrt(d))/2*a
        roots.append(r1)
        roots.append(r2)
    elif d==0:
        print("Root are real and same")
        r=(-b)/(2*a)
        roots.append(r)
    print( f"The roots are {roots} " )
find_roots(a,b,c)

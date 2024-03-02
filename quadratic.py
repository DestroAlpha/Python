import math
import cmath
a=eval(input("Enter the cofficient of x**2:- "))
b=eval(input("Enter the cofficient of x:- "))
c=eval(input("Enter the constant value "))
def find_root(a,b,c):
    d=b**2-4*a*c
    roots=[]
    if d>0:
        print("The roots are real and different")
        r1=(-b+math.sqrt(d))/2*a
        r2=(-b-math.sqrt(d))/2*a
        roots.append(r1)
        roots.append(r2)
    elif d==0:
        print("The roots are real and equal")
        r=(-b)/(2*a)
        roots.append(r)
    elif d<0:
        print("The roots are different and imaginary")
        r1=(-b+cmath.sqrt(d))/2*a
        r2=(-b-cmath.sqrt(d))/2*a
        roots.append(r1)
        roots.append(r2)
    print(f"The roots of the equation are {roots}")
find_root(a,b,c)
        

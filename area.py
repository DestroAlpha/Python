import random as rand
import math
def randomnum():
    o=rand.randint(1,10)
    return o
def area():
    while True:
        print('''Shape is you want the area for random dimension
1. Triangle,2.Square,3.Rectangle,4.Circle''')
        shape=int(input("Enter the no. of shape assigne to figures:- "))
        if shape==1:
            print("You has chosen to find the area of Triangle")
            b=randomnum()
            h=randomnum()
            area=1/2*b*h
            print(f"Area of the triangle is {area}")
        elif shape==2:
            print("You has chosen to find the area of Square")
            l=randomnum()
            area=l**2
            print(f"Area of square is {area}")
        elif shape==3:
            print("You has chosen to find the area of Rectangle")
            l=randomnum()
            b=randomnum()
            area=l*b
            print("Area of rectangle is {area}")
        elif shape==4:
            print("You has chosen to find the area of circle")
            r=randomnum()
            area=math.pi*(r**2)
            print(f"Area of circle is {area}")
        else:
            print("Thank you")
            break
randomnum()
area()

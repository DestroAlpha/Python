import time
start=time.time()
a="Aim:-To display square root of input number by appling try and expection handling error\nand run time of the program"
def Detail():
    print(f"Name:-Vivek Raj\n Roll no.:-23/19045\n Bsc Physics(H)\n{a}")
Detail()
try:
    a=eval(input("Enter the number to find the squreroot. "))
    root=a**(1/2)
    print(roo)
except:
    print("Invalid Input")
end=time.time()
print(f"The excution time of the code is {end-start} seconds.")

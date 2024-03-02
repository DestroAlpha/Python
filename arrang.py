#Arrangement of 'm' red and 'n' blue balls
m=eval(input("Enter the no. of red balls:- "))
n=eval(input("Enter the no. of blue balls:- "))
if m<0 or n<0:
    print("Invalid Inputs")
else:
    def fact(N):
        sum1=1
        for i in range(1,(N+1)):
            sum1=sum1*i
        return sum1
    def arrangements(m,n):
        result=fact(m+n)/(fact(m)*fact(n))
        print(result)
    arrangements(m,n)

a="To find the factorial of 'N' number and arrange the red and blue balls using python"
m=eval(input("Enter the no. of red balls:- "))
n=eval(input("Enter the no.of blue balls:- "))
def factorial(N):
    sum1=1
    for i in range(1,(N+1)):
        sum1=sum1*i
    return sum1
if m<0 or n<0:
    print("Invalid inputs")
else:
    def count_permutation(m,n):
        result=(factorial(m+n))/(factorial(m)*factorial(n))
        print(result)
    count_permutation(m,n)
        

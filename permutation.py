def Mydetail():
    a="Aim:- To find the factorial of 'N' number and arrange the red ball and blue ball using python "
    print(f"Name:-Vivek Raj\n Roll no.:-23/19045\n Bsc Physics \n {a}")
Mydetail()
m=eval(input("Enter the no. of red balls "))
n=eval(input("Enter the no. of blue balls "))
if m<0 or n<0:
    print("Ïnvalid Input")
else:
    def factorial (N):
        result=1
        for i in range(1,N+1):
            result=result*i
        return result
    def count_permutation(m,n):
        result=(factorial(m+n))/(factorial(m)*factorial(n))
        print(result)
    count_permutation(m,n)


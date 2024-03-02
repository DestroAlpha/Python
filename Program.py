a=eval(input("Enter the number to find the factorial"))
def factorial():
    b=1
    for i in range(1,a+1):
        b=b*i
    print(b)
factorial()
def count_permutation():
    result=factorial()/(factorial()*factorial())
    print(result)
count_permutation()

def factorial (N):
    result=1
    for i in range(1,N+1):
        result=result*i
    return result
def count_permutation(m,n):
    result=factorial(m+n)/(factorial(m)*factorial(n))
    print(result)
count_permutation(8,9)

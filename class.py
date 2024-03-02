print("Vivek raj \n 23/19045\n Bsc Physic(H)")
a=eval(input("Enter a number"))
b=eval(input("Enter a number"))
class A1:
    def method1():
        print("Sum of 'a' and 'b'",a+b)
    def method2():
        print("Difference of 'a' and 'b'",a-b)
class A2(A1):
    def method3():
        print("Product of 'a' and 'b'",a*b)
    def method4():
        print("Division of 'a' and 'b'",a/b)
class A3(A2):
    def method5():
        print("'A' modulus 'B'",a%b)
    def method6():
        print("'A' power 'B'",pow(a,b))
x=A1
x.method1()
x.method2()
z=A2
z.method3()
z.method4()
c=A3
c.method5()
c.method6()

        

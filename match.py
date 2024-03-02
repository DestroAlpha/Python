num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
operater=input("Enter  number")
match operater:
    case "+":
        print("addition",num1+num2)
    case "-":
        print("Subtraction",num1-num2)
    case "/":
        print("Division",num1/num2)
    case "*":
        print("Multiplication",num1*num2)
##****************************************************************************************************##
import Arithmetic

def main():
    print("Function to print Addition, Subtraction, Multiplication, Division")

    print("Enter first number :")
    no1=int(input())

    print("Enter second number :")
    no2=int(input())

    add=Arithmetic.Add(no1,no2)
    sub=Arithmetic.Sub(no1,no2)
    mult=Arithmetic.Mult(no1,no2)
    div=Arithmetic.Div(no1,no2)

if __name__=="__main__":
    main()

""" Below code is stored in other python file named as 'Arithmetic' so imported in above code"""
def Add(num1,num2):
    num=num1+num2
    print("Addition of number is :", num)

def Sub(num1,num2):
    num=num1-num2
    print("Subtraction of number is :", num)

def Mult(num1,num2):
    num=num1*num2
    print("Multiplication of number is :", num)

def Div(num1,num2):
    num=num1/num2
    print("Division of number is :", num)
##****************************************************************************************************##
def star(num):
    for i in range(num):
        for j in range(num):
            print("*", end='  ')
        print()

def main():
    print("Function to print pattern star")
    no=int(input())
    star(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def factors(num):
    num2=1
    for i in range(1,num+1):
        num2=num2*i
    print("Factorial of number is :", num2)

def main():
    print("Addition of factors of an input number")
    no=int(input())
    fact=factors(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def AddFactors(no):
    num=0
    for i in range(1,no):
        if (no%i==0):
            num=num+i
    print("The addition of factors of a number is :", num)

def main():
    print("Function to display addition of factors of a number")
    no=int(input())
    fact=AddFactors(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def prime(no):
    if no>1:
        for i in range(2,no):
            if (no%i==0):
                print("No is not prime")
                break
        else:
            print("No is prime")
    else:
        print("No is not a prime")

def main():
    print("Function to display a number prime or not")
    no=int(input())
    pri=prime(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def starPattern(star):
    for i in range(star):
        for j in range(star,i,-1):
            print("*", end='   ')
        print()

def main():
    print("Star pattern")
    no=int(input())
    s=starPattern(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def numPattern(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            print(j, end='  ')
        print()

def main():
    print("Number pattern")
    no=int(input())
    num=numPattern(no)


if __name__=="__main__":
    main()
##****************************************************************************************************##
def Pattern(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j, end='  ')
        print()

def main():
    print("Number Pattern")
    no=int(input())
    num=Pattern(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def digit(num):
    if num:
        print("Number of digits in the numbers are :", int(len(num)))

def main():
    print("Count of digits in the entered number")
    no=input()
    digi=digit(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##
def addDigit(digit):
    add=0
    for i in range(len(digit)):
        add=add+int(digit[i])
    print("Addition of digits are", add)

def main():
    print("Function to display addition of digits in the number")
    no=input()
    ad=addDigit(no)

if __name__=="__main__":
    main()
##****************************************************************************************************##




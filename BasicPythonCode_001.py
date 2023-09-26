#*****************************************************************************************************#
""" Program to display 'Hello' on console """
def Fun():
    print("Hello")

def main():
    print("Function to display Hello on console")
    Fun()

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to check the input number is even or odd"""
def ChkSum(num):
    if (num%2==0):
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Function to check the input number is even or odd")
    print("Enter a number to check")
    no=int(input())
    ChkSum(no)

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to check addition of input numbers"""
def Add(num2):
    addition=0
    for i in range(len(num2)):
        addition=addition+num2[i]
    print("addition of the numbers is :",addition)

def main():
    print("Function to check addition of input numbers")
    num=[]
    print("Please enter a count of number")
    num1=int(input())
    for i in range(num1):
        two=int(input())
        num.append(two)
    print("Entered number is :",num)
    Add(num)

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to display a string 5 times on console"""
def display():
    for i in range(5):
        print("Marvellous")
        
def main():
    display()

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to display numbers from 10 to 1 on console """
def tenToOne():
    for i in range(10,0,-1):
        print(i, end='  ')

def main():
    tenToOne()

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to check a given number is positive, negative or zero"""
def PosNegZero(num):
    if (num>0):
        print("Number positive")
    elif (num==0):
        print("Zero")
    else:
        print("Number negative")

def main():
    print("Please enter a number :")
    no=int(input())
    fun=PosNegZero(no)

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to check whether the given number is divisible by 5 or not"""
def divisible(num):
    print(bool(num%5==0))

def main():
    print("Enter a number to check if divisible by five")
    no=int(input())
    div=divisible(no)

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to display a given number times star on console"""
def starred(star1):
    for i in range(star1):
        print("*", end='  ')

def main():
    print("Function to enter number star ")
    star=int(input())
    starred(star)

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to display first 10 even numbers on console"""
def even():
    for i in range(1,21):
        if (i%2==0):
            print(i, end='  ')

def main():
    print("Function to display first ten even numbers")
    even()

if __name__=="__main__":
    main()
#*****************************************************************************************************#
""" Program to display given character count on the console"""
def length(character):
    if character:
        print(len(character))

def main():
    print("Function to display character count")
    count=input()
    l=length(count)

if __name__=="__main__":
    main()
#*****************************************************************************************************#

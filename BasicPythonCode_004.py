####************************************************************************************************####
def square(num):
    power=lambda num:num**2
    return power(num)

def main():
    print("Enter the number you want the square")
    no=int(input())
    sq=square(no)
    print("The square of the number is :", sq)

if __name__=="__main__":
    main()
####************************************************************************************************####
def mult(x,y):
    multi=lambda x,y:x*y
    return multi(x,y)

def main():
    print("Put the number")
    no1,no2=map(int,input().split())
    no3 = mult(no1,no2)
    print("The multiplication of number is :", no3)

if __name__=="__main__":
    main()
####************************************************************************************************####
from functools import reduce

def Filt(num):
    if num>=70 and num<=90:
        return num

def Map(num):
    return num+10

def Reduced(a,b):
    return a*b

def main():
    no=int(input("Enter a number you want to put in list"))
    listed=[]
    for i in range(no):
        listed.append(int(input("Enter numbers ")))
    print("Listed numbers are :", listed)

    strained=list(filter(Filt,listed))
    print("Data after filter is :", strained)

    Increased=list(map(Map, strained))
    print("Data after map is :", Increased)

    Integrate=reduce(Reduced, Increased)
    print("Data after reduce is :", Integrate)

if __name__=="__main__":
    main()
####************************************************************************************************####
from functools import reduce

def even(no):
    return no%2==0

def square(no):
    return no**2

def addition(m,n):
    return m+n

def main():
    print("enter the count of entity in list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The list is :",size)

    filter1=list(filter(even,size))
    print("The even numbers after filter from list is :", filter1)

    map1=list(map(square,filter1))
    print("The square of the numbers after map is :", map1)

    reduce1=reduce(addition, map1)
    print("Addition of the numbers after reduce is :", reduce1)

if __name__=="__main__":
    main()
####************************************************************************************************####
from functools import reduce

def prime(no):
    for i in range(2,no):
        if (no%i==0):
            return
    else:
        return no

def multiplyBy2(num):
    return num*2

def maximum(num1,num2):
    return max(num1,num2)

def main():
    print("enter the count of entity in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The list is :", size)

    filter1=list(filter(prime,size))
    print("The prime numbers from a list is :", filter1)

    map1=list(map(multiplyBy2,filter1))
    print("The multiplication of numbers after map is :", map1)

    reduce1=reduce(maximum,map1)
    print("The maximum number after reduce is :", reduce1)

if __name__=="__main__":
    main()
####************************************************************************************************####
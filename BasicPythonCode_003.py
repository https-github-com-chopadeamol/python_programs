###**************************************************************************************************###
def addition(list):
    add=0
    for i in range(len(list)):
        add=add+list[i]
    return add

def main():
    print("Accept N numbers from user store in list and return addition")
    print("How much N numbers you want to store?")

    no=int(input())
    nlist=[]

    print("Please enter the N numbers you want to store in list")

    for i in range(no):
        nlist.append(int(input()))
    print("Your entered N numbers are :",nlist)

    ret=addition(nlist)
    print("Addition of entered number is :", ret)

if __name__=="__main__":
    main()
###**************************************************************************************************###
def maximum(yaadi):
    maxi=max(yaadi)
    return maxi

def main():
    print("**** Function to display maximum number from the list ****")
    print("Enter count")
    num=int(input())

    li=[]
    for i in range(num):
        nNum = int(input())
        li.append(nNum)
    print("Numbers in a list is :", li)

    ret=maximum(li)
    print("Maximum number from a list is :", ret)

if __name__=="__main__":
    main()
###**************************************************************************************************###
def frequency(freq):
    no1=int(input())
    count=0
    for i in range(len(freq)):
        if (freq[i]==no1):
            count=count+1
    return count

def main():
    print("Enter the count you want in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The entered number in the list is :", size)

    fre=frequency(size)
    print("The match from the list is :", fre)

if __name__=="__main__":
    main()
###**************************************************************************************************###
def ChkPrime(size):
    prime=[]
    for i in size:
        k=0
        for j in range(1,i):
            if (i%j==0):
                k=k+1
        if k==1:
            prime.append(i)
    return prime

def listPrime(addPrime):
    sum=0
    for i in range(len(addPrime)):
        sum=sum+addPrime[i]
    return sum

def main():
    print("Numbers in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The numbers entered in a list is :",size)

    no1=ChkPrime(size)
    print("The prime numbers in list is :", no1)

    no2=listPrime(no1)
    print("The addition of prime numbers in a list is :", no2)

if __name__=="__main__":
    main()
###**************************************************************************************************###

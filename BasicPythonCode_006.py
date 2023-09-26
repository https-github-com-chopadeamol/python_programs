######********************************************************************************************######
class BookStore:
    NoOfBooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoOfBooks +=1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books : {BookStore.NoOfBooks}")
        print("The Author of Book is :", self.Author)
        print("The number of Books are :", BookStore.NoOfBooks)

def main():
    print("Enter the name of book")
    Name=input()
    print("Enter the author of book")
    Author=input()

    obj1=BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2=BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

if __name__=="__main__":
    main()
######********************************************************************************************######
class BankAccount:
    ROI=10.5
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Display(self):
        print(f"The name of account holder is :{self.Name}")
        print(f"The balance in Bank Account is : {self.Amount}")

    def Deposit(self,depo):
        self.Amount=self.Amount+depo
        print(f"The balance amount in your account after deposit of {depo} is :{self.Amount}")

    def WithDraw(self,bal):
        self.Amount = self.Amount-bal
        print(f"The balance amount in your account after withdrawal of {bal} is :{self.Amount}")

    def CalculateInterest(self):
        calInterest=self.Amount*(BankAccount.ROI/100)
        print(f"The interest amount is : {calInterest}")

def main():
    print("Please enter name and amount subsequently")
    obj=BankAccount(Name=input(),Amount=float(input()))
    print("Please enter the amount you want to deposit")
    obj.Deposit(float(input()))
    print("Enter the amount you want to withdraw")
    obj.WithDraw(float(input()))
    obj.CalculateInterest()
    obj.Display()

if __name__=="__main__":
    main()
######********************************************************************************************######
class Arithmetic:
    def __init__(self,value):
        self.value=value

    def ChkPrime(self):
        for i in range(2,self.value):
            if self.value%i==0:
                return False
        else:
            return True

    def ChkPerfect(self):
        sum=0
        for i in range(1, self.value):
            if self.value%i==0:
                sum=sum+i
        return sum==self.value

    def SumFactors(self):
        count=0
        for i in range(1,self.value):
            if self.value%i==0:
                count=count+i
        return count

    def Factors(self):
        for i in range(1, self.value+1):
            if self.value%i==0:
                print(i)
            break

def main():
    print("Enter the value")
    obj=Arithmetic(value=int(input()))

    obj.ChkPrime()
    print("Is number prime? :",obj.ChkPrime())

    obj.ChkPerfect()
    print("Is it a perfect number? :", obj.ChkPerfect())

    obj.SumFactors()
    print("The addition of factors are :",obj.SumFactors())

    obj.Factors()
    print("The factors of a number is :",obj.Factors())

if __name__=="__main__":
    main()
######********************************************************************************************######

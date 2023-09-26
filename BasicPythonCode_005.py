#####**********************************************************************************************#####
class Demo:
    Value=0
    def __init__(self, a, b):
        print("Inside constructor")
        self.no1=a
        self.no2=b

    def fun(self):
        print("The value of number1 and number2 in fun is :", self.no1, self.no2)

    def gun(self):
        print("The values of number1 and number2 in gun is :", self.no1, self.no2)

def main():
    print("Enter the first number")
    x=int(input())

    print("Enter the second number")
    y=int(input())

    obj=Demo(x,y)

    obj1=Demo(11, 21)
    obj2=Demo(51, 101)

    obj1.fun()
    obj2.fun()
    obj2.gun()
    obj2.gun()

if __name__=="__main__":
    main()
#####**********************************************************************************************#####
class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter the value of radius")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area =self.PI * self.Radius * self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference=2 * self.PI * self.Radius
        #print("The circum :",self.Circumference)
        return self.Circumference

    def Display(self):
        print("The area of a circle is :", self.CalculateArea())
        print("The circumference of circle is :", self.CalculateCircumference())

def main():
    obj=Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__=="__main__":
    main()
#####**********************************************************************************************#####
class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        print("Enter value1")
        self.value1=int(input())

        print("Enter value2")
        self.value2=int(input())

    def Addition(self):
        result=self.value1+self.value2
        return result

    def Substraction(self):
        result=self.value1-self.value2
        return result

    def Multiplication(self):
        result=self.value1*self.value2
        return result

    def Division(self):
        result=self.value1/self.value2
        return result

def main():
    obj=Arithmetic()
    obj.Accept()

    retAdd=obj.Addition()
    print("The addition is :", retAdd)

    retSub=obj.Substraction()
    print("Substraction is :", retSub)

    retMult=obj.Multiplication()
    print("The multiplication is :", retMult)

    retDiv=obj.Division()
    print("The division is :", retDiv)

if __name__=="__main__":
    main()
#####**********************************************************************************************#####









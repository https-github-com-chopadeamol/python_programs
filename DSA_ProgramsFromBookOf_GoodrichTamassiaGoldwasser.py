#page16*******************************************************************************
# Extended Assignment Operators
alpha = [1,2,3]
beta = alpha        # an alias for alpha
beta += [4,5]       # extends the original list two more elements
beta = beta + [6,7] #reassigns beta to a new list [1,2,3,4,5,6,7]
print(alpha)        # will be [1,2,3,4,5]


# d[key]              value associated with given key
# d[key] = value      set (or reset) the value associted with given key
# del d[key]          remove key and its associted value from dictionary
# key in d            containment check
# key not in d        non-containment check
# d1 == d2            d1 is equivalent to d2
# d1 != d2            d1 is not equivalent to d2


#page19******************************************************************************
# Control flow
"""if door_is_closed:
    if door_is_locked:
        inlocked_door()
    open_door()
advance()"""


#page21******************************************************************************
total = 0
for val in data:
    total += val

biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val     
j = 0
while j < len(data) and data[j] != 'X':     # 'X' is an end of sequence
    j += 1


#page22*********************************************************************************
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j
found = False
for item in data:
    if item == target:
        found = True
        break


#page23*********************************************************************************
def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n


#page26*********************************************************************************
def compute_gpa(grades, points = {'A+':4.0, 'A-':3.67, 'B+':3.33,'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0,'C':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses
print(compute_gpa)


#page27*********************************************************************************
def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0


#page31*********************************************************************************
reply = input("Enter x and y, separated by spaces:")
pieces = reply.split()
x = float(pieces[0])
y = float(pieces[1])
print(pieces)
print(x)
print(y)
print(x, y)
age = int(input("Enter your age in years:"))
maxz_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * maxz_heart_rate
print("Your target fat burning heart rate is:", target)


#page34*********************************************************************************
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    else:
        print("unable to get the square root of the entered value")
def main():
    x = int(input("enter the input value: "))   # the input must be either int or float type as mentioned in the sqrt() function
    squareRoot = sqrt(x)
    print(squareRoot)
main()


#page35*********************************************************************************
def sum(values):
    if not isinstance(values, (list, tuple)): #original statement from book:-> if not isinstance(values, collections.iterable):
        raise TypeError("Paramter must be an interable type")
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("Element must be numeric")
        total = total + v
    return total


#page36*********************************************************************************
x = int(input("enter number x: "))
y = int(input("enter number y: "))
if y != 0:
    ratio = x / y
    print("ratio is:", ratio)
else:
    print("This is for demo")

#**************************************************

x = int(input("Enter number x: "))  #added by me
y = int(input("Enter number y: "))  #added by me
try:
    ratio = x / y
    print(ratio)                    #added by me
except ZeroDivisionError:
    print("Division by zero makes it infinite, enter number other than zero")   #added by me


#page37*********************************************************************************
try:
    fp = open('sample.txt')
    print("Sample file has been read")
except IOError as e:
    print("Unable to open the file:", e)

#*************************************************

age = -1
while age <= 0:
    try:
        age = int(input("Enter your age in years: "))
        if age <= 0:
            print("Your age must be positive")
    except (ValueError, EOFError):
        print("Invalid response")


#page38*********************************************************************************
age = -1
while age <= 0:
	try:
		age = int(input("enter your age in years"))
		if age <= 0:
			print("Your age must be positive")
	except ValueError:
		print("That is an invalid age specification")
	except EOFError:
		print("There was an inexpected error reading input")
		raise
     

#page40*********************************************************************************
import time
def factors(n):                 # Traditional function that computes factors
    results = []                # store factors in list
    for k in range(1, n+1): 
        if n % k == 0:          # divides evenly, thus k is a factor
            results.append(k)   # add k to the list of factors
    return results              # return the entire list
def main():
    start = time.time()
    n = int(input("Enter a number: "))
    fact = factors(n)
    print(fact)
    end = time.time()
    TimeTaken = end-start
    print("Time taken to execute a program is: ",TimeTaken)
main()

#***********************************************************

# Implementation of generator for calculating factors
import time

def factors(n):                     #generator that computes factors
    for k in range(1, n+1):         
        if n % k == 0:              # divides evenly, thus k is a factor
            yield k                 # yield this factor as next result
def main():
    start = time.time()
    n = int(input("Enter a number(generator): "))
    fact = factors(n)
    print(list(fact))
    end = time.time()
    TimeTaken = end-start
    print("Time required to execute a program is: ", TimeTaken)
main()


#page41*********************************************************************************
def factors(n):                 # generator that computes factors
    k = 1
    while k * k < n:            # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:              # special case if n is perfect square
        yield k
def main():
    n = int(input("Enter number: "))
    fact = factors(n)
    print(list(fact))
main()

#*************************************************************

def fibonacci():
    a = 0
    b = 1
    while True:                     # keep going
        yield a                     # report value, a, during this pass
        future = a + b
        a = b                       # this will be next value reported
        b = future                  # and subsequently this
        if a >= 50:                 # added to break the infinite loop
            break
fib = fibonacci()
print(list(fib))


#page42*********************************************************************************
def foo(n):
    if n >= 0:
        param = n
    else:
        param = -n
    return param
def main():
    param = int(input("enter number: "))
    result = foo(param)                     # call the function
    print(result)
main()

#*******************************************

def foo(n):
    param = n if n >=0 else -n
    return param
n = int(input("Enter number: "))
result = foo(n)
print(result)


#page43*********************************************************************************
"""
Traditional way to get the squares of a number
"""
n = int(input("Enter a number: "))
squares = []
for k in range(1, n+1):
    squares.append(k * k)
print(squares)

"""
List comprehension to get the square of the number
"""
m = int(input("Enter a number: "))
def squares(m):
    square = [k*k for k in range(1, m+1)]
    return square
print(squares(m))

#**************************************************

"""
Traditional method: Factors of a number 
"""
def factors(n):
    factor = []
    for k in range(1, n+1):
        if n % k == 0:
            factor.append(k)
    return factor
n = int(input("Enter a number: "))
print(list(factors(n)))

"""
List Comprehension: Factors of a numner
"""
def fact(n):
    factors = [k for k in range(1, n+1) if n % k == 0]
    return factors
print(fact(int(input("Enter number: "))))


#page51*********************************************************************************
"""
Write a short python function, is_multiple(n,m), that takes two integer values and returns True if n
is a multiple of m, that is n= mi for some integer i, and False otherwise
"""
#51.1
import sys
def is_multiple(n,m):
    for i in range(n+1):
        if n == m * i:
            return True
    else:
        return False
print("Enter any two integer number: ")
# k = int(input("Enter first integer: "))
# j = int(input("Enter second integer: "))
g, h = len(sys.argv)
multiple = is_multiple(g, h)
print(multiple)

#******************************************************

#51.2
"""
R-1.2: Write a short python function, is_even(k), that takes an integer value and returns True if 
k is even, and False otherwise. However, your function cannot use the multiplication, modulo or 
division operators.
"""
def is_even(k):
    is_even = True
    for i in range(1,k+1):
        if is_even == True:
            is_even = False
        else:
            is_even = True
    return is_even
k = int(input("enter any integer: "))
even = is_even(k)
print("is number even ? :->", even)

#******************************************************

#51.3
"""
R-1.3: Write a short pyton function, minmax(data), that takes a sequence of one or more numbers, 
and returns the smallest and largest numbers, in the form of a tuple of length two, Do not use 
the built in functions min or max in implementing your solution
"""
import sys
def minmax(data):
    largest = data[0]
    smallest = data[0]
    for num in data:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return smallest, largest
iData = ([1,2,3,4,5])
iObj = minmax(iData)
print(iObj)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        num = []
        for i in nums:
            if i not in num:
                num.append(i)
        print(len(num),",", num)

nums = [0,0,1,1,1,2,2,3,3,4]
numbers = sorted(nums)
s = Solution()
s.removeDuplicates(numbers)

python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
for i in python_students:
    #for j in i:
    print(i[1][0])

#*********************************************************

#51.4
"""
Write a short python function that takes a positive integer n and returns the sum of the squares 
of all the positive integers smaller than n
"""
def sum_square(square):
    power = []
    for i in range(square-1,0,-1):
        power.append(i**2)
    add = sum(power)
    return add

iInput = int(input("Enter any positive integer: "))
iObj = sum_square(iInput)
print("Sum of square of positive integer than the given input is: ", iObj)

#*********************************************************

#51.5
"""
Give a single command that computes the sum of from "page51_4.py" relying on python's comprehension
 syntax and the built in sum function
"""
n = int(input("enter number:"))
sumSquare = sum([i*i for i in range(n-1,0,-1)])
print(sumSquare)

#*********************************************************

#51.6
"""
write a short python function that takes a positive integer n and returns the sum of the squares of 
all the odd positive integers smaller than n
"""
def sum_odd_positive(n):
    odd_pos = []
    for i in range(n-1,0,-1):
        if not i % 2 == 0:
            odd_pos.append(i**2)
    addition = sum(odd_pos)
    return addition
n = int(input("Enter any positive integer: "))
iObj = sum_odd_positive(n)
print("Sum of the odd positive is", iObj)

#********************************************************

#51.7
"""
Give a single line commmand that computes the sum from "page51_6.py" relying on python's comprehension 
syntax and the built in sum function
"""
n = int(input("Enter any positive integer: "))
odd_sum = sum([i*i for i in range(n-1,0,-1) if not i%2 == 0])
print("odd positive interger sum is :",odd_sum)

#********************************************************

#51.9
"""
What parameters should be sent to the range constructor, to produce a range with values 50,60,70,80?
"""
for i in range(50,80+1,10):
    print(i, end=" ")

#********************************************************

#51.10
"""
What parameters should be sent to the range constructor, to produce a range with values 
8,6,4,2,0,-2,-4,-6,-8 ?
"""
for i in range(8,-8-1,-2):
    print(i, end=" ")

#*********************************************************

#51.11
"""
Demonstrate how to use python's list comprehension syntax to produce the list [1,2,4,8,16,32,64,128,256]
"""
def multi(n):
    multiple = []
    for i in range(1,n+1):
        if n%i==0:
            multiple.append(i)
    return multiple
n = int(input("Enter a number: "))
iObj = multi(n)
print(iObj)
"""
List comprehension implementation
"""
n = int(input("Enter a number for comprehension: "))
factors = [i for i in range(1,n+1) if n%i==0]
print(factors)

#*******************************************************

#51.12
"""
R-1.12: Python's random module includes a function choice(data) that returns a random element 
from a non empty sequence. The random module includes a more basic function randrange, with 
parameterization similar to the built in range function, that returns a random choice from the 
given range. Using only the randrange function, implement your own version of the chice function
"""
import random
a = random.choice(10)
print(a)


#page70*********************************************************************************
class CreditCard:
    """
    A consumer credit card
    """
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance
        The initial balance is zero
        customer:  The name of the cutomer
        bank    :  The name of the bank
        acnt    :  The account identifier
        limit   :  Credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the banks name"""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number (typically stored as string"""
        return self._account
    
    def get_limit(self):
        """Return current credit limit"""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        Return True if charge eas processed; False if charge was denied
        """
        if price + self.get_balance > self.get_limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount

    def __str__(self):
        return 
    __repr__ = __str__

def main():
    cc = CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 1000)
    print("The details of the customer is: ", cc.__dict__)
main()


#********************************************************************************************************

    


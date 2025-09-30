#There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.
j_angry = bool(input("Enter True/False: "))
s_angry = bool(input("Enter True/False: "))
if j_angry == s_angry:
    print("You are in Trouble")
else:
    print("Not in Trouble")

#Given a positive integer x. Your task is to check, if it is even or odd
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("Even") 
else:
    print("Odd")
    
#Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

# Return True for the following cases:

# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.
# Otherwise, return False.
class Solution:
    def sol(self, a, b, flag):
        if flag == False and ((a > 0 and b < 0) or ( a < 0 and b > 0)) :
            return True
        elif flag == True and (a < 0 and b < 0):
            return True
        else:
            return False

#You are given a string str, you need to return True if  the words "cat" and "dog" appear same number of times in str, otherwise return False.
def animal(str):  
    a=str.count("cat")
    b=str.count("dog")
    if a==b:
        return True
    else:
        return False
    
#Given an integer a, you have to use the if statement to print "Big" (without quotes) if the given number is greater than 100, and use the else statement to print "Number" (without quotes) when the number is smaller than or equal to 100.
a = int(input())
p = "Big"
q = "Number"
if a > 100:
    print(p)
else:
    print(q)

#Given three numbers a, b, and c. You need to find which is the greatest of them all.
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a) 
elif b > a and b > c:
    print(b)
else:
    print(c)

#Given an integer year. Print "True" (without quotes) if it can represent a leap year, otherwise print "False" (without quotes).
year = int(input())
if year % 400 == 0 and year % 100 == 0:
    print(True)
elif year % 4 == 0 and year % 100 != 0:
    print(True)
else:
    print(False)

#You are given a number a and you have to print your answer according to the following:

# If the number is divisible by 3, you print "Fizz" (without quotes)
# If the number is divisible by 5, you print "Buzz" (without quotes)
# If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
# In any other case, you print the number itself
# Note: You should add a new-line character after print statement.
a = int(input())
p = "Fizz"
q = "Buzz"
r = "FizzBuzz"
if a % 3 == 0 and a % 5 == 0:
    print(r)
elif a % 5 == 0:
    print(q)
elif a % 3 == 0:
    print(p)
else:
    print(a)

#Given two numbers a and b. You need to perform basic mathematical operations on them. You will be provided an integer named as operator.

# If the operator equals to 1 add a and b, then print the result.
# If the operator equals to 2 subtract b from a, then print the result.
# If the operator equals to 3 multiply a and b, then print the result.
# If the operator equals to any other number, print "Invalid Input"(without quotes).
# Note: Do not add a new line at the end.

class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        if operator == 1:
            print(a + b,end="")
        elif operator == 2:
            print(a - b,end="")
        elif operator == 3:
            print(a * b,end="")
        else:
            print("Invalid Index",end="")

#Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 

# If you will win: print "You" (without quotes)
# If your friend will win: print "Friend" (without quotes)
n = int(input())
if n % 2 == 0:
    print("Friend")
else:
    print("You")

#Input a number and check if it is positive, negative, or zero.
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Input a character and check if it is a vowel or consonant.
blah = str(input("Enter a Character"))
if blah.isalpha():
    if blah.lower() in ['a','e','i','o','u']:
        print("vowel")
    else:
        print("consonant")
else:
    print("not an alphabet")

#Input a character and check if it is an alphabet, digit, or special character.
blah = input("Enter a Character/Digit/Special Character")
if blah.isalpha():
    print("Alphabet")
elif blah.isdigit():
    print("Digit")
else:
    print("Special Charcater")

#Input a number and check if it is a two-digit number or not.
n = int(input("Enter a number"))
if n > 10 and n < 100:
    print("The input given is a two digit number")
else:
    print("Input given is not a two digit number")

#Input marks of a student and print the grade (e.g., A/B/C/Fail based on ranges).
marks = int(input("Enter your marks"))
if marks > 80 and marks <= 100:
    print("Grade A")
elif marks > 60 and marks <= 80:
    print("Grade B")
elif marks > 40 and marks <= 60:
    print("Grade C")
else:
    print("Fail")

#Input the age of a person and check if they are eligible to vote.
age = int(input("Enter you age"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Input three angles of a triangle and check if it is valid.
a = int(input("Enter first side length of a triangle"))
b = int(input("Enter second side length of a triangle"))
c = int(input("Enter third side length of a triangle"))

if (a + b  > c) and (b + c > a) and (c + a > b):
    print("Valid Triangle")
else:
    print("Not a valid triangle")

#Input three sides of a triangle and check if it is scalene, isosceles, or equilateral.
a = int(input("Enter first side length of a triangle"))
b = int(input("Enter second side length of a triangle"))
c = int(input("Enter third side length of a triangle"))

if( a + b > c) and ( b + c > a) and ( a + c > b):
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")


#Input a character and check if it is uppercase, lowercase, or not an alphabet.
check = str(input("Enter a charcater"))
if check.alpha():
    if check.isupper():
        print("Uppercase Alphabet")
    else:
        print("Lowercase Alphabet")
else:
    print("Not an alphabet")

#Input electricity units consumed and calculate the bill amount using given slabs.
units = int(input("Enter the no.of units consumed"))
if units<=50:
    bill = units * 0.50
elif units<=150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units<=250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) ((units - 250) * 1.50)

charge = bill * 0.20
totalbill = bill + charge
print(totalbill)

#Input the salary of an employee and calculate HRA, DA, and gross salary based on ranges.
salary = int(input("Enter your salary"))
if salary <= 10000:
    HRA = salary * 0.20
    DA = salary * 0.80
elif salary <= 20000:
    HRA = salary * 0.25
    DA = salary * 0.90
else:
    HRA = salary * 0.30
    DA = salary * 0.95

grosssalary = salary + HRA + DA
print("grosssalary")

#Input a day number (1–7) and print the day of the week.
number = int(input("Enter a number(week)"))
match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

#Input a month number (1–12) and print the number of days in that month.
number = int(input("enter a number(months)"))
match number:
    case 1,3,5,7,8,10,12:
        print("31 days")
    case 4,6,9,11:
        print("30 days")
    case 2:
        print("28 or 29 days")

#Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
n = int(input("Enter a number: "))
for i in range(31):
            if 2**i == n:
                print(True)
print(False)


for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# Fibnocci Series
n = int(input("Enter a number: "))
if n == 0:
    print(0)
if n == 1:
    print(1) 
a,b=0,1
for i in range(2,n+1):
    a,b=b,a+b
print(b)



# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
a = "11"
b = "1"
num1 = int(a,2)
num2 = int(b,2)
print(bin(num1 + num2)[2:])



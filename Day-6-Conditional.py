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


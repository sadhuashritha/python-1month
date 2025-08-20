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
    def checkStatus(self, a, b, flag):
        if flag == False and ((a > 0 and b < 0) or ( a < 0 and b > 0)) :
            return True
        elif flag == True and (a < 0 and b < 0):
            return True
        else:
            return False

#You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
def cat_hat(str):  
    a=str.count("cat")
    b=str.count("hat")
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


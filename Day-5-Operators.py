#Take two integers as input and print their sum, difference, product, and quotient.
a = 7
b = 3
c = a // b
print(c)

#Input a number and print its square and cube using **.
a = 5
print(a ** 2)
print(a ** 3)

#Input a number and print the remainder when divided by 7.
a = 5
b = a % 7
print(b)

#Input two floats and print the result of dividing the first by the second with 2 decimal places.
a = 7.5
b = 2.4
c = (a / b)
print(c)
print(round(c,2))

#Input two numbers and check if the first is greater than the second.
a = 10
b = 15
if(a > b):
    print(a)
else:
    print(b)
    
#Input two strings and check if they are equal.
a = 10
b = 5
if a == b:
    print("equal")
else:
    print("not equal")

#Input an age and check if it is greater than or equal to 18.
age = 20
if age > 18:
    print("greater than 18")
elif age < 18:
    print("less than 18")
else:
    print("equal")

# #Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True. First a is checked then b is checked. a or b checks if either of a or b is True. If one is True; it doesn't check for the other. not a complements the boolean value of a.
# Note: 0 and empty string are False and all other values are True.In this question you basically need to do
# a and b
# a or b
# not a

a=int(input())
b=int(input())
p = a and b
q = a or b
r = not a
print(p,q,r)

#Given three positive integers a, b and c. Your task is to perform some bitwise operations
a=int(input())
b=int(input())
c=int(input())
d= a ^ a
e=c ^ b
f=a & b
g=c |(a ^ a)
e= ~e
print(d, e, f, g)

#Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).
class Solution:
    def modTask(self, N):
        # code here
        K = (N // 2) + 1
        return K
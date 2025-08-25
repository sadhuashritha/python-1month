n = int(input())
for i in range(0, n):
    print(i,end="")


li = ["geeks", "for", "geeks"]
for i in li:
    print(i,end="")
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i,end=" ")
    
s = "Geeks"
for i in s:
    print(i,end=" ")
    
d = dict({'x':123, 'y':354})
for i in d:
    print(i, d[i])
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i,end=" "),

#You are given a number N, you need to print its multiplication table.
N =int(input())
for i in range(1,11):
    print(N * i, end=" ")
    

#You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 
n = int(input())
for i in range (1,11):
    print(n * i, end = " ")

#You are given a string s, you need to print its characters at even indices(index starts at 0).
s = str(input())
for i in range(0,len(s),2):
        print(s[i], end="")

#Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
x = int(input())
while x >= 0:
    print(x, end= " ")
    x -= 1

#Given a positive integer x, the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, 4^2, 5^2, ... (in increasing order).
x = int(input())
i = 1
while(x >= i**2):
    print (i**2 , end = " ")
    i+=1
        
#Given an integer,perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format:
# A single line containing a positive integer, .

# Output Format:
# Print Weird if the number is weird. Otherwise, print Not Weird.
n = int(input().strip())
if n % 2 == 0 and n in range(2,6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,21):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
else:
    print("Weird")

#For all non-negative integers , i < n print i ^2
# Example
# The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.
    n = int(input())
    for i in range(0,n):
        print(i**2)

#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
s = str(input())
res = ""
for i in s:
    if i.islower():
        res += i.upper()
    elif i.isupper():
        res += i.lower()
    else:
        res += i

print(res)
    

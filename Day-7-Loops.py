n = int(input())
for i in range(0, n):
    print(i)


li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print(i, d[i])
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

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
        



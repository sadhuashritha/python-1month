# n = int(input("Enter a number"))
# for i in range(0, n):
#     print(i,end="")


# li = ["geeks", "for", "geeks"]
# for i in li:
#     print(i,end="")
    
# tup = ("geeks", "for", "geeks")
# for i in tup:
#     print(i,end=" ")
    
# s = "Geeks"
# for i in s:
#     print(i,end=" ")
    
# d = dict({'x':123, 'y':354})
# for i in d:
#     print(i, d[i])
    
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i,end=" "),

# #You are given a number N, you need to print its multiplication table.
# N =int(input("Enter a number"))
# for i in range(1,11):
#     print(N * i, end=" ")
    

# #You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 
# n = int(input("Enter a number"))
# for i in range (1,11):
#     print(n * i, end = " ")

# #You are given a string s, you need to print its characters at even indices(index starts at 0).
# s = str(input("Enter a string"))
# for i in range(0,len(s),2):
#         print(s[i], end="")

# #Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
# x = int(input("Enter a number"))
# while x >= 0:
#     print(x, end= " ")
#     x -= 1

# #Given a positive integer x, the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, 4^2, 5^2, ... (in increasing order).
# x = int(input("Enter a number"))
# i = 1
# while(x >= i**2):
#     print (i**2 , end = " ")
#     i+=1
        
# #Given an integer,perform the following conditional actions:

# # If  is odd, print Weird
# # If  is even and in the inclusive range of  to , print Not Weird
# # If  is even and in the inclusive range of  to , print Weird
# # If  is even and greater than , print Not Weird
# # Input Format:
# # A single line containing a positive integer, .

# # Output Format:
# # Print Weird if the number is weird. Otherwise, print Not Weird.
# n = int(input("Enter a number").strip())
# if n % 2 == 0 and n in range(2,6):
#     print("Not Weird")
# elif n % 2 == 0 and n in range(6,21):
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")
# else:
#     print("Weird")

# #For all non-negative integers , i < n print i ^2
# # Example
# # The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.
#     n = int(input("Enter a number"))
#     for i in range(0,n):
#         print(i**2)

# #You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# # For Example:
# # Www.HackerRank.com → wWW.hACKERrANK.COM
# # Pythonist 2 → pYTHONIST 2  
# s = str(input("Enter a string"))
# res = ""
# for i in s:
#     if i.islower():
#         res += i.upper()
#     elif i.isupper():
#         res += i.lower()
#     else:
#         res += i

# print(res)

# #Print the digits of a number in reverse order.
# #Example: 123 → 3 2 1
# n = int(input("Enter a number"))
# for i in range(n,-1):
#     print(i)

# #Given an integer n, return true if it is a power of two. Otherwise, return false.
# # An integer n is a power of two, if there exists an integer x such that n == 2x.
# n = int(input("Enter a number: "))
# for i in range(31):
#             if 2**i == n:
#                 print(True)
# print(False)

# # Given an integer n, return true if it is a power of three. Otherwise, return false.

# # An integer n is a power of three, if there exists an integer x such that n == 3x.
# n = int(input("Enter a number: "))
# if n <= 0:
#     print(False) 
# for i in range(31):
#     if 3**i == n:
#         print(True)
# print(False)

# # Write a function that reverses a string. The input string is given as an array of characters s.

# # You must do this by modifying the input array in-place with O(1) extra memory.4444

# s = list(input("Enter a string(reverse a string)"))
# l = 0
# r = len(s) - 1
# while l < r:
#     s[l],s[r] = s[r],s[l]
#     l+=1
#     r-=1
# s = "".join(s)
# print(s)

# #You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# line = "This is a string"
# line = line.split(" ")
# print(line)
# line = "-".join(line)
# print(line) 

# # Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# nums = list(map(int,input("Enter a array").split()))
# nums.sort()
# n=len(nums)
# for i in range(0,n-1,2):
#     if(nums[i]!=nums[i+1]):
#         print(nums[i]) 
#         break
# else:
#     print(nums[n-1])

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
n=int(input("Enter a number"))
result = []
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))
print(result)

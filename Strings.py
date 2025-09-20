# Whooaah! Your are now familiar with String slicing. Let's have one more question to make it crystal clear for you with some conditional statements.

# Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.

# Note: It is guranteed that no two string are of same length.
a = "Hi" 
b = "There"
c1 = 0
c2 = 0
for char in a:
    c1 += 1
for char in b:
    c2 += 1
if c1 > c2:
    short = b
    longer = a
else:
    short = a
    longer = b 

print(short + longer + short)

# Python has a lot of string methods that can be used to manipulate the strings like converting to lowercase, capitalizing, trimming the spaces and so on.

# In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip().
# You'll be given a string str and x, you'll perform various operations on them.

str = "hello" 
x = "llo"
print(str.strip())
print(str.find(x))
print(str.title())
print(str.swapcase())

# Given a string s. The task is to convert string characters to lowercase and uppercase.
s = "ABCddE"
print(s.lower())
print(s.upper())

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
address = "1.1.1.1"
print(address.replace('.','[.]'))

# Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string.
#  The order of remaining characters in the output should be same as in the original string.
s = "geEksforGEeks"
res = []
for char in s:
	if char not in res:
	    res.append(char)
print("".join(res))
	       
#Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
word1 = ["ab", "c"]
word2 = ["a", "bc"]
word1 = "".join(word1)
word2 = "".join(word2)
print(word1 == word2)

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.
# Example 1:
# Input: s = "RLRRLLRLRL" ---> RL  RRLL RL RL
# Output: 4
s = "RLRRLLRLRL"
R = 0
L = 0
res = 0
for i in s:
    if i == "L":
        L += 1
    else:
        R += 1
    if L == R:
        res += 1
print(res) 

# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# Example 1:
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

s = "10#11#12"
i = 0
res = ""
while i < len(s):
    if i + 2 < len(s) and s[i + 2] == "#":
        num = int(s[i:i+2])
        res += chr(num + 96)
        i+=3
    else:
        num = int(s[i])
        res += chr(num + 96)
        i+=1
print(res) 


# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
word1 = "ab"
word2 = "pqrs"
res = []
l = min(len(word1), len(word2))

for i in range(l):
    res.append(word1[i])
    res.append(word2[i])
        
res.append(word1[l:])
res.append(word2[l:])

print("".join(res))


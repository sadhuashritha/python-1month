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
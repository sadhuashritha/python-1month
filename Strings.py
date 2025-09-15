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


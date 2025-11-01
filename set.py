# Write a Python program to create a set with some numbers and print it.
set1 ={1,2,3,4}
print(set1)

# Write a program to add an element to a set using the add() method.
set1 ={1,2,3,4}
set1.add(5)
print(set1)

# Write a program to add multiple elements to a set using the update() method.
set1 ={1,2,3,4}
set1.update([6,7])
print(set1)

# Write a program to remove an element from a set using remove().
set1 ={1,2,3,4,5}
set1.remove(5)
print(set1)

# # Write a program to remove an element from a set using discard() and show the difference from remove().
set1 ={1,2,3,4}
set1.discard(4)
print(set1)

# Write a program to clear all elements from a set using clear().
set1 ={1,2,3,4}
set1.clear()
print(set1)

# Write a program to find the union of two sets.
set1 ={1,2,3,4}
set2 ={5,1,2,6,7}
ans = set1|set2
print(ans)
ans1 = set1.union(set2)
print(ans1)

# Write a program to find the intersection of two sets.
set1 ={1,2,3,4}
set2 ={5,1,2,6,7}
ans = set1 & set2
print(ans)
ans1 = set1.intersection(set2)
print(ans1)

# Write a program to find the difference between two sets (A - B).
set1 ={1,2,3,4}
set2 ={5,1,2,6,7}
ans = set1 - set2
print(ans)
ans1 = set1.difference(set2)
print(ans1)

# Write a program to find the symmetric difference between two sets.
set1 ={1,2,3,4}
set2 ={5,1,2,6,7}
ans = set1 ^ set2
print(ans)
ans1 = set1.symmetric_difference(set2)
print(ans1)

# Write a program to check if a set is a subset of another set.
set1 ={1,2,3,4}
set2 ={5,1,2,6,3,4,7}
count = 0
for i in set1:
    if i in set2:
        count += 1
if count == len(set1):
    print(True)
else:
    print(False)
# or
print(set1.issubset(set2))

# Write a program to check if a set is a superset of another set.
set1 ={1,2,3,4}
set2 ={5,1,2,6,3,4,7}
count= 0 
for i in set1:
    if i in set2:
        count+=1
if count == len(set1):
    print("set2 is superset of set1")
else:
    print("set2 is not superset of set1")
#  or
print(set2.issuperset(set1))

# Write a Python program to find common elements between three sets.
set1 ={1,2,3,4}
set2 ={5,1,2,6,3,4,7}
set3 = {5,1,2,4,9,6}

ans = set1 & set2 & set3
print(ans)

# Given two sets A and B, write a program to print elements that are in A or B but not in both.
set1 ={1,2,3,4}
set2 ={5,1,6,3,4,7}
ans = set1 ^ set2
print(ans)

# Write a Python program to find the maximum and minimum values in a numeric set.
set1 ={5,1,6,3,4,7}
print("min value of set1 is: ",min(set1))
print("max value of set1 is: ",max(set1))


# Write a program to count how many unique elements are present in a list using a set.
list = [1,2,3,3,2,4,5,4,6,7,8]
ans = set(list)
count = 0
for i in ans:
    count += 1
print(count)

# Write a program to count how many unique elements are present in a list using a set.
list = [1,2,3,3,2,4,5,4,6,7,8]
ans = set(list)
count = 0
for i in ans:
    count += 1
print(count)

# Write a program to find all elements that appear more than once in a list using sets.
list = [1,2,3,3,2,4,5,4,6,7,8]
present = set()
notpresent = set()
for i in list:
    if i in present:
        notpresent.add(i)
    else:
        present.add(i)
print(notpresent)


# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
nums = [3,0,1]
n = len(nums)
ans = n * (n + 1) // 2
ans1 = sum(nums)
ans2 = ans - ans1
print(ans2)

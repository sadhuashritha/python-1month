# Create a tuple with 5 integers. Print the first and last element.
tup = (1,2,3,4,5,6,7)
print(tup[0])
print(tup[-1])

# Given a tuple (10, 20, 30, 40, 50), print it in reverse order.
tup = (10, 20, 30, 40, 50)
print(tuple[::-1])

# Create a tuple with different data types (string, int, float, bool). Print each element with its type.
tup1 = ("Ashritha",30,50.68,True)
for i in tup1:
    print(type(i))
print(tup1)


# Check if the number 25 exists in the tuple (10, 20, 25, 30, 35)
tup = (10, 20, 25, 30, 35)
for i in tup:
    if i == 25:
        print("exits")

# Convert the list [1, 2, 3, 4, 5] into a tuple.
li = [1, 2, 3, 4, 5]
tup2 = tuple(li)
print(tup2)

# Concatenate two tuples (1,2,3) and (4,5,6) into one tuple.
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3)

# Repeat the tuple (‘a’, ‘b’) three times.
tup = ('a','b') 
print(tup * 3)

# Find the length of tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
print(len(tup))

# Count how many times 'apple' appears in the tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
count = 0
for i in tup:
    if i == 'apple':
        count += 1
print(count)

# Find the index of 'cherry' in the tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
for i in range(len(tup)):
    if tup[i] == 'cherry':
        print(i)


# Given a tuple (10, 20, 30), unpack it into variables a, b, c. Print each variable.
tup = (10, 20, 30)
a,b,c = tup
print(a)
print(b)
print(c)


# Swap two numbers using tuple unpacking.
tup = (10, 20)
a,b = tup
a,b = b,a
print(a)
print(b)


# Unpack the tuple (“Ashritha”, 21, “CSE”) into name, age, branch. Print a sentence using them.
tup = ("Ashritha", 21, "CSE")
name,age,branch = tup
print("I",name,"of age",age,"studying",branch,"at MRU")


# From the tuple ((10, 20), (30, 40), (50, 60)), print all first elements (10, 30, 50)
tup = ((10, 20), (30, 40), (50, 60))
for i in tup:
    print(i[0])

# Given a tuple of tuples ((1,2), (3,4), (5,6)), access the element 4.
tup = ((1,2), (3,4), (5,6))
print(tup[1][1])

# Create a nested tuple for student details: ("John", (85, 90, 78)). Print the average marks.
tup = ("John", (85, 90, 78))
student = tup[0]
marks = tup[1]
avg = sum(marks)/ len(student)
print("student" , student)
print("total marks",avg

# Iterate through tuple (‘red’, ‘green’, ‘blue’) and print each element with its index.
tup = ("red", "green", "blue")
for i in range(len(tup)):
    print(i,tup[i])

# Find the maximum and minimum in the tuple (45, 67, 23, 89, 12)
tup = (45, 67, 23, 89, 12)
min = tup[0]
max = tup[0]
for i in tup:
    if i <= min:
        min = i
    elif i >= max:
        max = i
print(min)
print(max)

# Write a program to check if two tuples (1,2,3) and (1,2,3) are identical.
tup = (1,2,3)
tup1 = (1,2,3)

if tup == tup1:
    print("Tuples are identical")
else:
    print("tuples are not identical")

# You have a list of student marks as tuples [("John", 85), ("Alice", 92), ("Bob", 78)]. Sort them by marks.
tup = [("John", 85), ("Alice", 92), ("Bob", 78)]
ans = sorted(tup,key=lambda x : x[1])
print(ans)


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans= []
        for i in arr2:
            for j in arr1:
                if i == j:
                    ans.append(i)

        for j in sorted(arr1):
            if j not in arr2:
                ans.append(j)
        return ans

# 1337. The K Weakest Rows in a Matrix
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
ans = []
for i in mat:
    count = 0
    for j in i :
        if j == 1:
            count += 1
    ans.append(count)
    
index = list(range(len(mat)))
index.sort(key = lambda x : ans[x])
print(index[:k])

# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print(False)
for i in s:
    if i not in t:
        print(False) 
    else:
        t = t.replace(i,"",1)
print(True)


# 1636. Sort Array by Increasing Frequency
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
nums = [1,1,2,2,2,3]
ans = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    ans.append((count))
freq = list(range(len(nums)))
freq.sort(key = lambda x : (ans[x], -nums[x]))
return [nums[i] for i in freq]


# 1337. The K Weakest Rows in a Matrix
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
ans = []
# for i in mat:
for i in range(len(mat)):
    count = 0
    # for j in i :
    for j in mat[i]:
        if j == 1:
            count += 1
    ans.append((i,count))
    # ans.append(count)
    
# index = list(range(len(mat)))
# index.sort(key = lambda x : ans[x])
# return index[:k]

ans.sort(key = lambda x : (x[1],x[0]))
return [x[0] for x in ans[:k]]


# Create a tuple with 6 elements of different data types. Print its length.
tup = [20,"ashritha",True,50.0,60,"lisa"]
a = len(tup)
print(a)

# Check whether the number 50 exists in the tuple (10, 20, 30, 40, 50, 60).
tup = [10,20,30,40,50,60]
for i in tup:
    if i == 50:
        print("Exists")

# Create a tuple (10, 20, 30) and convert it into a list, change the second value to 99, and convert it back to a tuple.
tup = [10,20,30]
a = list(tup)
a[1] = 99
print(a)

# Write a program to repeat the tuple (1, 2, 3) five times using repetition operator.
tup = [1,2,3]
print(tup * 5)


# Given a tuple (10, 20, 30, 40, 50), find the index of element 40.
tup = [10,20,30,40,50]
for i in range(len(tup)):
    if tup[i] == 40:
        print(i)

#389. Find the Difference
# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
s = "abcd"
t = "abcde"
for i in t:
    if t.count(i) != s.count(i):
        print(i)

# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
ransomNote = "a"
magazine = "b"
for i in ransomNote:
    if i in magazine:
        magazine = magazine.replace(i,"",1)
    elif i not in magazine:
        print(False)
print(True)


# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
nums = [2,7,11,15]
target = 9
ans= []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            ans.append(i)
            ans.append(j)
            print(ans)
print(False)

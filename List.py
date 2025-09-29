# GFG   You are given a list that contains integers. You need to print the elements of the list with a space between them.
# Note: Do not add a new line at the end.
arr = [54, 43, 2, 1, 5]
for i in arr:
    print(i,end=" ")
print()

# GFG   You are given a list that contains integers. You need to return the length of the list.
arr = [54, 43, 2, 1, 5]
# print(len(arr))
count = 0
for i in arr:
    count += 1
print(count)

# GFG   You are given a list that contains integers. You need to return the sum of the list.
arr = [54, 43, 2, 1, 5]
sum = 0
for i in arr:
    sum += i
print(sum)

# GFG   You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.
arr = [54, 43, 2, 1, 5]
for i in range(len(arr)):
    arr[i] -= 1
print(arr)

# You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list.
a,b,c = 1,2,3
list=[]
list.append(a)
list.append(b)
list.append(c)
print(list) 

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

nums = [1,2,1]
print(nums * 2)

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

nums = [1,2,3,4]
sum = 0
for i in range(1,len(nums)):
    nums[i] = nums[i-1] + nums[i]
print(nums)

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
nums = [0,2,1,5,3,4]
ans = []
for i in range(len(nums)):
    ans.append(nums[nums[i]])
print(ans)

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
sum = 0
for i in range(1,len(nums)):
    nums[i] = nums[i-1] + nums[i]
print(nums)

# There is a programming language with only four operations and one variable X:
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
operations = ["--X","X++","X++"]
X = 0
for i in operations:
    if i == "X++" or i == "++X":
        X += 1
    else:
        X -= 1
print(X)


# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

accounts = [[1,2,3],[3,2,1]]
max1 = 0
for i in range(len(accounts)):
    ans = 0
    for j in accounts[i]:
        ans += j 
    if ans > max1:
        max1 = ans
print(max1)

# leetcode 1313 We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.

nums = [1,2,3,4]
ans = []
for i in range(0,len(nums),2):
    freq = nums[i]
    val = nums[i + 1]
    ans.extend([val] * freq)
print(ans)


# leetcode 1431 There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.
# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 

candies = [2,3,5,1,3]
extraCandies = 3
ans = []
great = max(candies)
for i in range(len(candies)):
    if candies[i] + extraCandies >= great:
        ans.append(True)
    else:
        ans.append(False)
print(ans)

# 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
nums = [2,5,1,3,4,7]
n = 3
ans = []
# for i in range(n):
#     ans.append(nums[i])
#     ans.append(nums[i+n])
# print(ans)
n1 = nums[:n]
n2 = nums[n:]
for i,j in zip(n1,n2):
    ans.append(i)
    ans.append(j)
print(ans)

# 1854. Maximum Population Year
# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
# Return the earliest year with the maximum population.
logs = [[1993,1999],[2000,2010]]
count = [0] * 2050
for birth,death in logs:
    for i in range(birth,death):
        count[i] += 1

maxpop = max(count)
for i in range(1950,2050):
    if count[i] == maxpop:
print(i)

# 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 ans = []
# for i in range(n):
#     ans.append(nums[i])
#     ans.append(nums[i+n])
# print(ans)
n1 = nums[:n]
n2 = nums[n:]
for i,j in zip(n1,n2):
    ans.append(i)
    ans.append(j)
print(ans)

# 2114. Maximum Number of Words Found in Sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
count = 0
for i in sentences:
    res = len(i.split())
    if res > count:
        count = res
print(count)


# 1720. Decode XORed Array
# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.
encoded = [1,2,3]
first = 1
ans = []
ans.append(first)
for i in range(len(encoded)):
    ans.append(encoded[i] ^ ans[i])
print(ans)


# 1389. Create Target Array in the Given Order
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.
nums = [0,1,2,3,4], index = [0,1,2,2,1]
res = []
for i in range(len(nums)):
    res.insert(index[i],nums[i])
print(res)

# 2574. Left and Right Sum Differences
# You are given a 0-indexed integer array nums of size n.
# Define two arrays leftSum and rightSum where:
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
nums = [10,4,8,3]
ans = []
one = []
two = []
res = 0
res1 = 0
for i in range(len(nums)):
    if i == 0:
        one.append(0)
    else:
        res += nums[i-1]
        one.append(res)
for i in range(len(nums)-1,-1,-1):
    if i == len(nums)-1:
        two.append(0)
    else:
        res1 += nums[i+1]
        two.append(res1)
two.reverse()
for i in range(len(one)):
    ans.append(abs(one[i] - two[i]))
print(ans)

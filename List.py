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
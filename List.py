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
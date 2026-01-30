# Prime Number
n = 14
for i in range(2,n):
    if n % i == 0:
        print("Not a Prime")
        break
else:
    print("Prime Number")

# Fibonacci series
n = 10
a = 0
b = 1
print(a,end=" ")
for i in range(0,n+1):
    print(b,end=" ")
    a,b = b,a+b  #0,1,1,2...
# a,b = b,a+b
# 0,1 => 1,1
# 1,1 => 1,2...

# String palindrome
print()
a = "2wow2"
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")




# Reverse string
a = "ashritha"
b = list(a)
c = ""
for i in range(len(b)-1,-1,-1):
    c += b[i]
print(c)


a = "ashritha"
b = list(a)
p1 = 0
p2 = len(b)-1
while p1 < p2:
    b[p1],b[p2] = b[p2],b[p1]
    p1+=1
    p2-=1
c = "".join(b)
print(c)

s = ["h","e","l","l","o"]
c = ""
for i in range(len(s)-1,-1,-1):
    c+=s[i]
print(list(c))

a = "ashritha"
ans = a[::-1]
print(ans)

# Second largest in array
a = [1,4,3,7,8]
a.sort(reverse = True)
print(a[1])

# Remove duplicates
a = [1,4,5,7,2,1,4]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)

#  Valid Anagram
s = "anagrau"
t = "nagarau"
if len(s) != len(t):
    print("Not Anagram")
a = list(s)
b = list(t)
a.sort()
b.sort()
# c = "".join(a)
# d = "".join(b)

# a = "".join(sorted(s))
# b = "".join(sorted(t))
if a == b:
    print("Anagram")
else:
    print("Not an Anagram")


# Character frequency
a = [1,3,4,2,3,1,3,1]
d = {}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1
print(d)

# Pair sum
arr = [2, 7, 11, 15]
target = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(i,j)
            found = True
    if found:
        break
if not found:
    print("Not found")


# Even odd separation
arr = [1, 2, 3, 4, 5, 6]
Even = []
Odd = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        Even.append(arr[i])
    else:
        Odd.append(arr[i])
print(Even)
print(Odd)

# Factorial
a = 5
sum = 1
for i in range(1,a+1):
    sum *= i
print(sum)


# Question: Write a program which will find all such numbers 
# which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=" ")
print()
print()

# Question: Write a program which can compute the factorial of a given numbers.
#  The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

num = 8
sum = 1
for i in range(1,num+1):
    sum *= i

print(sum)

  
# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). 
# and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()


# Armstrong number
n = 153
num = list(str(n))
size = len(num)
a = []
for i in range(len(num)):
    a.append(int(num[i]) ** size)
sum = 0
for i in range(len(a)):
    sum += a[i]

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Fibonacci series
n = 10
a = 0
b = 1
print(a,end=" ")
for i in range(0,n+1):
    print(b,end=" ")
    a,b = b,a+b  
print()#0,1,1,2...
# a,b = b,a+b
# 0,1 => 1,1
# 1,1 => 1,2...

# 1. Reverse the given array in place using two pointers without using extra space.
arr = [5,6,7,8,9]
p1 = 0
p2 = len(arr)-1
while p1 < p2:
    arr[p1],arr[p2] = arr[p2],arr[p1]
    p1 += 1
    p2 -= 1
print(arr)

# 2. Check Whether an Array Is Palindrome
arr = [1,2,3,2,1]
if arr == arr[::-1]:
    print("Palindromic Array")
else:
    print("Not a Palindromic Array")

# 3. Find a Pair with Given Sum in Sorted Array
arr = [8,9,2,7,1,3]
sum = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        res = arr[i] + arr[j] 
        if res == sum:
            print(arr[i],arr[j],"Pair Found")
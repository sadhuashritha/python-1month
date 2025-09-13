#Input: n = 5
# Output:
# *
# **
# ***
# ****
# *****
n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

# 1
# 2 2 
# 3 3 3`    `
# 4 4 4 4
# 5 5 5 5 5
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()

# A
# B C
# D E F 
# G H I J
# K L M N O
n = 5
alph = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(alph),end=" ")
        alph += 1
    print()
print()

# Input: n = 5
# Output:
# *****
# ****
# ***
# **
# *

n = 6
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print()

# 01234
# 0123
# 012
# 01
# 0
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print(j,end=" ")
    print()
print()

# 55555
# 4444
# 333
# 22
# 1

n = 5
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
print()




# Input: n = 5
# Output:
#     *
#    ***
#   *****
#  *******
# *********

n = 6
sum = 0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print("*",end=" ")
    print()

print()

# 
#           A
#         A B C
#       A B C D E
#     A B C D E F G
#   A B C D E F G H I 
# A B C D E F G H I J K
n = 6
sum = 0
alph = 65
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print(chr(alph),end=" ")
        alph += 1
    alph = 65
    print()

print()


#           0
#         0 1 2 
#       0 1 2 3 4
#     0 1 2 3 4 5 6 
#   0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9 10 

n = 6
sum = 0
alph = 65
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print(k,end=" ")
        alph += 1
    alph = 65
    print()

print()


# Input: n = 5
# Output:
# 1
# 12
# 123
# 1234
# 12345

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

#   1 
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5
n=5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print()

# n=5
#         * 
#       * * *
#     * * * * *
#   * * * * * * * 
# * * * * * * * * *
#   * * * * * * * 
#     * * * * *
#       * * *
#         *

n = 5
for i in range(1,n+1):
    for j in range(n - i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range((2*i) - 1):
        print("*",end=" ")
    print()

print() 


# n=5
#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5 
#   4 4 4 4 4 4 4
#     3 3 3 3 3
#       2 2 2
#         1

n = 5
for i in range(1,n+1):
    for j in range(n - i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print(i,end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range((2*i) - 1):
        print(i,end=" ")
    print()

print() 
# Input: n = 5
# Output:
#     *
#    ***
#   *****
#    ***
#     *

n = 5
mid = (n + 1)//2
for i in range(1,mid+1):
    for j in range(mid - i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print("*",end=" ")
    print()

for i in range(mid-1,0,-1):
    for j in range(mid - i):
        print(" ",end=" ")
    for k in range((2*i) -1):
        print("*",end=" ")
    print()


print()

# n=5
# *   *
#  * * 
#   *  
#  * * 
# *   *
n = 5
mid = (n+1)//2
for i in range(1,mid+1):
    for j in range(1,n+1):
        if j == i or j == (n-i) + 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(mid-1,0,-1):
    for j in range(1,n+1):
        if j==i or j == (n-i) + 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()


# 1       1 
#   2   2
#     3
#   2   2
# 1       1 

n = 5
mid = (n+1)//2
for i in range(1,mid+1):
    for j in range(1,n+1):
        if j == i or j == (n-i) + 1:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(mid-1,0,-1):
    for j in range(1,n+1):
        if j==i or j == (n-i) + 1:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

print()

# n=5
#       A 
#      A B
#     A B C
#    A B C D
#   A B C D E
n = 5
alpha = 65
for i in range(1,n+1):
    print(" " * (n-i), end=" ")
    # for j in range(n-i):
        # print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(alpha),end=" ")
        alpha+=1
    alpha = 65
    print()

# n=5
#      1
#     2 2
#    3 3 3
#   4 4 4 4 
#  5 5 5 5 5
n = 5
for i in range(1,n+1):
    print(" " * (n-i), end=" ")
    # for j in range(n-i):
        # print(" ",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# # n = 5
# #         *
# #       *   *
# #     *       *
# #   *           *
# # * * * * * * * * *
n = 5
for i in range(1,n+1):
    for j in range(1,(2*n)):
        if i == n or j == (n-i) + 1 or j == n + (i - 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
n = 5
for i in range(1,n+1):
    for j in range(n):
        print("*",end=" ")
    print()

print() 

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
n = 5
for i in range(1,n+1):
    for j in range(n):
        print(i,end=" ")
    print()

print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
n = 5
for i in range(1,n+1):
    for j in range(n):
        print(j+1,end=" ")
    print()
print()


# * * * * * 
# *       *
# *       *
# *       *
# * * * * *
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i == n or j==1 or j == n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 1 1 1 1 1
# 2       2
# 3       3
# 4       4
# 5 5 5 5 5 
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i == n or j==1 or j == n :
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

# 1 2 3 4 5
# 1       5
# 1       5
# 1       5
# 1 2 3 4 5
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i == n or j==1 or j == n :
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()


# * * * * * 
#   *   *
#     *
#   *   *
# * * * * *
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or i == j or j == n-i+1:
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print()
print()

# 1 2 3 4 5
#   2   4
#     3
#   2   4
# 1 2 3 4 5

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or i == j or j == n-i+1:
            print(j,end=" ")
        else:
            print(" " ,end=" ")
    print()
print()

#      * * * * * 
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
n = 5
for i in range(n):
    print(" " * (n-i-1),end=" ")
    print("* " * n)



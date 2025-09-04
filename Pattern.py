n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

n = 6
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

n = 6
sum = 0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range((2*i) - 1):
        print("*",end=" ")
    print()

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

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
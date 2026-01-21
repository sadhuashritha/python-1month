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

# Armstrong number
n = 1234
num = list(str(n))
size = len(num)
a = []
for i in range(len(num)):
    a.append(int(num[i]) ** size)
sum = 0
for i in range(len(a)):
    sum += a[i]
print(sum)



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
a.sort()
print(a[1])




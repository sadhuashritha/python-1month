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
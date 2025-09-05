
#Assign a value to a variable and check its type using type().
c = {"name":"ashritha","age":20}
print(type(c))

#Store a string "100" in a variable, convert it into an integer, and add 50.
p = "100"
q = int(p)
r = q + 50
print(r)

#Demonstrate variable reassignment by assigning different data types (e.g., int → string → float) to the same variable and printing each time.
a = 10
print(a)
print(type(a))
a = "Hello"
print(a)
print(type(a))
a = True
print(a)
print(type(a))

#Check Data Type Write a program that takes input from the user and prints its data type.
x = int(input("Enter value of x: "))
print(type(x))

#Given an integer x, return true if x is a palindrome, and false otherwise.

x = str(input("Enter a Steing"))
if x == x[::-1]:
    print(True)
else:
    print(False)
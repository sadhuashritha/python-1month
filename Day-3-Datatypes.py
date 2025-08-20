#Declare two integer variables and print their sum.
a = 3
b = 5
print(a + b)

#Assign your name to a variable and print it.
z = "Ashritha"
print(z)

#Store an integer in a variable, then change its value to a float and print both.
z = 6
y = float(z)
print(z,y)

#Assign the same value to three variables in one line and print them.
m=n=o = 17
print(m,n,o)

#Swap two variables without using a third variable.
s = 5
p = 9
s,p = p,s
print(s,p)

#Assign multiple values to multiple variables in one line and print them.
s,p,q = 3,5,6
print(s,p,q)

#Store your age in a variable and print "I am X years old" using that variable.
age = 20
print("I am ",age,"years old")

#Assign a boolean value (True/False) to a variable and print it.
v = False
print(v)
print(type(v))

#Concatenate two string variables and print the result.
x = "Hello"
y = "World"
print(x + " " + y)

#Store a number in a variable and print its square using that variable.
d = 5
print(d*d)

#Assign a decimal number to a variable and convert it into an integer.
f = 5.6
g = int(f)
print(g)

#Declare a variable, delete it using del, and try printing it.
k = 40
del k
#print(k)

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
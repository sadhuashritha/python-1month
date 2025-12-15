# Python Introduction + Input/Output
# 1.Write a program to print "Hello, World!".
print("Hello World")

# 2.Write a program to print your name, age, and city on separate lines.
name = "Ashritha"
age = 20
city = "Medak"
print(name)
print(age)
print(city)

# 3.Write a program that prints a multi-line string using triple quotes.
string = """program that prints a 
multi-line string using 
triple quotes."""
print(string)

# 4.Write a program to take your name as input and print "Hello, <name>!".
Name  = "Ashritha"
print("Hello",name,"!")

# 5.Write a program that asks the user for two numbers and prints their sum.
n = 10
m = 20
print(n + m)

# 6.Write a program that asks the user for their age and prints whether they are a minor or an adult (just print the message, no conditions yet).
age =30
print("You are a minor or an adult")

# 7.Write a program that uses input() to read a string and then prints its length.
s = "Ashritha"
print(len(s))

# 8.Write a program to read a line from the user and print it in this format:
# You entered: <user_input>.
# n = int(input("Enter Your Name"))
n = "Ashritha"
print("You entered: " , name)

# 9.Write a program that reads your full name and prints it in one line and then in two lines (first name on first line, last name on second).
n = "Sadhu Ashritha"
print(n)
m = n.split()
one = m[0]
two = m[1]
print(one)
print(two)

# 10.Write a program that takes two numbers as strings from the user and shows the difference between string concatenation and numeric addition.
a = "9"
b = "10"
c = 9
d = 10
print("String Concatenation",a+b)
print("Numeric Addition:",c+d)

# 11.Write a program that asks the user for three values and prints them using an f-string i
a = 10
b = 20
c = 30
print(f"A: {a} B: {b} C: {c}")

# 12. Write a program that demonstrates the use of sep and end parameters in print().
a = "Apple"
b = "Banana"
print("A: ",a,"B: ",b)
print(a,b, sep=", " , end= " " )
print(a,b)

# 13. Write a program that prints a formatted table-like output using \t and \n.
print("Name\tAge\tCity")
print("Will\t20\tMedak")
print("Lisa\t22\tKamareddy")
print("Chandh\t18\tHyderabad")

# 14.Write a program that reads a float from the user and prints it rounded to 2 decimal places.
a = 15.345
b = round(a,2)
print(b)

# 15 Write a program that shows the difference between print(5) and print("5").
print(type("5"))
print(type(5))



# VARIABLES

# 16.Write a program that stores your name, age, and CGPA in variables and prints them.
name = "Ashritha"
age = 20
CGPA = 8.8
print(f"name :{name} age:{age} CGPA:{CGPA}")

# 17.Write a program to swap two variables using a temporary variable.
a = 20
b = 30
print("a: ",a)
print("b: ",b)
c = a
a = b
b = c
print("a: ",a)
print("b: ",b)
print()
print()

# 18 Write a program to swap two variables without using a temporary variable.
a = 20
b = 30
print("a: ",a)
print("b: ",b)
a,b = b,a
print("a: ",a)
print("b: ",b)

# 19 Write a program that assigns the same value to three variables in one line and prints them
a=b=c = 10
print(a,b,c)

# 20 Write a program that demonstrates multiple assignment like a, b, c = 1, 2, 3.
a,b,c = 1,2,3
print(a,b,c)

# 21 Write a program that reads two numbers and stores their sum, difference, product, and quotient in four different variables and prints all.
a = 20
b = 15
sum = a + b
diff = a - b
mul = a * b
quo = a / b
flo = a // b
print(sum,diff,mul,quo,flo)

# 22. Write a program to show what happens if you reassign a variable from int to string.
a = 10
print(a,type(a))

a = "ten"
print(a,type(a))
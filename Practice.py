# Python Introduction + Input/Output
# ==================================

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
# ==========

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

# 23. Write a program that uses descriptive variable names for calculating the area of a rectangle.
length = 10
breadth = 20
area = 2*(length + breadth)
print(area)

# 25.Write a program that uses a constant-like variable (e.g. PI = 3.14) and calculates the area of a circle.
r = 1.5
pi = 3.14
area = pi * r**2
print(area)

# 26 Write a program to add, subtract, multiply, and divide two numbers.
a = 20
b = 15
sum = a + b
diff = a - b
mul = a * b
quo = a / b
flo = a // b
print(sum,diff,mul,quo,flo)

# 27 Write a program that uses the floor division (//) and modulus (%) operators and prints the results for two integers.
a = 20
b = 10
print(a//b)
print(a % b)

# 28 Write a program to calculate a raised to the power b using **.
b = 2
a = 5
print(a**b)

# 29. Write a program that compares two numbers and prints which one is greater using comparison operators.
a = 20
b = 60
print(a<b)

# 30. Write a program that checks if two given numbers are equal or not.
a = 10
b = 20
print(a==b)
print()
print()

# 31. Write a program that demonstrates all comparison operators (==, !=, >, <, >=, <=) with sample values.
a = 10
b = 20
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print()

# 32. Write a program that uses logical operators (and, or, not) to check if a number is in the range 10 to 20.
a = 10
b = 20
print(a and b)
print(a or b)
print(not b)
print(not a)
print()

# 33.Write a program that checks if a given year is between 2000 and 2025 and not equal to 2010.
c = 2005
if c>=2000 and c<=2025 and c!=2010:
    print("Lies in between 2000 and 2025 and not equal to 2010")
else:
    print("Not satisfies the condition")

# 34. Write a program to show the effect of operator precedence in an expression like 3 + 4 * 2 ** 3.
a = 3 + 4 * 2 ** 3
print(a)
print()

# 35.Rewrite an expression using parentheses to change the default precedence and show different outputs.
a = 3 + 4 * 2 ** 3
print(a)
a = (3 + 4 ) * 2 ** 3
print(a)
a = 3 + (4 * 2 ) ** 3
print(a)
print()

# 36. Write a program to demonstrate assignment operators (+=, -=, *=, /=, //=, %=, **=) on a variable.
a = 20
b = 30
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a%=b
print(a)
a**=b
print(a)
print()

# 37. Write a program to check if a number is even using the modulus operator.
a = 20
if a %2==0:
    print("Even Number")
else:
    print("Odd number")
print()

# 38.Write a program to check if a number is a multiple of both 3 and 5 using logical operators.
a = 18
if a % 2 == 0 and a % 3 == 0:
    print("Divisible by 2 and 3")
elif a %2==0 and a %2!=0:
    print("Divisible by 2 but not 3")
elif a % 2 != 0 and a % 3 == 0:
    print("Divisible by 3 but not 2")
else:
    print("Not divisible by both 2 and 3")

# 39. Write a program that reads three numbers and prints the largest using only comparison operators (no max()).
a = 10
b = 20
c = 30
if a>b and a>c:
    print(a," a is greater element")
elif b>c and b>a:
    print(b, " b is greater element")
else:
    print(c," c is greater element")
print()

# 40. Write a program to demonstrate the difference between / and // when dividing integers.
a = 10
b = 20
print(a/b)
print(a//b)
print()

# 41. Write a program that uses bitwise operators (&, |, ^, <<, >>) on two small integers and prints the results.
a = 1
b = 2
print(a & b)
print(a | b)
print(a ^ b)
print(a<<b)
print(a>>b)
print()

# 42. Write a program that checks if a number is odd using a bitwise operation.



# 43.Write a program that toggles bits of a number using bitwise XOR.



# 44.Write a program that demonstrates the use of in and not in operators on a string
x = 20
y = 30
li = [10,20,30,40,50]
if (x not in li):
    print("Given element is not present in list")
else:
    print("Given element is present in list")
print()

# 45 Write a program that demonstrates the use of is and is not operators on small integers and lists (identity vs equality).
a = 10
b = a
c = 10
d = 20
print(a is not b)
print(a is b)
print(a is c)
print(c is not a)
print(c is d)
print(d is not c)


# KEYWORDS
# ========


# 46 Write a program that uses if, elif, and else to categorize a number as negative, zero, or positive.
a = -30
if a > 0:
    print("Given number is positive: ",a)
elif a < 0:
    print("Given number is negative: ",a)
else:
    print("Given number is zero: ",a)

# 47.Write a program to demonstrate the use of for and while keywords in simple loops.
# print 5 table using for loop
for i in range(1,11):
    sum = 5
    sum = sum * i
    print(sum,end=" ")
print()
# print 5 table using while loop 
sum = 1
while(sum < 11):
    a = 5
    a*=sum
    print(a,end=" ")
    sum += 1
print()

# 48. Write a program that uses the break keyword to exit a loop when a certain condition is met.
n = 15
for i in range(1,n+1):
    if i == 10:
        print("Element Found: ",i)
        break
else:
    print("Element not found")
print()

# 49.Write a program that uses the continue keyword to skip printing even numbers from 1 to 10.
for i in range(1,11):
    if i == 5 or i == 10:
        continue
    print("Number: ",i)
print()

# 50.Write a program that uses pass inside a function or loop and explain why it’s needed.


# 51.Write a program that demonstrates the use of True, False, and None.
a = True
b = False
c = None
print(a,type(a))
print(b,type(b))
print(c,type(c))
print()

# 52.Write a program that defines a function using def and returns a value using return.


# 53.Write a program that uses the in keyword to check if a character exists in a string.
stri = "Ashritha"
if "r" in stri:
    print("T exists in given string")
else:
    print("T doesnot exists in given string")
print()

# 54.Write a program to demonstrate the not keyword in a condition.
stri = "Ashritha"
if not "u" in stri:
    print("U does not exists in given string")
else:
    print("U exists in given string")
print()

# 55.Write a program that shows the difference between a variable named global_var and using the global keyword inside a function.



# DataTypes
# =========


# 56.Write a program that prints the type of various literals: 10, 10.5, "hello", True, None, [1,2], (1,2), {1,2}, {"a":1}.
a = 10
print(a,type(a))
b = 10.5
print(b,type(b))
c = "hello"
print(c,type(c))
d = True
print(d,type(d))
e = None
print(e,type(e))
f = [1,2]
print(f,type(f))
g = (1,2)
print(g,type(g))
h = {1,2}
print(h,type(h))
i = {"a":1}
print(i,type(i))

# 57.Write a program that reads a number from the user as a string, converts it to int and float, and prints their types.
a = "8"
b = int(a)
c = float(a)
print(a,type(a))
print(b,type(b))
print(c,type(c))
print()
print()

# 58. Write a program that demonstrates implicit type conversion (e.g., int + float).
# Implicit
a = 10
print(a,type(a))
b = 10.5
print(b,type(b))
c = "hello"
print(c,type(c))
print()

# Explicit
a = "8"
b = int(a)
c = float(a)
print(a,type(a))
print(b,type(b))
print(c,type(c))
print()

# 59.Write a program that shows an example where implicit conversion does NOT happen and you have to use explicit casting.
a = 10
b = "20"
# c = a + b
# causes error
c  = a + int(b)
print(c,type(c))
print()

# 60. Write a program that calculates the average of three integers but ensures the result is a float.
a = 10
b = 30
c = 100
d = (a+b+c) / 3
e = float(d)
print(d)
print()

# 61.Write a program that stores different data types in a list and prints the type of each element.
li = [10,10.0,"Ashritha",False]
for i in li:
    print(i,type(i))
print()

# 62. Write a program that checks whether the input is numeric or not using string methods and then converts it to int safely.
# n = input("Enter a value: ")
# if n.isdigit():
#     x = int(n)
#     print("The number is numeric: ",x)
# else:
#     print("The given number is not numeric")
# print()
# print()

# 63. Write a program that takes a decimal number and converts it to int using int() and explains what happens to the fractional part.
a = 10.6
b = int(a)
print(b,type(b))
print()

# 64.Write a program that demonstrates boolean operations using expressions like 5 > 3, 3 == 4, etc., and prints their types.
a = 10
b = 20
c = a > b
d = a == b
print(c,type(c))
print(d,type(d))
print()

# 65 Write a program that converts an integer to string, concatenates it with another string, and prints the result.
a = 10
b = "ashritha"
c = str(a)
print("a:",a,"b:",b)
print(c + b)
print()


# 66 Write a program that takes a boolean expression and prints True or False depending on a condition (e.g. age >= 18).
age = 20
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
print()

# 67.Write a program that converts a string "123" to int, adds 1 to it, and prints the result.
a = "123"
b = int(a)
c = b + 1
print(c)

# 68.Write a program that converts a float to string and checks its length.
a = 50.5678
b = str(a)
print("Length of a string: ",len(b))

# 69. Write a program that converts a string like "3.14" to float and uses it in a calculation
a = "3.14"
b = float(a)
r = 1
areaofcircle = b * r**2
print(areaofcircle)
print()

# 70.Write a program that uses type() and isinstance() to check types of variables.

# 71.Write a program that checks if a number is positive.
n = 10
if n > 0:
    print("Given number is positive")
else:
    print("Given number is not positive")

# 72.Write a program that checks if a number is even or odd using if-else.
n = 9
if n % 2 == 0:
    print("Even number")
elif n % 2 != 0:
    print("Odd Number")
else:
    print("Zero")

# 73. Write a program that checks if a number is divisible by 3, 5, or both, and prints the appropriate message.
x = 15
if x % 3 == 0 and x % 5 == 0:
    print("Given Number is divisible by both 3 and 5")
elif x % 3 != 0 and x % 5 == 0:
    print("Divisible by 3 but not 5")
elif x % 3 != 0 and x % 5 == 0:
    print("Divisible by 5 but not 3")
else:
    print("Not divisible by both 3 and 5")

# 74.Write a program that checks if a given year is a leap year.
a = 2024
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# 75.Write a program that reads three numbers and prints the largest using if-elif-else.
a = 10
b = 0
c = 89
if a>b and b>c:
    print("A is gearter: ",a)
elif b>a and b>c:
    print("B is gearter: ",b)
elif c>a and c>b:
    print("C is gearter: ",c)
print()

# 76. Write a program that assigns a grade (A, B, C, D, F) based on a student’s marks using if-elif-else.
a = 75
if a<=100 and a>=90:
    print("Grade A",a)
elif a<=89 and a>=70:
    print("Grade B",a)
elif a<=69 and a>=50:
    print("Grade C",a)
elif a<=49 and a>=36:
    print("Grade D",a)
else:
    print("Fail",a)

# 77.Write a program that checks if a character is a vowel or consonant.
b = "s"
if b == "a"or b=="e"or b=="i"or b=="o"or b=="u":
    print("Vowel")
else:
    print("Consonant")
print()

# or
b= "a"
if b in "aeiou":
    print("Vowel")
else:
    print("Consonant")
# 78.Write a program that checks if a character is uppercase, lowercase, digit, or special character.
a = "@"
if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Digit")
else:
    print("Special Character")

# 79.Write a program that checks if a given string is empty or not.
# a =""
# if a.isempty():
#     print("Empty")
# else:
#     print("Not empty")

# 80. Write a program that checks if a given number lies between 1 and 100 (inclusive).
a = 101
if 101>a>0:
    print("lies between 1-100, Inclusive")
else:
    print("Doesn't lies between 1-100")
# # 81. Write a program that checks whether a given string contains the word "python" (case insensitive).
# a = "pythoin"
# if a == "python":
#     print("string contains the word python")
# else:
#     print("contains the word python")
# 82. Write a program that takes a number and prints "Small" if <10, "Medium" if between 10 and 50, "Large" if >50.
a = 200
if a < 10:
    print("Small")
elif 10 >= a >= 50:
    print("Medium")
else:
    print("Large")
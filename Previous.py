# 1.Take the user’s name and age and print: "Hello <name>, you are <age> years old."
name = "Ashritha"
age = 20
print("Hello",name,"you are",age,"years old")
print("%s is %d years old." % (name, age))
print("Hello %s you are %d years old"% (name,age))

# 2.Take two integers and print their sum, difference, multiplication, and division.
n = 10
m = 20
sum = n + m
diff = n - m
mul = n * m
div = n / m
print("sum: ",sum,"difference: ",diff,"multiplication: ",mul,"division: ",div)

# 3.Input three numbers and print the largest.
a = 10
b = 100
c = 30
if a > b and a > c:
    print("Largest numebr is a: ",a)
elif b > a and b > c :
    print("Largest number is b: ",b)
else:
    print("Largest number is c: ",c) 

#4. Input a number and check whether it is positive, negative, or zero.
x = 0
if x > 0:
    print(x, " is positive number")
elif x < 0:
    print(x," is negative number")
else:
    print(x," is zero")

# 5. Input a floating-point number and round it to two decimals.
# n = float(input("Enter a decimal number: "))
n =56.455678
print(n.__round__(2))
print(round(n,2))

# 6. Input length and breadth; calculate rectangle area and perimeter.
len = 5
bre = 10
area = len * bre
perimeter = 2*(len + bre)
print("area: ",area,"perimeter: ",perimeter)

# 7. Input temperature in Celsius and convert to Fahrenheit.
cel = 56
far = (cel * 9/5) + 32
print(far)

# 8. Input two numbers and swap them (without using a third variable).
a = 10
b = 20
print("Before swaping : " "a:",a,"b:",b)
a,b = b,a
print("After Swapping: " "a:",a,"b:",b)

# 9.Input a number and print its square and cube.
n = 6
print("square: ",n ** 2,"Cube: ",n**3)

# 10.Input the marks of 5 subjects and print total, average, and percentage.
math = 60
sci = 90
soc = 60
tel = 80
hin = 90
total = math + sci + soc + tel + hin
average = total / 5
percentage = (total / 500) * 100
print("total: ",total,"average: ",average,"percentage:",percentage)

# 11.Input radius and calculate area and circumference of a circle.
r = 70
area = 3.14 * (r**2)
circumference = 2 * 3.14 * r
print("area: ",area,"circumference: ",circumference)

# 12 Input a number and check if it is even or odd.
n = 98
if n % 2 == 0:
    print(n,"is Even number: ")
else:
    print(n,"is Odd number: ")


# 13 Take two numbers and print True if first is greater than second, else False.
x = 90
y = 80
if x > y:
    print("First number is greater than second")
else:
    print("First number is not greater than second")


# Input cost price and selling price, calculate profit or loss.

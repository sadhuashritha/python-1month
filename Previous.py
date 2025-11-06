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
n = float(input("Enter a decimal number: "))
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
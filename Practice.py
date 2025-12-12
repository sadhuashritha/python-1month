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



# Write a program that asks the user for three values and prints them using an f-string i
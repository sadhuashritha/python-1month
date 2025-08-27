#Concatenate the strings "hello" and "world" into a single string.
x = 'hello'
y = 'world'
z = x + " " + y
print(z)

#Repeat the string "abc" three times.
p = "abc"
q = p * 3
print(q)

#Extract the first and last characters of the string "python".
s = "python"
firstchar = s[0]
lastchar = s[-1]
print(firstchar,lastchar)

#From the string "programming", extract the substring "progra".
a = "programming"
print(a[0:6])

#Reverse the string "hello" using slicing.
b = "hello"
print(b[::-1])

#Check whether the substring "world" exists in the string "hello world".
p = "hello world"
print("world" in p)

#Convert the string "PyThoN" into:
# all lowercase
# all uppercase
p = "pyThoN"
print(p.lower())
print(p.upper())

#Check if the string "python" starts with "py" and ends with "on".
s = "python"
print(s.startswith("py"))
print(s.endswith("on"))

#Remove extra spaces from the beginning and end of the string " hello ".
h = "   hello     "
print(h)
print(h.strip())

#Replace the word "cats" with "dogs" in the string "I like cats".
p = "I like cats"
print(p.replace("cats","dogs"))

#Find the index of the substring "for" in the string "geeksforgeeks".
g = "geeksforgeeks"
print(g.find("for"))

# #Split the string "hello world" into a list of words, and then join them with "-" as a separator.
a = "hello world"
b = a.split()
print(b)
c = "-".join(b)
print(c)
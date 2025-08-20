# Datatypes
#id() // identity

x = 5
print(id(x))
x = 10
print(id(x))
y = "hello world"
print(id(y))


a = 5 # INT
print(type(a))
print(a)

b = 5.80 #FLOAT
print(type(b))
print(b)

c = 2 + 5j #COMPLEX
print(type(c))
print(c)

d = "String" #STRING
print(type(d))
print(d)
print(d[1])

e = True #BOOL
print(type(e))
print(e)

f = ["V","S","CODE",1,2,True] #LIST
print(type(f))
print(f)
print(f[3])
print(f[2])

t = ("Geeks","for")#Tuple
print(type(t))
print(t)
print(t[1])
print(t[0])

g1 = set("Geeks For Geeks") #Set with the use of string
print(type(g1))
print(g1)
g2 = set(["Geeks","For","Geeks"]) #Set with the use of list
print(type(g2))
print(g2)

h = {1 : "Geeks", 2 : "For", 3 : "Geeks","name" : "hello"}
print(type(h))
print(type(h[1]))
print(h)
print(h[1])
print(h.get(2)) # Accessing using "GET"



# Create a tuple with 5 integers. Print the first and last element.
tup = (1,2,3,4,5,6,7)
print(tup[0])
print(tup[-1])


# Given a tuple (10, 20, 30, 40, 50), print it in reverse order.
tup = (10, 20, 30, 40, 50)
print(tuple[::-1])

# Create a tuple with different data types (string, int, float, bool). Print each element with its type.
tup1 = ("Ashritha",30,50.68,True)
for i in tup1:
    print(type(i))
print(tup1)

# Check if the number 25 exists in the tuple (10, 20, 25, 30, 35)
tup = (10, 20, 25, 30, 35)
for i in tup:
    if i == 25:
        print("exits")

# Convert the list [1, 2, 3, 4, 5] into a tuple.
li = [1, 2, 3, 4, 5]
tup2 = tuple(li)
print(tup2)

# Concatenate two tuples (1,2,3) and (4,5,6) into one tuple.
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3)

# Repeat the tuple (‘a’, ‘b’) three times.
tup = ('a','b') 
print(tup * 3)# Find the length of tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
print(len(tup))

# Count how many times 'apple' appears in the tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
count = 0
for i in tup:
    if i == 'apple':
        count += 1
print(count)

# Find the index of 'cherry' in the tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
for i in range(len(tup)):
    if tup[i] == 'cherry':
        print(i)
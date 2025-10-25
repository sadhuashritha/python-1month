# Given a list of strings containing names of students and 
# another list containing marks of corresponding students. 
# The task is to create a dictionary to store marks of students with their names (name will be unique).
names = ["john", "ala", "ilia", "sudan", "mercy"]
marks = [100, 200, 150, 80, 300]
dic = {}
for i,j in zip(names,marks):
    dic[i] = j
print(dic)

# Create a dictionary named student with keys name, age, and grade and print it.
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
print(student)

# How do you access the value of the key "age" from a dictionary named student?
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
print(student["age"])


#Write a program to change the value of "grade" from "A" to "B".
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
student["grade"] = "B"
print(student)


# Remove a key "age" from a dictionary using pop().
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
del student["age"]
print(student)

# Check whether the key "name" exists in a dictionary or not
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
for i in student.keys():
    if i == "name":
        print("The key, name exists")


# Write a Python program to get all keys from a dictionary.
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
for i in student.keys():
#for i in student: 
    print("keys: ",i)

#Write a Python program to get all values from a dictionary.
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
for i in student.values():
    print("values: ",i)

# Use a loop to print all keys and values in a dictionary.
student = {"name" : "ashritha" ,"age": 20, "grade": "A"}
for i,j in student.items():
    print(i,": ",j)
# Create an empty dictionary and add 3 key-value pairs using assignment (dict[key] = value).
dic = {}
dic[1] = "ashritha"
dic["age"] = 20
dic["a"] = "Grade A"
print(dic)


# Write a Python program to merge two dictionaries into one.
d1 = {1:"A",2:"B"}
d2 = {2:"C",3:"D"}
d3 = d1 | d2
# or
d4 = {**d1, **d2}
print(d3)
print(d4)

# Write a Python program to find the key with the maximum value in a dictionary.
dic = {"A":1,"B":15,"C":100,"D":45,"E":50,"F":46}
max = 0
for i,j in dic.items():
    if j > max:
        max = j
        key = i
print(key)

# Write a Python program to count the number of keys in a dictionary.
dic = {1:"A",2:"B",3:"C",6:"D",8:"E",7:"F"}
count = 0
for i in dic:
    count += 1
print(count)

# Given a dictionary { 'a': 10, 'b': 20, 'c': 30 }, increase all values by 5
dic = { 'a': 10, 'b': 20, 'c': 30 }
for i,j in dic.items():
    dic[i] = (j + 5)
print(dic)


# Write a Python program to sort a dictionary by its keys.
dic = {"B": 15, "A": 1, "E": 50, "C": 10, "D": 45}
print(dict(sorted(dic.items())))

#Write a Python program to sort a dictionary by its values(ascending).
dic = {"B": 15, "A": 1, "E": 50, "C": 10, "D": 45}
sol = dict(sorted(dic.items(), key = lambda item : item[1]))
print(sol)


#Convert two lists — one of keys and one of values — into a single dictionary.
keys = ["A", "B", "C", "D"]
values = [10, 20, 30, 40]
res= {}
for i in range(len(keys)):
    res[keys[i]] = values[i]
print(res)
# or
res1 = dict(zip(keys,values))
print(res1)


# Write a program to find the sum of all values in a dictionary.
dic = {"B": 15, "A": 1, "E": 50, "C": 10, "D": 45}
sum = 0
for i in dic.values():
    sum += i
print(sum)


#  Write a Python program to create a dictionary from a string, where keys are characters and values are their frequencies. Example: "apple" → { 'a':1, 'p':2, 'l':1, 'e':1 }
alph = "hello"
freq = {}
for char in alph:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

# Write a Python program to remove all keys with None or empty string values. explain these two questions
dic = {"B": 15, "A": "", "E": 50, "C": None, "D": ""}
dic2 = {}
for i,j in dic.items():
    if j != None and j != "":
        dic2[i] = j
print(dic2)


# Write a Python program to invert a dictionary — swap keys and values.
dic = {"B": 15, "A": 1, "E": 50, "C": 10, "D": 45}
dic2 = {}
for i,j in dic.items():
    dic2[j] = i
print(dic2)

# Write a Python program to combine two dictionaries, adding values for common keys.
# Example:
# { 'a': 10, 'b': 20 }, { 'b': 30, 'c': 40 } → { 'a': 10, 'b': 50, 'c': 40 }
dic1 = {'a': 10, 'b': 20}
dic2 = {'b': 30, 'c': 40}
ans = dic1.copy()
for i,j in dic2.items():
    if i in ans:
        ans[i] += j
    else:
        ans[i] = j
print(ans)


# Given a list of strings containing names of students and 
# another list containing marks of corresponding students. 
# The task is to create a dictionary to store marks of students with their names (name will be unique).
names = ["john", "ala", "ilia", "sudan", "mercy"]
marks = [100, 200, 150, 80, 300]
dict = {}
for i,j in zip(names,marks):
    dict[i] = j
print(dict)

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
dict = {}
dict[1] = "ashritha"
dict["age"] = 20
dict["a"] = "Grade A"
print(dict)

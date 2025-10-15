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

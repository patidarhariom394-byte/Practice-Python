a={1,2,3}
b={1,2,3,4}
print(a.union(b))

a={1,2,3}
b={1,2,3,4}
print(a.intersection(b))

student={
  "Name" : "Tarun",
  "Age" : "20",
  "Course" : "Python"
}

print(student)

print(student["Name"])

print(student.keys())
print(student.values())
print(student.items())
student.update({"Age":25})
print(student)

student.pop("Age")
print(student)


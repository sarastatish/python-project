courses = ["MIT","cybersecurity","datascience"]
print(courses)
#acessing an element in an array
print(courses[0])
#looping through an array
for y in courses:
    print("course is",y)

# adding a new element
courses.append("android development")
print(courses)
#removing item
courses.remove("MIT")
print(courses)
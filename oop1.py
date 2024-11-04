class student:
    #properties/variables/attributes
    name = "Joe"
    age = 23
    #behaviours/functions
    def study(self):
        print("student is studying")

student1 = student() #creating object
student1.study()

print(student1.study)
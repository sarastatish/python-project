class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def movement(self):
        print("person is moving")

a = person("Joe",34,"male")
print(a.name)
print(a.age)
print(a.gender)

b = person("mary",23,"female")
print(b.name)
print(b.age)
print(b.gender)
c = person("john",45,"male")
print(c.name)
print(c.age)
print(c.gender)

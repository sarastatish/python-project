

number = 25 # integer
second = 56.78 #float
text = "Hello there"#string
isPythonInteresting = True #boolen
#datastructeres in python - multiple values stored in a single variable
cars = ["toyota","nissan","VW"] #List - ordered and changable
fruits = ("banana","orange","apple")#tuple
countries = {"Kenya","Tunisia","Algeria"}#set-unordred and unchangable
student = {
    "first_name":"Sarsata",
    "age": 34,
    "course":"web development",
    "nationality":"Kenyan"
}#dictionary-key and value pair
print(cars)
print(fruits)
print(countries)
print(student)
print(student["nationality"])

print(number)
print(second)
print(text)
print(isPythonInteresting)

#determining a data type
print(type(countries))
print(type(student))
print(type(second))

#typecasting - process of converting  one data  type to another
print(float(number))
print(int(second))


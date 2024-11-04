try:
    print(number)
except:
    print("A error has occurred")


num1 = 39
num2 = 0
try:
    print(num1 / num2)
except:
    print("zero division error")
finally:
    print("success")

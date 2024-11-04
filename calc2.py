print("choose an operator")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operator = input("Enter an operator: ")

if operator == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("the sum is:", num1 + num2)
elif operator == "2":
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print("The diffrence is:", num1 - num2)
elif operator == "3":
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print("The product is:", num1 * num2)
elif operator == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Error:Division by zero is impossible")
        else:
            print("The division is:",num2/num1)
else:
        print("invalid input operator")

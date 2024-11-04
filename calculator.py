operator = input("Choose an operator between {- + / * }: ")

firstnum = float(input("Enter the First Number: "))

secondnum = float(input("Enter the Second Number: "))

if operator == "-":
    print(f"The answer to {firstnum} less {secondnum} is {firstnum - secondnum}")
elif operator == "+":
    print(f"The answer to {firstnum} added to {secondnum} is {firstnum + secondnum}")
elif operator == "/":
    if secondnum == 0:
        print("Error: Division by zero is undefined.")
    else:
        print(f"The answer to {firstnum} divided by {secondnum} is {firstnum / secondnum}")
elif operator == "*":
    print(f"The answer to {firstnum} multiplied by {secondnum} is {firstnum * secondnum}")
else:
    print("Please choose a valid operator between +, *, -, /")

print("Welcome to the calculator")
print('if you wish to exit, enter "exit"')
print("A)addition, B)subtraction C)multiplication D)division")

Number_1 = ""
while True:
    if not Number_1:
        Number_1 = input("Enter the first number: ")
        if Number_1.lower() == "exit":
            break
        Number_1 = int(Number_1)
    operation = input("Enter the operation: ")
    if operation.lower() == "exit":
        break
    Number_2 = input("Enter the second number: ")
    if Number_2.lower() == "exit":
        break
    Number_2 = int(Number_2)

    if operation.upper() == "A":
        Number_1 += Number_2
    elif operation.upper() == "B":
        Number_1 -= Number_2
    elif operation.upper() == "C":
        Number_1 *= Number_2
    elif operation.upper() == "D":
        Number_1 /= Number_2
    else:
        print("Operation not validated")
    print(f"The result is {Number_1}")

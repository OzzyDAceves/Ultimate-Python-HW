EXIT = ''
while EXIT != 'E':
    print("Enter the first number: ")
    Number_1 = input()

    if Number_1 == "" or Number_1 == " ":
        print("Please, enter the firs number")
        Number_1 = input()
        Number_1 = int(Number_1)
    elif Number_1 != "" or Number_1 != " ":
        Number_1 = int(Number_1)
    else:
        print("Value error")

    print("What operation do you want to do?, A) addition, B) subtraction C) multiplication D) division E) exit")
    option = input()
    option = option.upper()

    if option == 'A':
        print("Enter the second number: ")
        Number_2 = input()
        Number_2 = int(Number_2)
        addition = Number_1 + Number_2
        print("The value is: ", addition)
    elif option == 'B':
        print("Enter the second number: ")
        Number_2 = input()
        Number_2 = int(Number_2)
        subtraction = Number_1 - Number_2
        print("The value is: ", subtraction)
    elif option == 'C':
        print("Enter the second number: ")
        Number_2 = input()
        Number_2 = int(Number_2)
        multiplication = Number_1 * Number_2
        print("The value is: ", multiplication)
    elif option == 'D':
        print("Enter the second number: ")
        Number_2 = input()
        Number_2 = int(Number_2)
        division = Number_1 / Number_2
        print("The value is: ", division)
    elif option == 'E':
        EXIT = 'E'
    else:
        print("The operation its incorrect")

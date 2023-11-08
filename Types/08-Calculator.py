
print("Enter the first number: ")
Number_1 = input()
print("Enter the second number: ")
Number_2 = input()

Number_1 = int(Number_1)
Number_2 = int(Number_2)

addition = Number_1 + Number_2
subtraction = Number_1 - Number_2
multiplication = Number_1 * Number_2
division = Number_1 / Number_2

message = f"""
The operations have been successful, 
\nfor numbers {Number_1} and {Number_2}.
\nthe result of the addition is {addition}.
\nthe result of the subtraction is {subtraction}.
\nthe result of the multiplication is {multiplication}.
\nthe result of the division is {division}.
"""
print(message)

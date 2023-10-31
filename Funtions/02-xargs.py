def addition(*numbers):
    """Function to addition numbers"""
    result = 0
    for number in numbers:
        result += number
    print(result)


addition(2, 3, 4)
addition(4, 5)
addition(22, 12, 14, 0, 5)

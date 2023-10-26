search = 3

for number in range(5):
    print(number)
    if number == search:
        print("Found", search)
        break
else:
    print("Not found")

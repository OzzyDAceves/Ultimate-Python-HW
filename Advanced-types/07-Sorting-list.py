Numbers = [2, 15, 42, 4, 0, 13, 99]
Numbers_2 = [5, 10, 44, 81, 9, 23]
Numbers_3 = [22, 18, 14, 65, 71, 88]
Users = [[4, "Ozzy"], [5, "Yuks"], [23, "Braulio"], [6, "Paco"]]
Users_2 = [["César", 3], ["Rocha", 1], ["Ozzy", 2]]

Numbers.sort()
print(Numbers)

Numbers_2.sort(reverse=True)
print(Numbers_2)

Numbers_4 = sorted(Numbers_3)
print(Numbers_3)
print(Numbers_4)
Numbers_4 = sorted(Numbers_3, reverse=True)
print(Numbers_4)

Users.sort()
print(Users)


def Sorting(item):
    return item[1]


Users_2.sort(key=Sorting)
print(Users_2)

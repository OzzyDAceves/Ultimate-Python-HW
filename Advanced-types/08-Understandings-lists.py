Users = [[4, "Ozzy"], [5, "Yuks"], [23, "Braulio"], [6, "Paco"]]
Users_2 = [["Ozzy", 9], ["Paolo", 8], ["Minnuti", 10], ["César", 7]]
Users_3 = [["Petu", 10], ["Fausto", 6], [
    "Dogo", 5], ["Tazmania", 9], ["Merlyn", 10]]
USERS = [["0014", 9], ["0004", 8], ["1341", 10], ["0103", 7]]
USERS_2 = [["X104", 9], ["Y920", 8], ["1341", 10], ["0103", 7]]

Names = []
for User in Users:
    Names.append(User[1])
print(Names)

# Function map, same as lines 16 and 17
NAMES = list(map(lambda USER: USER[0], USERS))
print(NAMES)

Names_2 = [User_2[0] for User_2 in Users_2]
print(Names_2)

# Function filter, same as lines 24 and 25
Less_Users = list(filter(lambda USER_2: USER_2[1] > 8, USERS_2))
print(Less_Users)

Names_3 = [User_3[0] for User_3 in Users_3 if User_3[1] > 7]
print(Names_3)

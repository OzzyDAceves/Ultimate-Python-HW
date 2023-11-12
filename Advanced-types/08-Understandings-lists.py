Users = [[4, "Ozzy"], [5, "Yuks"], [23, "Braulio"], [6, "Paco"]]
Users_2 = [["Ozzy", 9], ["Paolo", 8], ["Minnuti", 10], ["César", 7]]
Users_3 = [["Petu", 10], ["Fausto", 6], [
    "Dogo", 5], ["Tazmania", 9], ["Merlyn", 10]]

Names = []
for User in Users:
    Names.append(User[1])
print(Names)

Names_2 = [User_2[0] for User_2 in Users_2]
print(Names_2)

Names_3 = [User_3[0] for User_3 in Users_3 if User_3[1] > 7]
print(Names_3)

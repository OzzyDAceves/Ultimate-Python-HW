Numbers_1 = [1, 2, 3, 4]
Numbers_2 = [5, 6]
print(*Numbers_1, *Numbers_2)

combination = ["Petu", *Numbers_1, "Merlyn", *Numbers_2]
print(combination)

point_1 = {"X": 15, "Y": "Dogo"}
point_2 = {"Y": 9}
new_point = {**point_1, **point_2}
combination_2 = {"Name": "Petu", **point_1, "Name_2": "Dogo", **point_2}
print(new_point)
print(combination_2)

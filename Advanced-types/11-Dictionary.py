Point = {"X": 25, "Y": 50}
print(Point)
print(Point["X"])
print(Point["Y"])

Point["Z"] = 45
print(Point)
if "W" in Point:
    print("I've found W: ", Point["W"])

print(Point.get("X"))
print(Point.get("W", "Doesn't exist"))

del Point["X"]
print(Point)

Point["X"] = 25
for value in Point:
    print(value, Point[value])

for value in Point.items():
    print(value)

for key, value in Point.items():
    print(key, value)

users = [
    {"ID": 1, "Name": "Petu"},
    {"ID": 2, "Name": "Merlyn"},
    {"ID": 3, "Name": "Dogo"},
    {"ID": 4, "Name": "Fausto"}
]

for user in users:
    print(user["Name"])

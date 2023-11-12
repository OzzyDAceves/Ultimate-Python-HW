Pet = [
    "Petu",
    "Merlyn",
    "Dogo",
    "Fausto",
    "Tazmania",
    "Merlyn"]

#   Pet.insert(5, "Kenich")
Pet.append("Kenich")  # Adds an item to the end of the list
print(Pet)

Pet.remove("Merlyn")
print(Pet)
Pet.pop(2)  # If no value is assigned, it deletes the last item in the list.
print(Pet)
del Pet[3]
print(Pet)
Pet.clear()  # Removes all items from the list
print(Pet)

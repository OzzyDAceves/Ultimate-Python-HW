Numbers = (1, 2, 3) + (3, 5, 6)
print(Numbers)

Not_modify = tuple([1, 11, 22, 33])
print(Not_modify)

less_numbers = Numbers[:2]
print(less_numbers)

first, second, *others = Numbers
print(first, second, others)

for i in Numbers:
    print(i)

list_numbers = list(Numbers)
list_numbers[0] = "Petu"
print(list_numbers)

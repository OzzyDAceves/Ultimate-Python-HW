Numbers = [1, 2, 3]

First, Second, Third = Numbers
print(First, Second, Third)

Only_first, *Others = Numbers
print(Only_first)
print(Others)

Numbers_2 = list(range(1, 11))
First, *Others, Tenth = Numbers_2
print(First, Others, Tenth)

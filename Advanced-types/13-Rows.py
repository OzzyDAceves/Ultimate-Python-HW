from collections import deque

row = deque([1, 2])
row.append(3)
row.append(4)
row.append(5)
print(row)
row.popleft()
print(row)
row.popleft()
print(row)
row.popleft()
print(row)
row.popleft()
print(row)
row.popleft()
if not row:
    print("empty row")

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
last_element = queue.pop()
print(last_element)
print(queue)
print(queue[-1])
queue.pop()
queue.pop()
if not queue:
    print("Empty queue")

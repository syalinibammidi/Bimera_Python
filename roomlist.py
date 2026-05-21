import random
lists = []
count = 0
while count < 10:
    length = random.randint(1,25)
    breadth = random.randint(1,20)
    rectangle = [length, breadth, length, breadth]
    lists.append(rectangle)
    count += 1
print(lists)

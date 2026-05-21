#pen length =100m need ponints for every 4.5 , ho wmay points are placed by taking start as 4.5 and find end value usinf for loop, 
len=100
dist=4.5
count=1#place at initail place also
for point in range(1, int(len / dist) + 1):
    position = point * dist
    print(position)
    count += 1

print("Total points placed:", count)
print("End value:", position)

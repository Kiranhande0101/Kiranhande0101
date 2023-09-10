import math
def perfectSquare(x):
    root = math.sqrt(x)
    if int(root + 0.5) ** 2 == x:
        return 1
    else:
        return 0
num =[25,77,54,81,34]
count = 0 
print(num)
for i in num:
    if perfectSquare(i) == 1:
        count += 1
print(count)''''''
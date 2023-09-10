rows=int(input())
num=1
for x in range(rows):
    for y in range(x+1):
        print(num,end=" ")
        num=num+2
    print()
 
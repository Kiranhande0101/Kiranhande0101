rows=int(input())
num=1
for i in range(rows-1):
    for j in range(i):
        print(" ",end=" ")
    for z in range(rows-i):
        print(num,end=" ")
        num=num+1
    print()
        
    
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end=" ")
    for z in range(i+1):
        print(num,end=' ')
        num=num+1
    print()
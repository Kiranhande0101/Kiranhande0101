rows=int(input())
for i in range(rows-1):
    num=1
    for j in range(i,rows):
        print(num,end=" ")
        num=num+1
    print()
        
    
for i in range(rows):
    num=1
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print()
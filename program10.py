rows=int(input())
for i in range(rows-1):
    for j in range(i,rows):
        if i%2==0:
            print('#',end=' ')
        else:
            print("*",end=" ")
    print()
        
    
for i in range(rows):
    for j in range(i+1):
        if i%2==0:
            print('*',end=' ')
        else:
            print("#",end=" ")
        
    print()
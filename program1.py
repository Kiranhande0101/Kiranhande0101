n=8

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
        
    for j in range(i,n):
        if j==0:
            print(" ",end=" ")
        else:
            print("*",end="")
            
    for j in range(i):
        if i==0:
            print(" ",end=" ")
        else:
            print("*",end="")
            
    print()
    
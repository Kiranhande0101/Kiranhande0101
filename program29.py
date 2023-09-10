rows=int(input("enter the number of rows"))
for x in range(rows):
    for y in range(rows):
        if rows//2==x:
            print("-",end=" ")
        elif rows//2==y:
            print("-",end=" ")
        else:
            print("*",end=" ")
        if (x==2 or y==2 ) or (x==3 or y==3 ):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
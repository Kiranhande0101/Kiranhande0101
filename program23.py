rows=int(input("enter rows"))
for x in range(rows):
    for y in range(rows-x-1):
        print(" ",end=" ")
    for z in range(rows):
        print("*",end=" ")
    print()
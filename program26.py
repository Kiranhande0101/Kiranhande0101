rows=int(input("enter rows"))
 #cols=int(input("enter cols"))
for x in range(rows):
    for y in range(rows+1):
        print("*",end=" ")
        if (x==2 and y==2 ) or (x==3 and y==3 ):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
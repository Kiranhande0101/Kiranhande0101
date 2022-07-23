rows=int(input("enter rows"))

for x in range(rows):
    num=1+x
    for y in range((rows-x)):
        print(" ",end=" ")
    for z in range(x+1):
        print(num*(z+1),end=" ")
    print()
            
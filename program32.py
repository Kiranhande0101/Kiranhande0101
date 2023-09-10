rows= int(input("Enter rows: "))
for i in range(rows):
    for y in range(i):
        print(" ",end=" ")
    for z in range((rows*2)-(i*2)-1):
        print("*",end=" ")
    print()
for i in range(1,rows):
    for j in range(rows-i-1):
        print(" ",end=" ")
    for z in range(i*2+1):
        print("*",end=" ")
    print()
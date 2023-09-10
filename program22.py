
rows=int(input("enter rows"))
cols=int(input("enter cols"))
for x in range(rows):
    for y in range(cols):
        print("*",end=" ")
    print()    

for x in range(rows):
    for y in range(rows-x-1):
        print(" ",end=" ")
    for z in range(rows):
        print("*",end=" ")
    print()
for x in range(2):
    for y in range(3):
        print("*",end=" ")
    print()
        
for x in range(rows):
    for y in range(cols):
        print("*",end=" ")
    print()   
 
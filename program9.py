rows=int(input("enter rows"))

for x in range(rows):
    num=97
    for y in range(rows-x-1):
        print(" ",end=" ")
    for z in range(x+1):
        if x%2==0:
            print(chr(num),end=" ")
        else:
            print(num-96,end=" ")
        num=num+1
            
    print()
            
        
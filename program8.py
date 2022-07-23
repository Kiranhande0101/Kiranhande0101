rows=int(input("enter rows"))

for x in range(rows):
    c=x+97
    num=x+1
    for y in range((rows-x)-1):
        print(" ",end=" ")
    for z in range(x+1):
        if x%2==0:
            data=chr(c)
            print(data,end=" ")
            c=c-1
        else:
            print(num,end=" ")
            num=num-1
    print()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
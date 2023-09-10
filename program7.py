rows=int(input())
for i in range(rows):
    for y in range(i+1):
        if i%4==0:
            print("*",end=" ")
        elif i%3==0:
            print("$",end=" ")
        elif i%2==0:
            print("+",end=" ")
        else:
            print("#",end=" ")
    print()
        
            
            
            
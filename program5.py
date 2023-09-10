'''5 4 3 2 1
   D C B A
   3 2 1
   B A
   1'''



rows=int(input("enter num of rows"))

for x in range(rows):
    num=5-x
    num2=69-x
    for j in range(rows-x):
        data=chr(num2)
        if x % 2==0:
            print(num,end=" ")
        else:
            print(data,end=" ")
        num=num-1
        num2=num2-1
        
    print()
            
    
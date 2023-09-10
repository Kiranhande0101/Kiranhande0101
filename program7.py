'''          9
         18  27
    36   45  54
63  72   81  90'''

from re import X


rows=int(input("enter rows"))
num=1
for i in range(rows):
    for y in range(rows-i-1):
        print("  ",end="  ")
    for z in range(i+1):
             print(num*9,end="  ")
             num=num+1
        
    print()
    

     
    
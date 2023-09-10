'''d c b a 
   c b a
   b a 
   a '''
from re import A


rows=int(input("enter rows"))
for i in range(rows):
    num=100-i
    for j in range(rows-i):
        data=chr(num)
        print(data,end=" ")
        num=num-1
    print()
        
    
   
#  1   4   9
# 16  25  36
# 49  64  81

rows=int(input("Enter the no.of rows: "))  
cols=int(input("Enter the no.of columns: "))  
n=1
sum=0
for x in range(rows):
    for y in range(cols):
        print(n*n,end=" ")
        sum+=n*n
        n=n+1
    print() 
print(sum)       
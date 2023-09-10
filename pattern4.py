# 1  2  3
# 4  5  6
# 7  8  9
#right diagonal+ left diagonal
rows=int(input("Enter the no. of rows: "))
cols=int(input("Enter the no. of columns: "))
n=1
sum=0
for x in range(rows):
    for y in range(cols):
        print(n,end=" ")
        if (x==y) or (x+y)==rows-1:
            sum+=n
        n=n+1
    print()  
print(sum)  
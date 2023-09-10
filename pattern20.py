# 1
# 22
# 333
# 4444
rows=int(input("Enter the number of rows: "))
n=1
for x in range(rows):
    for y in range(x+1):
        print(n,end=" ")
        
    n=n+1
    print()
# 1
# 21
# 321
# 4321

rows=int(input("Enter the number of rows: "))
for x in range(rows):
    n=x+1
    for y in range(x+1):
        print(n,end=" ")
        n=n-1
    print()    
# 1234
# 123
# 12
# 1

rows=int(input("Enter the number of rows: "))
for x in range(rows):
    n=1
    for y in range(rows-x):
        print(n,end=" ")
        n=n+1
    print() 
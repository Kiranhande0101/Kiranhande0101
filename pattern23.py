# ***1
# **12
# *123
rows=int(input("Enter the number of rows: "))
for x in range(rows):
    n=1
    for y in range(rows-x-1):
        print("*",end=" ")
    for y in range(x+1):
        print(n,end=" ")
        n=n+1
    print()        
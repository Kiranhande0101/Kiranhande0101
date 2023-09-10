# 54321
#  4321
#   321
#    21
rows=int(input("Enter the number of rows: "))

for x in range(rows):
    n=rows-x
    for y in range(x):
      print(" ",end=" ")
    for y in range(rows-x):
        print(n,end=" ")
        n=n-1
    
    print()      
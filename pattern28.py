#    *
#   ***
#  *****
# *******
rows=int(input("Enter the number of rows: "))
for x in range(rows):
    for y in range(rows-x-1):
        print(" ",end=" ")
    for x in range(x*2+1):
        print("*",end=" ")
    print()        
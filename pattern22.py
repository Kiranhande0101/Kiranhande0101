# from abc import ABC


# A
# AB
# ABC
# ABCD
rows=int(input("Enter the number of rows: "))
for x in range(rows):
    c=65
    for y in range(x+1):
        print(chr(c),end=" ")
        c=c+1
    print()    
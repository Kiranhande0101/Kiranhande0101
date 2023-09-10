# from abc import ABC


# ABCD
# ABC
# AB
# A

rows=int(input("Enter the number of rows: "))
for x in range(rows):
    c=65
    for y in range(rows-x):
        print(chr(c),end=" ")
        c=c+1
    print()    
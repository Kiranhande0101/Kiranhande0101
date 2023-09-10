# A  C  E
# G  I  K
# M  O  Q
rows=int(input("Enter the no of rows: "))
cols=int(input("Enter the no of cols: "))
c=65
for x in range(rows):
    for y in range(cols):
        print(chr(c),end=" ")
        c=c+2
    print()    
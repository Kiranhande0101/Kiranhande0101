# A  B  C  
# D  E  F
# G  H  I

rows=int(input("Enter the no of rows: "))
cols=int(input("Enter the no of columns: "))
c=65
for x in range(rows):
    for y in range(cols):
        print(chr(c),end=" ")
        c=c+1
    print()    
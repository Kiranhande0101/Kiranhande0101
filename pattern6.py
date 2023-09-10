# I  H  G      i  h  g
# E  F  D  OR  e  f  d
# C  B  A      c  b  a
rows=int(input("Enter the no of rows: "))
cols=int(input("Enter the no of columns: "))
char=ord(input("Enter the alphabet from which reverse: "))
for x in range(rows):
    for y in range(cols):
        print(chr(char),end=" ")
        char=char-1
    print()    
# AAAAAAA
# BBBBBB
# CCCCC 
# DDDD 
# EEE
# FF
# G
rows=int(input("Enter the no of rows: "))
c=65
for x in range(rows):
    for y in range(rows-x):
        print(chr(c),end=" ")
    c=c+1
    print()      
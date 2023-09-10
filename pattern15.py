# from termios import CBAUD


# A
# 21
# CBA
# 4321
rows=int(input("Enter the number of rows: "))
for x in range(rows):
    c=x+65
    n=x+1
    for y in range(x+1):
        if x%2==0:
            print(chr(c),end=" ")
            c=c-1
        else:
            print(n,end=" ")
            n=n-1
    print()        
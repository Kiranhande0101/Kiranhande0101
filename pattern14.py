# from termios import CBAUD
# from zmq import BACKLOG


# A
# BA
# CBA
# DCBA
rows=int(input("Enter the number of rows: "))
for x in range(rows):
    c=65+x
    for y in range(x+1):
        print(chr(c),end=" ")
        c=c-1
    print()    
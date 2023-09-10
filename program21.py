rows=int(input("enter rows"))
for i in range(rows):
    for j in range(i,rows-1):
        print('*',end=' ')
    print()
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()
rows=int(input("enter number rows: "))
cols=int(input("enter number cols: "))
for i in range(rows):
    num=i+1
    for j in range(cols):
        print(num,end=" ")
        num=num+4
        num=num-1
    print()
    
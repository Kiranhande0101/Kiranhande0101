rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print("*",end="")
    for j in range(0, i):
        if j==0 or i==0:
            print("*",end=" ")
        else:
            print(" ", end = " ")
    print()
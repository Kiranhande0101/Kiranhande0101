# A
# AA
# AAA
rows=int(input("Enter the number of rows: "))
# cols=int(input("Enter the number of columns: "))
for x in range(rows):
    for y in range(x+1):
        print("A",end=" ")
    print()    
        
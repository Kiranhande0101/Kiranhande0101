# *
# **
# ***
# ****

rows=int(input("Enter the number of rows: "))
for x in range(rows):
    for y in range(x+1):
        print("*",end=" ")
    print()    
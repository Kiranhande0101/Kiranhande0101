# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

rows=int(input("Enter the number od rows: "))
for x in range(rows):
    for y in range(rows-x):
        print("*",end=" ")
    print()    
rows = 5
k = 2 * rows - 2
for i in range(rows):
    for j in range(2 * rows - 2):
        print(end=" ")
    k=k+1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(rows - 2, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
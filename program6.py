rows=int(input())

for x in range(rows):
    num=65+x
   # num2=97+x
    for j in range(x+1):
        if x%2==0:
            print(chr(num),end=" ")
        else:
            print(chr(num+32),end=" ")
    print()
            
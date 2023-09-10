'''D4 C3 B2 A1
   D4 C3 B2 A1
   D4 C3 B2 A1
   D4 C3 B2 A1'''
   
rows=int(input("enter no of rows"))

for i in range(rows):
    n=4
    a=68
    for j in range(rows):
        print(chr(a)+str(n),end=" ")
        n=n-1
        a=a-1
    print()
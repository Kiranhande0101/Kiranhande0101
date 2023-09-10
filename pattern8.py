# A  B  C 
# 4  5  6
# G  H  I 
rows=int(input("Enter the no.of rows: "))
cols=int(input("Enter the no.of columns: "))
c=65
n=1
for x in range(rows):
    for y in range(cols):
        if x%2==0:
            print(chr(c),end=" ")
           
        else:
            print(n,end=" ")
        n=n+1
        c=c+1
           
    print()            
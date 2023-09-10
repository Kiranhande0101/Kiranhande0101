# 17  15  13
# 11  9   7
# 5   3   1
rows=int(input("Enter the no.of rows: "))
cols=int(input("Enter the no.of columns: "))
n=int(input("Enter the last number: "))
for c in range(rows):
     while n>0:
      for y in range(cols):
        print(n,end=" ")
        n=n-2
      print()   
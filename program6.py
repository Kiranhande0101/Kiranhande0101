'''A
   B 2
   C 3 C
   D 4 D 4'''
rows=int(input("enter rows"))

for x in range(rows):
       num=x+65
       for y in range(x+1):
              if y%2==0:
                     print(chr(num),end=" ")
              else:
                     print(num-64,end=" ")
   
       print()


# *  *  *
# A  B  C
# 1  2  3
# *  *  *

# rows=int(input("Enter the no of rows: "))
# cols=int(input("Enter the no of columns: "))
# c=65
# n=1
# for x in range(rows):
#     for y in range(cols):
#         if x%3==0:
#             print("*",end=" ")
#         elif x%2!=0:
#             print(chr(c),end=" ")
#             c=c+1
#         else:
#             print(n,end=" ")  
            # n=n+1
                     
    # print()  

# *  *  *
# A  B  C
# 1  2  3
# *  *  *
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
c=65
n=1
for x in range(rows):
    for y in range(cols):
        if x%3==0:
          print("*",end=" ")
        elif x%2==0:
            print(chr(c),end=" ")
            c=c+1 
        elif x%2!=0:
            print(n,end=" ")
            n=n+1
               
    print()        
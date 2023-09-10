''' A b C
    d E f
    G h I'''


rows=int(input("enter number rows: "))
a=65
c=1
b=33
for i in range(rows):
    for j in range(rows):
        if c%2!=0:
            print(chr(a),end=" ")
            a=a+b
        else:
            print(chr(a),end=" ")
            a=a-(b-2)
        c=c+1
     
    print()
    

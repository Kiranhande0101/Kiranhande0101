'''    * *
       * *
   * * * * * *
       * *
       * *   
       '''
rows=int(input("enter rows"))
for x in range(rows):
    for y in range(rows):
        if (x==2 or y==2 ) or (x==3 or y==3 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
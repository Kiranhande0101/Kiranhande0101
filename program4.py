rows=4
for i in range(rows):
    num=68
    for j in range(i+1):
        data=chr(num)
        print(data,end=" ")
        num=num-1
    print()
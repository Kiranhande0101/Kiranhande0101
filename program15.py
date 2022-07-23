'''WAP is print alternative numbers in reverse order between 15 to 30'''
i1=int(input("start"))
i2=int(input("end"))

for x in range(i1,0,i2-1):
    if x%2==0:
        print(x,end=" ")

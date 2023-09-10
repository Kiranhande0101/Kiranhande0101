'''rows=int(input("enter rows"))
for i in range(rows):
    print(" "*(i+1)+"*"((2*(rows-1)-i))-1)
for i in range(rows):
    print(" "*(rows-i-1)+"*"*((2*i)+1))'''
num=int(input("enter rows"))

for i in range(num):
    print(" "*(i+1)+"*"*((2*((num-1)-i))+1))
for i in range(1,num):
    print(" "*(num-i)+"*"*((2*i)+1))
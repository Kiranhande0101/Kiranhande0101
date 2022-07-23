'''write a program to print even number which are divisible by 5 in given range i1=1,i2=30'''
i1=int(input("enter start "))
i2=int(input("input start "))

for x in range(i1,i2+1):
    #if(x%2==0):
        if(x%5==0):
            print(x,end=" ")
            
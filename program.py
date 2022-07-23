'''WAP a program that prints a niven number ranging in 1 to 100 '''



start=int(input("enter value"))
end=int(input("enter value"))
sum=0
for x in range(start,end+1):
    temp=x
    sum=0
    while x!=0:
        rem=x%10
        sum+=rem
        x=x//10
    if(temp%sum==0):

         print(temp,end=" ")
               
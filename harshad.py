# 11=1+1=2
# 11/2==0
# 78=7+8=78/15==0:

for x in range(1,10):
  temp=x  
  sum=0
  while x!=0:
   rem=x%10
   sum=sum+rem
   x=x//10
  if temp%sum==0:
      print(temp,end=" ")
'''write a program to take chr as input,but only print
chr do not print sprcial chr'''
import array
arr=array.array("u",[])
arr1=array.array("u",[])
size=int(input("enter the size of array: "))
for i in range(size):
    elements=input("enter the elements of array: ")
    arr.append(elements)
for x in arr:
    if(ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
        arr1.append(x)
print(arr1)

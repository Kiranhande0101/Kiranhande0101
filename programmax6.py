import array
arr=array.array("i",[1,43,65,71,89,55])
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]

print(f"min number from array={max}")
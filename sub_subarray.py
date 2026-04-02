arr=[5,23,13]
min=float('inf')
for i in range(len(arr)):
    sub=0
    for j in range(i,len(arr)):
        sub=sub-arr[j]
        if sub<min:
            min=sub
print(min)
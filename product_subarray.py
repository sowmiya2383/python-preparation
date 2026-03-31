arr=list(map(int,input().split()))
max=arr[0]
for i in range(len(arr)):
    mul=1
    for j in range(i,len(arr)):
        mul=mul*arr[j]
        if mul>max:
            max=mul
print(max)
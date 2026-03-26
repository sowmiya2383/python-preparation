n=int(input())
arr=list(map(int,input(f"Enter {n} elements:").split()))
temp=arr[0]
count=0
for i in range(n):
    if arr[i]>=temp:
        count+=1
print(count)
    
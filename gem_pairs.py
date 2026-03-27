n=int(input())
arr=list(map(int,input().split()))
k=int(input())
used = [False] * n
count=0
for i in range(n):
    if used[i]:
        continue
    for j in range(i+1,n):
        if used[j]:
               continue
        if arr[i]+arr[j]==k:
            count+=1
            used[i] = True
            used[j] = True
            break 
print(count)
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            used=[False]*n
            count+=1
print(used)

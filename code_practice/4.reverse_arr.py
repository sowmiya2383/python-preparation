n=int(input())
arr=list(map(int,input().split()))
res=[]
for i in range(-1,0-n-1,-1):
    res.append(i)
    print(arr[i],end=' ')
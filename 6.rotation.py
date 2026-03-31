arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n=len(arr1)
if arr1==arr2:
    print('0')
else:
    res=-1
    for i in range(1,n):
        left=arr1[i:]+arr1[:i]
        if left==arr2:
            res=i
            break
        right=arr1[-i:]+arr1[:-1]
        if right==arr2:
            res=i
            break
print(res)
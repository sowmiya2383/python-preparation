n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if n==0 or n==1:
    print(-1,-1)
else:
    print("2rd smallest:",arr[1])
    print("2rd largest:",arr[n-2])
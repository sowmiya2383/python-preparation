n=int(input())
arr=list(map(int,input().split()))
date=int(input())
fine=int(input())
count=0
for i in arr:
    if date%2==0:
        if i%2!=0:
            count+=1
    else:
         if i%2==0:
            count+=1
amt=count*fine
print(amt)
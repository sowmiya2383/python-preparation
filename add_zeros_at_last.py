n=int(input())
arr=list(map(int,input().split()))
lst=[]
count=0
for i in arr:
    if i!=0:
        lst.append(i)
    else:
        count+=1
for i in range(count):
    lst.append(0)
print(lst)
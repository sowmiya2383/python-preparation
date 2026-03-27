s=input().strip()
l=int(input())
lst=[]
for i in range(0,len(s),l):
    lst.append(s[i:i+l])
max_a=0
for i in lst:
    count=i.count('a')
    if count>max_a:
        max_a=count
print(max_a)
arr=[23,5,5,5,5,8,8]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
min_count=min(d.values())
max_count=max(d.values())
for i,count in d.items():
    if count==min_count:
        print(i,end=' ')
    if count==max_count:
        print(i)
  
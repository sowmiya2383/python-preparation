n=int(input())
arr=list(map(int,input().split()))
rank_map={}
rank=1
for i in sorted(arr):
    if i not in rank_map:
        rank_map[i]=rank
        rank+=1
for i in arr:
    print(rank_map[i], end=" ")

    

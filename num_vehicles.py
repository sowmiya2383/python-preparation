v=int(input())
w=int(input())
if w%2!=0 or w<2*v or w>4*v:
    print(-1)
else:
    y=(w-2*v)//2
    x=v-y
    print(x,y)
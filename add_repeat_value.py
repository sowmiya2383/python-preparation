n=input()
r=int(input())
sum=0
result=0
for i in n:
    sum+=int(i)
mul=r*sum
result=0
for i in str(mul):
    result+=int(i) 
print(result)

s=input()
k=int(input())
res=""
for i in range(len(s)):
    if i%k==0:
        res+=s[i]
print(res)
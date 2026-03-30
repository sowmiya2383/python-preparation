str1=input()
str2=input()
remove=set(str2)
res=""
for i in str1:
    if i not in remove:
        res+=i
print(res)
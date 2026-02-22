n=int(input("Enter the number:"))
s=str(n)
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
for i,count in freq.items():
    print(i,count,"times")
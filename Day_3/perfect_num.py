n=int(input("Enter the perfect number:"))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("Perfect number")
else:
    print("Not")
    
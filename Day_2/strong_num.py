n=int(input("Enter a number:"))
temp=n
sum=0
while n>0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i     
    sum=sum+fact
    n=n//10
if sum==temp:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
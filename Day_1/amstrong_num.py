digit=input()
num=int(digit)
sum=0
temp=num
while num>0:
    rem=num%10
    rem=rem**len(digit)
    sum+=rem
    num=num//10
if temp==sum:
    print("true")
else:
    print("false")

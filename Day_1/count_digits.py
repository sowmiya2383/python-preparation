num=int(input("Enter numbers:"))
if num==0:
    count = 1
else:
    count=0
    while num>0:
        num=num//10
        count+=1
print("Count of digits:",count) 
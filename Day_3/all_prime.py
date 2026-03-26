num=int(input())
if num<2:
    print("Value is less than 2")
else:
    for i in range (2,num+1):
        is_prime=True
        j=2
        while j*j<=i:
            if i%j==0:
                is_prime=False
                break
            j+=1
        if is_prime==True:
            print(i)

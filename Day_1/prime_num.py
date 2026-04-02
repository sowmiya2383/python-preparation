num=int(input())
is_prime=True
if num<2:
    is_prime=False
else:
    i=2
    while i*i<=num:
        if num%i==0:
            is_prime=False
            break
        i+=1
if is_prime:
    print("Prime")
else:
    print("Not prime")
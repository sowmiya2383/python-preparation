n = int(input())
square = n * n
print(square)
temp = n

while temp > 0:
    if temp % 10 != square % 10:
        print("False")
        break
    temp //= 10
    square //= 10
else:
    print("True")

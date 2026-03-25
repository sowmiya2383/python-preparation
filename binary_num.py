n=int(input("Enter a number:"))
binary=bin(n)[2:]
toggle=""
for i in binary:
    if i=='0':
        toggle+='1'
    else:
        toggle+='0'
num=int(toggle,2)
print(num)
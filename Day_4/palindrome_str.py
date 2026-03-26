str=input("Enter a string:")
rev=""
temp=str
for ch in str:
    rev=ch+rev
if(temp==rev):
    print("True")
else:
    print("False")
str=input("Enter a string:")
v_count=0
c_count=0
for i in str:
    if i.isalpha():
        if i in "aeiouAEIOU":
            v_count+=1
        else:
            c_count+=1  
print("Vowels:",v_count)
print("Consonants:",c_count)
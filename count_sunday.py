n=int(input("Enter num of days:"))
start_day=input("Enter the starting day:")
days={
    'mon':1, 'tue':2, 'wed':3, 'thurs':4,
    'fri':5, 'sat':6, 'sun':0
}
position=days[start_day]
sun_count=0
if position==0:
    sun_count=0
else:
    sun_count=7-position
if sun_count>=n:
    count=0
else:
    rem=n-sun_count
    count=(1+rem//7)
print("Total num of sundays:",count)


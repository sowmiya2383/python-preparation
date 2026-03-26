n=int(input())
arr=list(map(int,input().split()))

copy = list(arr)

for i in range(n):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

if arr == copy:
      print("Already Sorted")

print(*arr)
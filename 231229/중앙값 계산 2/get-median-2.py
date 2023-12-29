n = int(input())
nums = list(map(int,input().split()))

arr = []
for i in range(n):
    if i % 2 == 0:
        arr = nums[:i+1]
        arr.sort()
        print(arr[len(arr)//2], end =" ")
n = int(input())
nums = list(map(int,input().split()))

sum = 0
lens = 0
for i in range(n):
    if i % 2 ==0:
        sum += nums[i]
        lens += 1
        print(int(sum/lens), end =" ")
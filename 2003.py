n, m = map(int, input().split())

nums = list(map(int, input().split()))

l, r = 0, 1
cnt = 0

while r <= n and l <= r:
    sumNums = nums[l:r]
    total = sum(sumNums)
    if(total == m):
        cnt+=1
        r+=1
    elif(total > m):
        l+=1
    elif(total < m):
        r+=1
print(cnt)
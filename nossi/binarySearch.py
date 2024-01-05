nums = [-1,0,3,5,9,12]
target = 2

#output: 4

l, r = 0, len(nums) - 1


def binarySearch(nums, l, r):
    while True:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if  m > r or m < l:
            return -1
        
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1

print(binarySearch(nums, l, r))

def solution(nums, target):
    nums.sort() # O(nlogn)
    l, r = 0, len(nums) - 1

    # 투포인트
    while l < r:
        if nums[l] + nums[r] == target:
            return [l, r]
        elif nums[l] + nums[r] > target:
            r = r-1
        elif nums[l] + nums[r] < target:
            l = l+1

    return False

print(solution([2, 7, 11, 15], 9))

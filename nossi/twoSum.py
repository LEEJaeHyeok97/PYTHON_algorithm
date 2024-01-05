nums = [4, 9, 7, 5, 1]
target = 14
ans = []



# 재귀
def backtracking():
    for i in range(start, len(nums)):
        ans.append(i)
        if backtracking()


backtracking():



# def twoSum(nums):
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if(nums[i] + nums[j] == target):
#                 ans.append(i)
#                 ans.append(j)
#                 return

# twoSum(nums)
# print(ans)







# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])



# 재귀
# def backtracking():
#     # basecase
#     if len(ans) == 2:
#         print(nums[ans[0]], nums[ans[1]])
#         return 
#     for i in range(len(nums)):
#         ans.append(i)
#         backtracking()
#         ans.pop()

# backtracking()  
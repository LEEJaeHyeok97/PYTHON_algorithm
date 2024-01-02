nums = [4, 9, 7, 5, 1]
target = 14
ans = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])



# 재귀
def backtracking():
    # basecase
    if len(ans) == 2:
        print(nums[ans[0]], nums[ans[1]])
        return 
    for i in range(len(nums)):
        ans.append(i)
        backtracking()
        ans.pop()

backtracking()
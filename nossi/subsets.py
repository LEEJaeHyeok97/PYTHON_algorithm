class Solution:
    def subsets(self, nums):
        def backtracking(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        result = []
        backtracking(0, [])
        return result
    

solution = Solution()
print(solution.subsets([1, 2, 3]))


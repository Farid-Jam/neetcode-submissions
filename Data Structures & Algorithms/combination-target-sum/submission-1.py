class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        def dfs(start, total):
            if total == target:
                res.append(combination.copy())
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                combination.append(nums[i])
                dfs(i, total + nums[i])
                combination.pop()
        dfs(0, 0)
        return res


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(total, idx):
            if total > target:
                return
            
            if total == target:
                res.append(subset.copy())
                return
            
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                dfs(total + nums[i], i)
                subset.pop()
        
        dfs(0, 0)
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(depth):
            if depth >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[depth])
            dfs(depth + 1)
            subset.pop()
            depth += 1
            while depth < len(nums) and nums[depth] == nums[depth - 1]:
                depth += 1
            dfs(depth)


        dfs(0)
        return res
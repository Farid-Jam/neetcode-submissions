class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tracking = [False] * len(nums)
        res = []
        permutation = []
        def dfs(depth):
            if depth >= len(nums):
                res.append(permutation.copy())
            for i in range(len(nums)):
                if tracking[i] == False:
                    tracking[i] = True
                    permutation.append(nums[i])
                    dfs(depth + 1)
                    tracking[i] = False
                    permutation.pop()

        dfs(0)
        return res
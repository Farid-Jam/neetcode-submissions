class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in nums:
            if num - 1 in seen:
                continue
            curr = 1
            i = num + 1
            while i in seen:
                curr += 1
                i += 1
            res = max(curr, res)
        
        return res
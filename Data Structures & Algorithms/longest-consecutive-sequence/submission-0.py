class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in contains:
                continue
            curr = 1
            while num + curr in contains:
                curr += 1
            longest = max(longest, curr)

        return longest
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currTotal = nums[0]

        for i in range(len(nums)):
            if i == 0:
                continue
            if currTotal + nums[i] < nums[i]:
                currTotal = nums[i]
            else:
                currTotal += nums[i]
            res = max(res, currTotal)
        
        return res
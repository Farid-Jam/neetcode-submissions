class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashSet:
                return [hashSet[remainder], i]
            hashSet[nums[i]] = i
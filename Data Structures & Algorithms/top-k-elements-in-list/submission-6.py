class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashSet = defaultdict(int)

        for num in nums:
            hashSet[num] += 1

        freqMap = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashSet.items():
            freqMap[freq].append(num)

        ans = []
        for i in range(len(nums), 0, -1):
            if k <= 0:
                return ans
            for num in freqMap[i]:
                if k <= 0:
                    return ans
                ans.append(num)
                k -= 1
            
        return ans
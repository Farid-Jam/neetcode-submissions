class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freqMap = [[] for i in range(len(nums))]
        for key, value in count.items():
            freqMap[value - 1].append(key)
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            while k != 0 and freqMap[i]:
                res.append(freqMap[i].pop())
                k -= 1

            if k == 0:
                break

        return res
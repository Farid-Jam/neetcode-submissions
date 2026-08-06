class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1

        freqMap = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            freqMap[value].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            while freqMap[i]:
                if k <= 0:
                    return res
                res.append(freqMap[i].pop())
                k -= 1
        return res

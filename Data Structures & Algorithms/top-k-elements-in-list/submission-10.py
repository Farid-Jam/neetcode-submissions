class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqMap = [[] for i in range(len(nums) + 1)]

        for val, cnt in count.items():
            freqMap[cnt].append(val)

        res = []
        for i in range(len(nums), -1, -1):
            while freqMap[i]:
                res.append(freqMap[i].pop())
                k -= 1
                if k == 0:
                    return res
        
        return res
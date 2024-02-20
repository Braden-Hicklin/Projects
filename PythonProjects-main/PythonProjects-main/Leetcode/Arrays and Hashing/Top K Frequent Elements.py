class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = dict()
        solution = []
        for i in nums:
            if i in kMap:
                kMap[i] += 1
            else:
                kMap[i] = 1
        kMap = dict(sorted(kMap.items(), key = lambda x:x[1], reverse=True))
        for i in range(k):
            solution.append(list(kMap.keys())[i])
        return solution


# Uses dictionary to store count of each variable as it shows in list
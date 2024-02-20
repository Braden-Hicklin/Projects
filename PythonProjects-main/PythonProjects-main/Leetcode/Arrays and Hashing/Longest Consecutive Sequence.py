class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        target = 0
        consec = 1
        solution = 1
        for a, b in zip(nums, nums[1:]):
            target = a + 1
            if b == target:
                consec += 1
            else:
                if solution < consec:
                    solution = consec
                consec = 1
            if solution < consec:
                solution = consec
        return solution
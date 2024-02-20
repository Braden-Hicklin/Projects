class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            variable = target - nums[i]
            if variable in numSet:
                return [numSet[variable], i]
            numSet[nums[i]] = i
        return []

# Creates a dictionary hash map where the variable is the key
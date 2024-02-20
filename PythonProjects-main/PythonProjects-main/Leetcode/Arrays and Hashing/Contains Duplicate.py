class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(nums) == len(numSet):
            return False
        return True

# Converts list to set, if there is a duplicate the set will exclude it thus making a smaller list
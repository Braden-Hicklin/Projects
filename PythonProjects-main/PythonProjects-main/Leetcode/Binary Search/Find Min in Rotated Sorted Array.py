class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]

        while l <= r:
            mid = (l+r)// 2
            if nums[mid] >= nums[l]:
                if nums[l] < res:
                    res = nums[l]
                l = mid+1
            else:
                if nums[mid] < res:
                    res = nums[mid]
                r = mid-1
        return res
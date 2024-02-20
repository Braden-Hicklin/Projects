class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = self.bs(nums, 0, len(nums)-1, target)
        return result

    def bs(self, li, l, r, x):
        if r >= l:
            mid = (r + l) // 2
            # Element found in the middle
            if li[mid] == x:
                return mid
            # Element found in the left sublist
            elif li[mid] > x:
                return self.bs(li, l, mid - 1, x)
            # Element found in the right sublist
            else:
                return self.bs(li, mid + 1, r, x)
        # Element doesn't exist in list
        else:
            return -1
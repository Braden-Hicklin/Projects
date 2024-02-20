class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxCon = 0
        con = 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] > height[r]:
                con = height[r] * (r-l)
                r -= 1
            else:
                con = height[l] * (r-l)
                l += 1
            if con > maxCon:
                maxCon = con
        return maxCon
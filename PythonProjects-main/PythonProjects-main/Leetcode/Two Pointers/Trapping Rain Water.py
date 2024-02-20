class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
	# Two pointers left and right
        l, r = 0, len(height)-1
	# Max encountered value of each pointer
        ml, mr = l, r
        while l < r:
            if height[l] <= height[r]:
                l += 1
                if height[ml] < height[l]:
                    ml = l
                else:
                    trapped += height[ml] - height[l]         
            elif height[r] < height[l]:
                r -= 1
                if height[mr] < height[r]:
                    mr = r
                else:
                    trapped += height[mr] - height[r]
        return trapped

# Calculates trapped water as it moves pointers on the left and right hand side
# Which of the two max values is the minimum determines what pointer gets shifted
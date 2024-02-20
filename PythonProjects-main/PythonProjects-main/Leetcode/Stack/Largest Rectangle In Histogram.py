class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def isIncreasing(current, cycBool, newi):
            if not stack:
                stack.append((0, heights[current]))
                return
            if heights[current] >= stack[-1][-1] and cycBool == False:
                stack.append((current, heights[current]))
                return
            elif heights[current] < stack[-1][-1]:
                newi = stack.pop(-1)
                maxArea.append(newi[-1] * (current - newi[0]))
                isIncreasing(current, True, newi)
            else:
                stack.append((newi[0], heights[current]))
                return

        if not heights:
            return 0
        
        stack = []
        maxArea = []
        for i, rects in enumerate(heights):
            isIncreasing(i, False, [0])
        for i in stack:
            maxArea.append(i[-1] * (len(heights) - i[0]))
        return max(maxArea)
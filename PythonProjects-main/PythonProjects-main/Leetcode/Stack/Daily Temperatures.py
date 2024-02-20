class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def MaxTemp(current):
            if stack[-1][0] < current:
                x = stack.pop()[-1]
                ans[x] = i-x
                if stack:
                    MaxTemp(current)
            return

        stack = list()
        ans = list()
        for i, k in enumerate(temperatures):
            if not stack:
                stack.append((k, i))
            else:
                MaxTemp(k)
                stack.append((k,i))
            ans.append(0)
        return ans
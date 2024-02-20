class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compliment = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in compliment.values():
                stack.append(i)
            elif not stack:
                return False
            elif compliment[i] != stack.pop(-1):
                return False
        return not stack

# Leetcode Stats: 
# Runtime = 32ms 
# Memory = 16.27mb
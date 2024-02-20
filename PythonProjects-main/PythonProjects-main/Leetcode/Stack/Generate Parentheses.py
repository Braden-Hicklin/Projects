# The idea is to add ')' only after valid '('
# We use two integer variables left & right to see how many '(' & ')' are in the current string
# If left < n then we can add '(' to the current string
# If right < left then we can add ')' to the current string

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def addPara(left, right, s):
            if len(s) == n * 2:
                stack.append(s)
                return
            if left < n:
                addPara(left + 1, right, s + '(')
            if right < left:
                addPara(left, right + 1, s + ')')
            
        stack = []
        addPara(0, 0, '')
        return stack
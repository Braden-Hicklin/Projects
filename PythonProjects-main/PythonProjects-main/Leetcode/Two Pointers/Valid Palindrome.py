class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
	# Pointers 
        left, right = 0, len(s)-1
        
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            left, right = left +1, right -1
        return True

    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))